metadata = """
summary @ The Shared MIME-info Database specification
homepage @ http://freedesktop.org/wiki/Software/shared-mime-info
license @ GPL
src_url @ http://freedesktop.org/~hadess/$fullname.tar.xz
arch @ ~x86
"""

depends = """
runtime @ dev-libs/libxml2 sys-libs/glib
build @ dev-util/intltool dev-util/pkg-config
"""


def prepare():
    patch(level=1)

def configure():
    conf("--disable-update-mimedb")

def build():
    make(j=1)

def install():
    raw_install("DESTDIR=%s" % install_dir)
