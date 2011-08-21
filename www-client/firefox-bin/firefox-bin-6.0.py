metadata = """
summary @ Firefox Web Browser (binary version)
homepage @ http://www.mozilla.com/firefox
license @ MPL-1.1 GPL-2 LGPL-2.1
src_url @ ftp://ftp.mozilla.org/pub/firefox/releases/$version/linux-i686/en-US/firefox-$version.tar.bz2 
arch @ ~x86
"""

depends = """
runtime @ dev-libs/dbus-glib x11-libs/libXrender x11-libs/libXt x11-libs/libXmu x11-libs/gtk+
    media-libs/alsa-lib
build @ app-arch/unzip
"""

standard_procedure = False

srcdir = "firefox"

def install():
    system("mkdir -p %s/opt/firefox" % install_dir)
    system("mv * %s/opt/firefox/" % install_dir)
    insexe("%s/firefox-bin" % filesdir, "/usr/bin/firefox-bin")

#TODO: Lots of shit, http://gpo.zugaina.org/AJAX/Ebuild/2420026/View
# startup-notification, desktop files and icon
