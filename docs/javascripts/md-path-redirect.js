// Redirect legacy .md URLs to MkDocs directory URLs.
(function () {
  var path = window.location.pathname;
  if (!path || !path.endsWith(".md")) return;

  var normalized = path.replace(/\.md$/, "/");
  var target = normalized + window.location.search + window.location.hash;
  window.location.replace(target);
})();
