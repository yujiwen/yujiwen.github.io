(() => {
  'use strict';
  const dialogs = Array.from(document.querySelectorAll('dialog.contact-dialog'));
  document.querySelectorAll('[data-contact-dialog]').forEach(trigger => {
    trigger.addEventListener('click', event => {
      const dialog = document.getElementById(trigger.dataset.contactDialog);
      if (!dialog || typeof dialog.showModal !== 'function') return;
      event.preventDefault();
      const status = dialog.querySelector('[role="status"]');
      if (status) status.textContent = '';
      dialog.querySelectorAll('img[data-src]').forEach(image => {
        if (!image.getAttribute('src')) image.src = image.dataset.src;
      });
      dialog.showModal();
      document.documentElement.classList.add('contact-dialog-open');
    });
  });
  dialogs.forEach(dialog => {
    dialog.querySelector('[data-dialog-close]').addEventListener('click', () => dialog.close());
    dialog.addEventListener('click', event => {
      if (event.target !== dialog) return;
      const rect = dialog.getBoundingClientRect();
      if (event.clientX < rect.left || event.clientX > rect.right ||
          event.clientY < rect.top || event.clientY > rect.bottom) dialog.close();
    });
    dialog.addEventListener('close', () => {
      if (!dialogs.some(item => item.open)) {
        document.documentElement.classList.remove('contact-dialog-open');
      }
    });
  });
  const copy = document.querySelector('[data-copy-email]');
  if (copy) copy.addEventListener('click', async () => {
    const dialog = copy.closest('dialog');
    const address = dialog.querySelector('.contact-dialog__address').textContent.trim();
    const status = dialog.querySelector('[role="status"]');
    try {
      await navigator.clipboard.writeText(address);
      status.textContent = 'Email copied.';
    } catch (_) {
      status.textContent = 'Please select the email address above to copy it.';
    }
  });
})();
