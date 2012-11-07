metadata = """
summary @ Introspection system for GObject-based libraries
homepage @ http://live.gnome.org/GObjectInstrospection
license @ LGPL + GPL
src_url @ http://ftp.gnome.org/pub/gnome/sources/$name/1.30/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glib dev-libs/libffi dev-lang/python:2.7[xml]
"""

def configure():
    export("PYTHONDONTWRITEBYTECODE", "1")
    export("HOME", build_dir)
    export("PYTHON", "/usr/bin/python2")
    #autoreconf("-fi")
    conf(
        "--disable-static",
        "--disable-tests")

#TODO: tests needs cairo, should add some flags to fix that

def build():
    export("PYTHONDONTWRITEBYTECODE", "1")
    export("HOME", build_dir)
    make()

def install():
    export("PYTHONDONTWRITEBYTECODE", "1")
    raw_install("DESTDIR=%s" % install_dir)
