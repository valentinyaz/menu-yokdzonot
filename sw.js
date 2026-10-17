// Guarda el menú en el celular del cliente para que abra aunque no haya señal.
// - Página y precios (index.html, menu-data.js): primero intenta internet (para ver
//   siempre los precios nuevos); si no hay señal en 4 s, usa la copia guardada.
// - Fotos y fuentes: usa la copia guardada al instante y la actualiza en segundo plano.
var CACHE = "menu-yokdzonot-v1";
var BASE = ["./", "index.html", "menu-data.js", "fuentes/fraunces-latin.woff2", "fuentes/outfit-latin.woff2"];

self.addEventListener("install", function (e) {
  e.waitUntil(caches.open(CACHE).then(function (c) { return c.addAll(BASE); }).then(function () { return self.skipWaiting(); }));
});

self.addEventListener("activate", function (e) {
  e.waitUntil(
    caches.keys().then(function (ks) {
      return Promise.all(ks.filter(function (k) { return k !== CACHE; }).map(function (k) { return caches.delete(k); }));
    }).then(function () { return self.clients.claim(); })
  );
});

function primeroRed(req) {
  return caches.open(CACHE).then(function (c) {
    var red = fetch(req).then(function (r) { if (r.ok) c.put(req, r.clone()); return r; });
    var espera = new Promise(function (ok) { setTimeout(ok, 4000); }).then(function () {
      return c.match(req, { ignoreSearch: true });
    });
    // gana internet si responde a tiempo; si no, la copia guardada (si existe)
    return Promise.race([red, espera.then(function (r) { return r || red; })])
      .catch(function () { return c.match(req, { ignoreSearch: true }); });
  });
}

function primeroGuardado(req) {
  return caches.open(CACHE).then(function (c) {
    return c.match(req).then(function (guardado) {
      var red = fetch(req).then(function (r) { if (r.ok) c.put(req, r.clone()); return r; }).catch(function () { return guardado; });
      return guardado || red;
    });
  });
}

self.addEventListener("fetch", function (e) {
  var req = e.request;
  if (req.method !== "GET" || new URL(req.url).origin !== location.origin) return;
  var ruta = new URL(req.url).pathname;
  if (/\/(fotos|fuentes)\//.test(ruta)) e.respondWith(primeroGuardado(req));
  else e.respondWith(primeroRed(req));
});
