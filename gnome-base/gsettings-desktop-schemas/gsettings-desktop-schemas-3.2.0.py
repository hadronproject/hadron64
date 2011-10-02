metadata = """
summary @ Shared GSettings schemas for the desktop 
homepage @ http://live.gnome.org/ 
license @ GPL 
src_url @ http://ftp.gnome.org/pub/gnome/sources/$name/3.2/$name-$version.tar.bz2 
arch @ ~x86
"""

depends = """
common @ sys-libs/glib
build @ sys-devel/gettext dev-util/intltool
"""

def configure():
	conf(
	"--disable-schemas-compile")

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("AUTHORS", "HACKING", "NEWS", "README")

def post_install():
	system("/usr/bin/glib-compile-schemas /usr/share/glib-2.0/schemas")

def post_remove():
    post_install
