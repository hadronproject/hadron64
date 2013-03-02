metadata = """
summary @ VDPAU Backend for Video Acceleration (VA) API
homepage @ http://www.freedesktop.org/wiki/Software/vaapi
license @ GPL2
src_url @ http://www.freedesktop.org/software/vaapi/releases/$name/$fullname.tar.bz2
arch @ ~x86_64
options @ opengl
"""

depends = """
common @ >=x11-libs/libva-1.1.0 x11-libs/libvdpau
"""

opt_build = """
opengl @ media-libs/mesa >=x11-libs/libva-1.1.0[opengl]
"""

def prepare():
    patch()
    autoreconf()

def configure():
    conf(
    "--disable-silent-rules",
    config_enable("opengl", "glx"))

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("NEWS", "README", "AUTHORS")
