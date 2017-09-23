importScripts('workbox-sw.prod.v2.0.1.js');

/**
 * DO NOT EDIT THE FILE MANIFEST ENTRY
 *
 * The method precache() does the following:
 * 1. Cache URLs in the manifest to a local cache.
 * 2. When a network request is made for any of these URLs the response
 *    will ALWAYS comes from the cache, NEVER the network.
 * 3. When the service worker changes ONLY assets with a revision change are
 *    updated, old cache entries are left as is.
 *
 * By changing the file manifest manually, your users may end up not receiving
 * new versions of files because the revision hasn't changed.
 *
 * Please use workbox-build or some other tool / approach to generate the file
 * manifest which accounts for changes to local files and update the revision
 * accordingly.
 */
const fileManifest = [
  {
    "url": "/index.html",
    "revision": "87c511d894aa4d54d36a7e8806c4d02f"
  },
  {
    "url": "/static/css/app.a2a6686344dc798b4d955edd25b459cf.css",
    "revision": "ed84fcc9e0e351d0929a9e216828c066"
  },
  {
    "url": "/static/js/app.7f7df18456d110d2af7a.js",
    "revision": "043b950ddc0047d5627ca8231ff392b7"
  },
  {
    "url": "/static/js/manifest.f183ec866b0c52d814f8.js",
    "revision": "c5e4a910ddcf7702ee23fcee6ae05fa8"
  },
  {
    "url": "/static/js/vendor.448f2d15e3f6731dd22b.js",
    "revision": "2109a61b8fcb286b07346860baf9aca3"
  }
];

const workboxSW = new self.WorkboxSW();
workboxSW.precache(fileManifest);
