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
    "revision": "d0236c938b81439895791b227e675c6f"
  },
  {
    "url": "/static/css/app.a2a6686344dc798b4d955edd25b459cf.css",
    "revision": "ed84fcc9e0e351d0929a9e216828c066"
  },
  {
    "url": "/static/js/app.fbf78670ec8ef2480de5.js",
    "revision": "af24be0b250e31676c0dff6f6c203499"
  },
  {
    "url": "/static/js/manifest.77bd5bf18904d80e389e.js",
    "revision": "1136b8eddce9a9d7fd4ce0f0d215ae49"
  },
  {
    "url": "/static/js/vendor.448f2d15e3f6731dd22b.js",
    "revision": "2109a61b8fcb286b07346860baf9aca3"
  }
];

const workboxSW = new self.WorkboxSW();
workboxSW.precache(fileManifest);
