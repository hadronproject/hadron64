metadata = """
summary @ C++ bindings for gtk2
homepage @ http://gtkmm.sourceforge.net
license @ LGPL
src_url @ http://ftp.gnome.org/pub/GNOME/sources/$name/2.24/$fullname.tar.bz2
arch @ ~x86
"""


depends = """
runtime @ x11-libs/gtk+ dev-cpp/pangomm dev-cpp/cairomm
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)

