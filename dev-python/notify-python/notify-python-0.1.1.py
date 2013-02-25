metadata = """
summary @ Python bindings for libnotify
homepage @ http://www.galago-project.org/
src_url @ http://www.galago-project.org/files/releases/source/$name/$fullname.tar.bz2
license @ LGPL2.1
arch @ ~x86_64
"""

depends = """
runtime @ dev-python/pygtk x11-libs/libnotify
build @ dev-util/pkg-config
"""

def prepare():
    patch()

def configure():
    system("rm -f src/pynotify.c")
    conf()

def build():
    export("PYTHONDONTWRITEBYTECODE", "1")
    make()

def install():
    export("PYTHONDONTWRITEBYTECODE", "1")
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("AUTHORS", "ChangeLog", "NEWS", "README")
