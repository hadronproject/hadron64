metadata = """
summary @ Nouveau driver (GIT)
homepage @ http://nouveau.freedesktop.org/
license @ GPL
src_url @ http://xorg.freedesktop.org/archive/individual/driver/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
build @ x11-proto/glproto x11-proto/xf86driproto x11-proto/dri2proto x11-libs/libdrm
"""

def install():
    installd()
    insfile("%s/30-nouveau.conf" % filesdir, "/etc/X11/xorg.conf.d/")
