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
  function play(video) {
    if (document.hidden) return;
    load(video);
    const promise = video.play();
    if (promise) promise.catch(error => {
      // Scrolling away can interrupt a pending play request normally.
      if (error.name !== 'AbortError') video.controls = true;
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
