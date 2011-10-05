metadata = """
summary @ Lightweight, GTK2-based advanced audio player focused on audio quality
homepage @ http://audacious-media-player.org/
license @ GPL3
src_url @ http://distfiles.atheme.org/$fullname.tar.bz2
arch @ ~x86
options @ altivec chardet nls session sse2
"""

depends = """
runtime @ x11-libs/gtk+:2 dev-libs/libmcs dev-libs/dbus-glib dev-libs/libguess dev-util/desktop-file-utils
        x11-themes/hicolor-icon-theme media-libs/pango x11-libs/cairo
postmerge @ media-plugins/audacious-plugins
"""

opt_runtime = """
session @ x11-libs/libSM
nls @ dev-util/intltool
"""

def configure():
    conf(
    config_enable("altivec"),
    config_enable("chardet"),
    config_enable("nls"),
    config_enable("session", "sm"),
    config_enable("sse2"))

def install():
    raw_install("DESTDIR=%s" % install_dir)
