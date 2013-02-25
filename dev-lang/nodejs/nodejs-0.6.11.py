metadata = """
summary @ Evented I/O for V8 javascript
homepage @ http://nodejs.org/
license @ MIT
src_url @ http://nodejs.org/dist/v$version/node-v$version.tar.gz
arch @ ~x86_64
"""

depends = """
common @ dev-lang/python:2.7[threads]
"""

get("waf")

srcdir = "node-v%s" % (version)

configure = lambda: raw_configure("--prefix=/usr")

def install():
    installd()
    insdoc("LICENSE")
    insinto("doc/api/api/*", "/usr/share/doc/nodejs/")

