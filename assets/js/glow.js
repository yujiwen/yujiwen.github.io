// Homepage background: soft blue light drifting through the margins, drawn live
// with WebGL2. The field is smooth, so it is rendered at a quarter of CSS
// resolution and the browser scales the canvas up. It fades out before the
// text column and pauses whenever the tab is hidden.
(function () {
  'use strict';

  var root = document.querySelector('.site-glow');
  var canvas = root && root.querySelector('.site-glow__canvas');
  if (!root || !canvas) return;

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  var connection = navigator.connection || navigator.mozConnection || navigator.webkitConnection;
  function showStill() { root.classList.add('glow-still'); }
  if (reduced.matches || (connection && connection.saveData)) { showStill(); return; }

  var gl = canvas.getContext('webgl2', {
    alpha: true, premultipliedAlpha: true, antialias: false,
    depth: false, stencil: false, powerPreference: 'low-power'
  });
  if (!gl) { showStill(); return; }

  var VS = [
    '#version 300 es',
    'void main() {',
    '  vec2 p = vec2(gl_VertexID == 1 ? 3.0 : -1.0, gl_VertexID == 2 ? 3.0 : -1.0);',
    '  gl_Position = vec4(p, 0.0, 1.0);',
    '}'
  ].join('\n');

  var FS = [
    '#version 300 es',
    'precision highp float;',
    'uniform vec2 uSize;',    // viewport, CSS px
    'uniform vec2 uTexel;',   // CSS px per canvas pixel
    'uniform float uTime;',
    'uniform vec4 uCol;',     // text column left, right, feather, top of the text (phones), CSS px
    'uniform vec4 uSide;',    // profile box left, top, right, bottom, CSS px
    'uniform float uNarrow;',
    'out vec4 o;',
    'float hash(vec2 p) { vec3 q = fract(vec3(p.xyx) * 0.1031); q += dot(q, q.yzx + 33.33); return fract((q.x + q.y) * q.z); }',
    'float noise(vec2 p) {',
    '  vec2 i = floor(p), f = fract(p);',
    '  vec2 u = f * f * (3.0 - 2.0 * f);',
    '  return mix(mix(hash(i), hash(i + vec2(1.0, 0.0)), u.x), mix(hash(i + vec2(0.0, 1.0)), hash(i + vec2(1.0, 1.0)), u.x), u.y);',
    '}',
    'float fbm(vec2 p) {',
    '  float v = 0.0, a = 0.5;',
    '  for (int i = 0; i < 3; i++) { v += a * noise(p); p = mat2(1.62, 1.18, -1.18, 1.62) * p + 5.1; a *= 0.5; }',
    '  return v;',
    '}',
    'void main() {',
    '  vec2 px = vec2(gl_FragCoord.x * uTexel.x, uSize.y - gl_FragCoord.y * uTexel.y);',
    // Present only outside the text: in the margins on wide screens, above the
    // text on phones.
    '  float f = uCol.z, m;',
    '  float edge;',   // 0 next to the text, 1 far from it
    '  if (uNarrow > 0.5) {',
    '    m = 1.0 - smoothstep(uCol.w - f * 0.6, uCol.w + 6.0, px.y);',
    '    edge = 1.0 - smoothstep(0.0, uCol.w + 1.0, px.y);',
    '  } else {',
    '    m = 1.0 - smoothstep(uCol.x - f, uCol.x - 8.0, px.x) * (1.0 - smoothstep(uCol.y + 8.0, uCol.y + f, px.x));',
    '    edge = smoothstep(0.0, 460.0, max(uCol.x - px.x, px.x - uCol.y));',
    '  }',
    '  if (m <= 0.002) { o = vec4(0.0); return; }',
    // Domain-warped noise gives slow, folding bands of light.
    '  vec2 p = px / 640.0;',
    '  float t = uTime * 0.04;',
    '  vec2 q = vec2(fbm(p + vec2(0.0, t)), fbm(p + vec2(5.2, 1.3) - vec2(t * 0.8, 0.0)));',
    '  vec2 r = vec2(fbm(p + 1.7 * q + vec2(1.7, 9.2) + 0.6 * t), fbm(p + 1.7 * q + vec2(8.3, 2.8) - 0.5 * t));',
    '  float v = fbm(p + 1.5 * r);',
    '  vec3 c = mix(vec3(0.82, 0.90, 1.00), vec3(0.40, 0.63, 0.98), smoothstep(0.30, 0.78, v));',
    '  c = mix(c, vec3(0.30, 0.55, 0.96), edge * smoothstep(0.35, 0.75, v) * 0.35);',
    '  c = mix(c, vec3(0.50, 0.84, 0.97), smoothstep(0.45, 0.85, r.x) * 0.5);',
    '  c = mix(c, vec3(0.70, 0.66, 0.98), smoothstep(0.50, 0.90, q.y) * 0.35);',
    // Two bright spots wander slowly, like light behind frosted glass.
    '  vec2 l1 = vec2(uSize.x * 0.06 + 70.0 * sin(uTime * 0.07), uSize.y * 0.30 + 90.0 * sin(uTime * 0.05 + 1.0));',
    '  vec2 l2 = vec2(uSize.x * 0.95 + 50.0 * sin(uTime * 0.06 + 2.0), uSize.y * 0.70 + 80.0 * sin(uTime * 0.045));',
    '  float glow = exp(-dot(px - l1, px - l1) / 52000.0) + exp(-dot(px - l2, px - l2) / 42000.0);',
    '  c = mix(c, vec3(1.0), clamp(glow, 0.0, 1.0) * 0.75);',
    // Lighter behind the profile text.
    '  vec2 s = vec2(clamp(px.x, uSide.x, uSide.z), clamp(px.y, uSide.y, uSide.w));',
    '  float side = 1.0 - 0.45 * (1.0 - smoothstep(0.0, 60.0, length(px - s)));',
    '  float a = m * side * (0.30 + 0.25 * edge + 0.40 * smoothstep(0.25, 0.75, v));',
    '  o = vec4(c * a, a);',
    '}'
  ].join('\n');

  function compile(type, src) {
    var s = gl.createShader(type);
    gl.shaderSource(s, src);
    gl.compileShader(s);
    if (!gl.getShaderParameter(s, gl.COMPILE_STATUS)) throw new Error(gl.getShaderInfoLog(s));
    return s;
  }
  var prog, u = {};
  try {
    prog = gl.createProgram();
    gl.attachShader(prog, compile(gl.VERTEX_SHADER, VS));
    gl.attachShader(prog, compile(gl.FRAGMENT_SHADER, FS));
    gl.linkProgram(prog);
    if (!gl.getProgramParameter(prog, gl.LINK_STATUS)) throw new Error(gl.getProgramInfoLog(prog));
  } catch (err) {
    if (window.console) console.warn('glow:', err.message);
    showStill();
    return;
  }
  ['uSize', 'uTexel', 'uTime', 'uCol', 'uSide', 'uNarrow'].forEach(function (n) { u[n] = gl.getUniformLocation(prog, n); });
  var vao = gl.createVertexArray();

  /* ---------------------------------------------------------------- layout */

  var TEXEL = 4;   // CSS px per canvas pixel
  var cw = 0, ch = 0, narrow = false, col = [0, 0, 0, 0], side = [-1e5, -1e5, -1e5, -1e5];
  var text = null;

  function measure() {
    cw = window.innerWidth; ch = window.innerHeight;
    canvas.width = Math.ceil(cw / TEXEL);
    canvas.height = Math.ceil(ch / TEXEL);
    text = document.querySelector('.page__content');
    var sb = document.querySelector('.sidebar');
    narrow = cw < 925;
    var r = text ? text.getBoundingClientRect() : { left: cw * 0.3, right: cw * 0.7, top: 0 };
    col = [r.left, r.right, narrow ? 120 : 96, r.top];
    var s = sb && !narrow ? sb.getBoundingClientRect() : null;
    side = s ? [s.left, s.top, s.right, s.bottom] : [-1e5, -1e5, -1e5, -1e5];
  }

  function draw(t) {
    // On phones the light sits above the text and scrolls away with it.
    if (narrow && text) col[3] = text.getBoundingClientRect().top;
    gl.viewport(0, 0, canvas.width, canvas.height);
    gl.useProgram(prog);
    gl.uniform2f(u.uSize, cw, ch);
    gl.uniform2f(u.uTexel, cw / canvas.width, ch / canvas.height);
    gl.uniform1f(u.uTime, t);
    gl.uniform4f(u.uCol, col[0], col[1], col[2], col[3]);
    gl.uniform4f(u.uSide, side[0], side[1], side[2], side[3]);
    gl.uniform1f(u.uNarrow, narrow ? 1 : 0);
    gl.bindVertexArray(vao);
    gl.drawArrays(gl.TRIANGLES, 0, 3);
  }

  /* ------------------------------------------------------------------ loop */

  var start = performance.now(), last = 0, raf = 0, frameGap = 1000 / 30;
  function tick(now) {
    raf = requestAnimationFrame(tick);
    if (now - last < frameGap - 2) return;
    last = now;
    draw((now - start) / 1000 + 20.0);
  }

  var resizeTimer = 0;
  window.addEventListener('resize', function () {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(measure, 120);
  });
  document.addEventListener('visibilitychange', function () {
    if (document.hidden) { cancelAnimationFrame(raf); raf = 0; }
    else if (!raf) { last = 0; raf = requestAnimationFrame(tick); }
  });

  function begin() {
    measure();
    draw(20.0);
    root.classList.add('glow-ready');
    raf = requestAnimationFrame(tick);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', begin, { once: true });
  else begin();
})();
