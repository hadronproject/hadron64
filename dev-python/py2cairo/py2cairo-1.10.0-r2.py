get("waf")

metadata = """
summary @ Python2 bindings for the cairo graphics library
homepage @ http://www.cairographics.org/pycairo
license @ LGPL + MPL
src_url @ http://cairographics.org/releases/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ x11-libs/cairo dev-lang/python:2.7
"""

srcdir = "py2cairo-%s" % raw_version
