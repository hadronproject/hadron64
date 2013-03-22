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

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("AUTHORS", "ChangeLog", "NEWS", "doc/startup-notification.txt")
