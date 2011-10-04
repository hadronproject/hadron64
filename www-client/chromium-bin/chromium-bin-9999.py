metadata = """
summary @ Chromium Browser Latest Developer Build
homepage @ http://chromium.org/
license @ GPL
arch @ ~x86
"""

depends = """
runtime @ media-libs/alsa-lib dev-util/desktop-file-utils media-libs/libpng gnome-base/gconf
x11-libs/libXtst x11-misc/libxss media-libs/libpng:12 net-print/cups
"""

standard_procedure = False

def prepare():
    color("** Determining latest build version **", "green")
    import urllib   
    try:
        donk = urllib.urlopen("http://commondatastorage.googleapis.com/chromium-browser-continuous/Linux/LAST_CHANGE")
    except:
        warning("Couldn't read the version info, this is going to fail.")
    lastver = donk.read()
    notify("Revision %s" % lastver)
    system("rm -fr chrome-linux.zip")
    system("wget http://commondatastorage.googleapis.com/chromium-browser-continuous/Linux/%s/chrome-linux.zip" % lastver)
    system("unzip chrome-linux.zip")

def install():
    cd("chrome-linux")
    insinto("*", "/opt/chromium-browser/")
    insexe("%s/chromium-browser.sh" % filesdir, "/usr/bin/chromium-bin")
    insfile("%s/chromium-browser.default" % filesdir, "/etc/chromium-browser/default")
    insfile("%s/chromium-browser.desktop" % filesdir, "/usr/share/applications/chromium-browser.desktop")
    makesym("%s/opt/product_logo_48.png", "/usr/share/pixmaps/product_logo_48.png")

def post_install():
    system("chmod +x /opt/chromium-browser/chrome")
    system("chmod +x /opt/chromium-browser/chrome-wrapper")
    system("update-desktop-database -q")
