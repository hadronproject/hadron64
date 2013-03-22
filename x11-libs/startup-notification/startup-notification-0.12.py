metadata = """
summary @ Monitor and display application startup
homepage @ http://www.freedesktop.org/
license @ LGPL
src_url @ http://www.freedesktop.org/software/startup-notification/releases/$fullname.tar.gz
arch @ ~x86_64
options @ static-libs
"""

depends = """
runtime @ x11-libs/libX11 x11-misc/xcb-util
"""

def configure():
    system("sed -i -e '/AC_PATH_XTRA/d' configure.in")
    autoreconf("--force --install")
    conf() 

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("AUTHORS", "ChangeLog", "NEWS", "doc/startup-notification.txt")
