// Fetch paper clips near the viewport; decode only the clips readers can see.
(() => {
  'use strict';
  const videos = Array.from(document.querySelectorAll('video.paper-video[data-src]'));
  const visible = new Set();
  function load(video) {
    if (video.getAttribute('src')) return;
    video.preload = 'auto';
    video.src = video.dataset.src;
    video.load();
  }
  // Some browsers refuse to autoplay even muted clips (iOS Low Power Mode,
  // embedded web views). A tap or key press anywhere counts as permission, so
  // the visible clips are retried on the first one.
  let waitingForGesture = false;
  function retryOnGesture() {
    if (waitingForGesture) return;
    waitingForGesture = true;
    const kinds = ['pointerdown', 'touchend', 'keydown'];
    const retry = () => {
      kinds.forEach(kind => document.removeEventListener(kind, retry, true));
      waitingForGesture = false;
      visible.forEach(play);
    };
    kinds.forEach(kind => document.addEventListener(kind, retry, { capture: true, passive: true }));
  }
  function play(video) {
    if (document.hidden) return;
    load(video);
    const promise = video.play();
    if (promise) promise.then(() => { video.controls = false; }, error => {
      // Scrolling away can interrupt a pending play request normally.
      if (error.name === 'AbortError') return;
      video.controls = true;
      if (error.name === 'NotAllowedError') retryOnGesture();
    });
  }
  if ('IntersectionObserver' in window) {
    const nearby = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        load(entry.target);
        nearby.unobserve(entry.target);
      });
    }, { rootMargin: '250px 0px' });
    const onscreen = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          visible.add(entry.target);
          play(entry.target);
        } else {
          visible.delete(entry.target);
          entry.target.pause();
        }
      });
    });
    videos.forEach(video => { nearby.observe(video); onscreen.observe(video); });
  } else {
    videos.forEach(video => { visible.add(video); play(video); });
  }
  document.addEventListener('visibilitychange', () => {
    videos.forEach(video => {
      if (document.hidden || !visible.has(video)) video.pause();
      else play(video);
    });
  });
})();
