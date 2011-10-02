metadata = """
summary @ Chromium Browser Latest Developer Build
homepage @ http://chromium.org/
license @ GPL
arch @ ~x86
"""

depends = """
runtime @ media-libs/alsa-lib dev-util/desktop-file-utils media-libs/libpng gnome-base/gconf
x11-libs/libXtst x11-misc/libxss media-libs/libpng:12
"""

srcdir = "chrome-linux"
standard_procedure = False

import urllib
donk = urllib.urlopen("http://commondatastorage.googleapis.com/chromium-browser-continuous/Linux/LAST_CHANGE")
lastver = donk.read()

src_url = ("http://commondatastorage.googleapis.com/chromium-browser-continuous/Linux/%s/chrome-linux.zip" % lastver)


def install():
    insinto("*", "/opt/chromium-browser/")
    makesym("/opt/chromium-browser/chrome", "/usr/bin/chromium-bin")

def post_install():
    system("chmod +x /usr/bin/chromium-bin")
