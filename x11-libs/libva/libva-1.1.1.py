metadata = """
summary @ Video Acceleration (VA) API for Linux
homepage @ http://freedesktop.org/wiki/Software/vaapi
license @ MIT
src_url @ http://www.freedesktop.org/software/vaapi/releases/$name/$name-$version.tar.bz2
arch @ ~x86_64
options @ vdpau opengl intelvideo
"""

depends = """
runtime @ sys-libs/glibc
"""

opt_postmerge = """
vdpau @ x11-libs/libva-vdpau-driver
"""

opt_runtime = """
intelvideo @ x11-drivers/xf86-video-intel
"""

def configure(): 
    conf(
    config_enable("intelvideo", "i965-driver"),
    config_enable("opengl", "glx"))

def install():
    raw_install("DESTDIR=%s" % install_dir)
    
