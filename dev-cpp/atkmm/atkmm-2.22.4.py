metadata = """
summary @ C++ bindings for atk
homepage @ http://gtkmm.sourceforge.net
license @ LGPL
src_url @ http://ftp.gnome.org/pub/GNOME/sources/$name/2.22/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ dev-libs/atk dev-cpp/glibmm dev-libs/libsigc++
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)
