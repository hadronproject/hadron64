metadata = """
summary @ XML-XCB protocol descriptions
homepage @ http://xcb.freedesktop.org/
license @ custom
src_url @ http://xcb.freedesktop.org/dist/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
build @ dev-lang/python dev-libs/libxml2
"""

def install():
    export("PYTHONDONTWRITEBYTECODE", "1")
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
