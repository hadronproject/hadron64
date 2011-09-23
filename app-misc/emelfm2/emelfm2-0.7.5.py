metadata = """
summary @ A file manager that implements the popular two-pane design
homepage @ http://emelfm2.net/
license @ GPL
src_url @ http://emelfm2.net/rel/$fullname.tar.bz2
arch @ ~x86
"""
#TODO: options @ acl policykit spell nls udev gimp

#Gentoo, seriously, WTF is this: http://gpo.zugaina.org/AJAX/Ebuild/2249898/View


depends = """
common @ x11-libs/gtk+ sys-libs/glib
build @ dev-util/pkg-config
"""

opt_runtime = """
udev @ sys-fs/udisks
"""

opt_build = """
nls @ sys-devel/gettext
"""

def build():
	make("PREFIX=%s/usr" % install_dir)

def install():
	make("PREFIX=%s/usr install" % install_dir)
	make("PREFIX=%s/usr install_i18n" % install_dir)

