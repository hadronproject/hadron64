metadata = """
summary @ Firefox Web Browser (binary version)
homepage @ http://www.mozilla.com/firefox
license @ MPL-1.1 GPL-2 LGPL-2.1
src_url @ ftp://ftp.mozilla.org/pub/mozilla.org/firefox/releases/19.0.2/linux-x86_64/en-US/firefox-19.0.2.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ dev-libs/dbus-glib x11-libs/libXrender x11-libs/libXt x11-libs/libXmu x11-libs/gtk+:2 
    media-libs/alsa-lib
build @ app-arch/unzip
"""

standard_procedure = False

srcdir = "firefox"

get("fdo_mime", "gnome2_utils")

def install():
    makedirs("/usr/share/pixmaps")
    makedirs("/usr/share/applications")
    makedirs("/opt")
    insfile("%s/chrome/icons/default/default48.png" % build_dir, "/usr/share/pixmaps/%s.png" % name)
    insfile("%s/%s.desktop" % (filesdir, name), "/usr/share/applications/%s.desktop" % name)
    copytree(build_dir, "/opt/firefox")
    insexe("%s/firefox-bin" % filesdir, "/usr/bin/firefox-bin")

def post_install():
    desktop_database_update()
    gnome2_icon_cache_update()
