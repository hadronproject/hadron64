metadata = """
summary @ Nouveau driver (GIT)
homepage @ http://nouveau.freedesktop.org/
license @ GPL
arch @ ~x86
"""

depends = """
build @ x11-proto/glproto x11-proto/xf86driproto x11-proto/dri2proto x11-libs/libdrm
"""

def prepare():
    notify("cloning git://anongit.freedesktop.org/git/nouveau/xf86-video-nouveau.git")
    if not system("git clone git://anongit.freedesktop.org/git/nouveau/xf86-video-nouveau.git"):
        error("git clone failed.")

def configure():
    cd(name)
    system("./autogen.sh")
    conf()

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insfile("%s/30-nouveau.conf" % filesdir, "/etc/X11/xorg.conf.d/")
