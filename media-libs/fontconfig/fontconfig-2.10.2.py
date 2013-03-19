metadata = """
summary @ A library for configuring and customizing font access
homepage @ http://www.fontconfig.org/release/
license @ custom
src_url @ http://www.fontconfig.org/release/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc media-libs/freetype dev-libs/expat
"""

def prepare():
    patch(level=1)

def configure():
    conf("--disable-docs")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")

def post_install():
    notify("building fonts.cache")
    if not system("/usr/bin/fc-cache -r"):
        raise BuildError
