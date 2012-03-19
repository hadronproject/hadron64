metadata = """
summary @ Chromium Browser Latest Developer Build
homepage @ http://chromium.org/
license @ GPL
arch @ ~x86
"""

depends = """
runtime @ media-libs/alsa-lib dev-util/desktop-file-utils gnome-base/gconf
x11-libs/libXtst x11-misc/libxss media-libs/libpng:1.2 dev-libs/nss
"""

get("fdo_mime", "gnome2_utils")

standard_procedure = False

srcdir = "chrome-linux"

def extract():
    color("** Determining latest build version **", "green")
    import urllib   
    try:
        donk = urllib.urlopen("http://commondatastorage.googleapis.com/chromium-browser-continuous/Linux/LAST_CHANGE")
    except:
        warn("Couldn't read the version info, this is going to fail.")
    lastver = donk.read()
    notify("Revision %s" % lastver)
    system("rm -fr chrome-linux.zip")
    fetch("http://commondatastorage.googleapis.com/chromium-browser-continuous/Linux/%s/chrome-linux.zip" % lastver)
    unpack("chrome-linux.zip")

def install():
    insinto("*", "/opt/chromium-browser/")
    insexe("%s/chromium-browser.sh" % filesdir, "/usr/bin/chromium-bin")
    insfile("%s/chromium-browser.default" % filesdir, "/etc/chromium-browser/default")
    insfile("%s/chromium-browser.desktop" % filesdir, "/usr/share/applications/chromium-browser.desktop")
    makesym("%s/opt/product_logo_48.png" % filesdir, "/usr/share/pixmaps/product_logo_48.png")

def post_install():
    setmod("+x /opt/chromium-browser/chrome")
    setmod("+x /opt/chromium-browser/chrome-wrapper")
    desktop_database_update()
    gnome2_icon_cache_update()
