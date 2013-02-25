metadata = """
summary @ A front-end for CORBA 2.2 IDL and Netscape's XPIDL
homepage @ http://www.gnome.org
license @ LGPL
src_url @ http://ftp.gnome.org/pub/gnome/sources/libIDL/0.8/libIDL-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glib sys-apps/texinfo
"""

srcdir = "libIDL-%s" % version

def install():
    raw_install("DESTDIR=%s" % install_dir)
