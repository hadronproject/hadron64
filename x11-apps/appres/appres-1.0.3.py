metadata = """
summary @ list X application resource database
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/archive/individual/app/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ x11-libs/libXt
build @ x11-misc/util-macros
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insfile("COPYING", "/usr/share/licenses/%s" % name)
