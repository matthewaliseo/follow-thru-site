// Share button: the phone's share sheet where it exists, otherwise copy the link.
document.querySelectorAll('[data-share-url]').forEach(function (btn) {
  btn.addEventListener('click', function () {
    var url = btn.getAttribute('data-share-url');
    var status = btn.closest('section').querySelector('.share-status');
    var data = {
      title: btn.getAttribute('data-share-title') || 'CounterWait in 27 Seconds',
      text: btn.getAttribute('data-share-text') || 'Lock the apps you choose and earn the time back with exercise and tasks.',
      url: url
    };
    if (navigator.share) {
      navigator.share(data).catch(function () {});
    } else if (navigator.clipboard) {
      navigator.clipboard.writeText(url).then(function () { if (status) status.textContent = 'Link copied.'; });
    } else if (status) {
      status.textContent = url;
    }
  });
});
