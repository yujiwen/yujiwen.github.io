// Page background video: keep it cheap, and never let it get in the way.
(function () {
  var backdrop = document.querySelector('.robotics-background');
  var video = document.getElementById('robotics-background-video');
  if (!backdrop || !video) return;

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  var small = window.matchMedia('(max-width: 760px)');
  var connection = navigator.connection || navigator.mozConnection || navigator.webkitConnection;

  function reveal() {
    backdrop.classList.add('scene-ready');
  }

  function showStill() {
    video.pause();
    backdrop.classList.add('scene-still');
    reveal();
  }

  function play() {
    var played = video.play();
    // Autoplay can be refused (data saver, strict browser policy). The still
    // frame is already on screen in that case, so just show it.
    if (played && typeof played.catch === 'function') played.catch(showStill);
  }

  // A still frame is the whole experience for these readers, so don't spend
  // bandwidth on a clip that will never be seen.
  if (reduced.matches || (connection && connection.saveData)) {
    showStill();
    return;
  }

  video.addEventListener('loadeddata', function () {
    backdrop.classList.remove('scene-still');
    reveal();
  }, { once: true });
  video.addEventListener('error', showStill, { once: true });

  function start() {
    // Choose one file rather than shipping a <source> list: <video> ignores the
    // media attribute, so the browser would otherwise fetch the large file even
    // on a phone.
    video.src = small.matches ? video.dataset.srcSm : video.dataset.src;
    play();
  }

  // Let the page's own CSS, fonts and images land first; the clip is decoration
  // and must not compete with them for bandwidth.
  if (document.readyState === 'complete') {
    start();
  } else {
    window.addEventListener('load', start, { once: true });
  }

  // Never decode frames nobody is looking at.
  document.addEventListener('visibilitychange', function () {
    if (document.hidden) {
      video.pause();
    } else if (video.src && !reduced.matches && !backdrop.classList.contains('scene-still')) {
      play();
    }
  });

  // The source is chosen once on load; a resize across the breakpoint should
  // not restart the clip.
})();
