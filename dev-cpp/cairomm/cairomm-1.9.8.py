metadata = """
summary @ C++ bindings for the Cairo vector graphics library
homepage @ http://cairographics.org/cairomm
license @ LGPL-2
src_url @ http://cairographics.org/releases/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ x11-libs/cairo dev-libs/libsigc++
build @ dev-util/pkg-config
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)
