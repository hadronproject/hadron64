metadata = """
summary @ A library for portable low-level access to a video framebuffer, audio output, mouse, and keyboard
homepage @ http://www.libsdl.org/
license @ LGPL
src_url @ http://www.libsdl.org/release/$fullname.tar.gz
arch @ ~x86_64
options @ alsa nas X dga xv xinerama static-libs alsa-shared pulseaudio pulseaudio-shared
"""

depends = """
build @ media-libs/mesa
"""

opt_runtime = """
pulseaudio @ media-sound/pulseaudio
alsa @ media-libs/alsa-lib
X @ x11-libs/libXt x11-libs/libXext x11-libs/libX11 x11-libs/libXrandr
nas @ media-libs/nas x11-libs/libXt x11-libs/libXext x11-libs/libX11
"""

opt_build = """
nas @ x11-proto/xextproto x11-proto/xproto
X @ x11-proto/xextproto x11-proto/xproto
"""

def prepare():
    patch(level=1)

def configure():

    myconf = ""
    if not opt("alsa-shared"):
        myconf += " --disable-alsa-shared "

    if not opt("pulseaudio-shared"):
        myconf += " --disable-pulseaudio-shared "

        conf(
        "--disable-rpath",
        "--disable-arts",
        "--disable-esd",
        "--enable-events",
        "--enable-cdrom",
        "--enable-threads",
        "--enable-timers",
        "--enable-file",
        "--enable-cpuinfo",
        "--disable-esd-shared",
        "--disable-arts-shared",
        "--disable-nas-shared",
        "--disable-osmesa-shared",
        "--disable-video-x11-xme",
        config_enable("alsa"),
        config_enable("X", "video-x11"),
    config_enable("nas"),
    config_enable("pulseaudio"),
    config_enable("dga"),
    config_enable("dga", "video-dga"),
    config_enable("xv", "video-x11-xv"),
    config_enable("xinerama", "video-x11-xinerama"),
    config_enable("X", "video-x11-xrandr"),
    config_with("X", "x"),
    config_enable("static-libs", "static"), myconf)

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("BUGS", "CREDITS", "README", "README-SDL.txt", "README.CVS", "TODO", "WhatsNew")
