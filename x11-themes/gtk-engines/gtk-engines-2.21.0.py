metadata = """
summary @ Theme engines for GTK+ 2
homepage @ http://live.gnome.org/GnomeArt
license @ GPL LGPL
src_url @ ftp://ftp.archlinux.org/other/$name/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
build @ dev-util/pkg-config dev-util/intltool
"""

def configure():
    conf("--enable-animation")

def install():
    raw_install("DESTDIR=%s" % install_dir)
