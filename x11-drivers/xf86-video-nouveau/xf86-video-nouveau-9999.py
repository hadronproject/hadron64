metadata = """
summary @ Nouveau driver (GIT)
homepage @ http://nouveau.freedesktop.org/
license @ GPL
arch @ ~x86
"""

depends = """
build @ x11-proto/glproto x11-proto/xf86driproto x11-proto/dri2proto x11-libs/libdrm
"""

srcdir = "down"

def prepare():
    notify("cloning git://anongit.freedesktop.org/git/nouveau/xf86-video-nouveau.git")
    if not system("git clone git://anongit.freedesktop.org/git/nouveau/xf86-video-nouveau.git down"):
        error("git clone failed.")

def configure():
    cd("down")
    system("./autogen.sh")
    conf()

def build():
    cd("down")
    make()

def install():
    cd("down")
    raw_install("DESTDIR=%s" % install_dir)

