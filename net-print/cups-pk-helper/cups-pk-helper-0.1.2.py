metadata = """
summary @ A helper that makes system-config-printer use PolicyKit 
homepage @ http://www.freedesktop.org/software/cups-pk-helper/releases/ 
license @ GPL 
src_url @ http://www.freedesktop.org/software/$name/releases/$name-$version.tar.bz2 
arch @ ~x86
"""

depends = """
runtime @ sys-auth/polkit dev-libs/dbus-glib net-print/cups 
build @ dev-util/intltool
"""

def configure():
	conf(
	"--libexecdir=/usr/lib/cups-pk-helper")

def install():
	raw_install("DESTDIR=%s" % install_dir)


