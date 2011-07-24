metadata = """
summary @ Python bindings for the GTK widget set
homepage @ http://www.pygtk.org/
license @ LGPL
src_url @ http://ftp.gnome.org/pub/gnome/sources/$name/2.24/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ gnome-base/libglade dev-python/py2cairo dev-python/pygobject
"""

import os

def prepare():
	patch(level=1)
	move("py-compile", "py-compile.orig")
	makesym("/bin/true", "py-compile")
	#export("AT_M4DIR", "m4")
	#print system('autoreconf')
	#autoreconf()

def configure():
    conf("--prefix=/usr --with-glade --enable-thread --disable-docs")

def build():
    export("PYTHONDONTWRITEBYTECODE", "1")
    make()

def install():
	raw_install("DESTDIR=%s" % install_dir)

