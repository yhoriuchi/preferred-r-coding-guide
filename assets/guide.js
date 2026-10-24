'use strict';
const copyButton = document.getElementById('copy-guide');
if (copyButton) {
  copyButton.addEventListener('click', async () => {
    const text = JSON.parse(document.getElementById('guide-text').textContent);
    const status = document.getElementById('copy-status');
    try {
      if (!navigator.clipboard) throw new Error('Clipboard unavailable');
      await navigator.clipboard.writeText(text);
      status.textContent = 'Complete guide and instructions copied.';
    } catch {
      const fallback = document.getElementById('copy-fallback');
      const textarea = document.getElementById('copy-text');
      fallback.hidden = false;
      fallback.open = true;
      textarea.value = text;
      textarea.focus();
      textarea.select();
      status.textContent = 'Text selected below. Press Cmd+C or Ctrl+C to copy.';
    }
  });
}
