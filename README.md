inliner
=======

Inlines various assets in an HTML page, specifically, so far it handles:

    - Inlining local relative images into data URIs
    - Inlining link[type=text/css] into style tags.

With plans to handle:

    - Inlining scripts.
    - Automatically running converter and converting content types
      of embedded resources (e.g. CoffeeScript -> JavaScript, Less -> CSS,
      etc)


inline -h for help.


TODOs
=====
- Only replace local references.
- Default to automatically creating backup files with option to disable.
- Options to only do CSS or only do data URIs, etc.
- Inline scripts too.
