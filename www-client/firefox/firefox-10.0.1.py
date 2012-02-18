metadata = """
summary @ Web Browser by Mozilla
homepage @ http://www.mozilla.com/en-US/firefox
license @ MPL-1.1 GPL-2 LGPL-2.1
src_url @ ftp://ftp.mozilla.org/pub/mozilla.org/firefox/releases/$version/source/firefox-$version.source.tar.bz2
arch @ ~x86
"""

depends = """
common @ media-libs/alsa-lib dev-libs/dbus-glib dev-util/desktop-file-utils x11-libs/gtk+:2 x11-themes/hicolor-icon-theme app-text/hunspell
dev-libs/libevent x11-libs/libnotify media-libs/libvpx x11-libs/libXt x11-misc/shared-mime-info net-libs/xulrunner dev-libs/nss dev-db/sqlite 
x11-libs/startup-notification media-libs/libpng[apng] media-libs/mesa
build @ dev-lang/yasm
"""

standard_procedure = False

srcdir = "mozilla-release"

def prepare():
    copy("%s/mozconfig" % filesdir, "mozconfig")
    sed("-i 's#VPX_CODEC_USE_INPUT_PARTITION#VPX_CODEC_USE_INPUT_FRAGMENTS#' configure")
    sed("-i '/Version/aRequires: nspr >= 4.8.9' xulrunner/installer/libxul-embedding.pc.in")

def build():
    make('-f client.mk MOZ_MAKE_FLAGS="%s"' % get_env("JOBS"))

def install():
    raw_install("-C firefox-build-dir DESTDIR=%s" % install_dir)
    makedirs("/usr/lib/mozilla/plugins")
    rmdir("/usr/lib/firefox-%s/plugins" % raw_version)
    makesym("../mozilla/plugins", "/usr/lib/firefox-%s/plugins" % raw_version)
    insfile("%s/firefox.desktop" % filesdir, "/usr/share/applications/firefox.desktop")
    makesym("/usr/lib/firefox-%s/icons/mozicon128.png" % raw_version, "/usr/share/pixmaps/firefox.png")

    #setowner("-R root:root %s/usr/lib/firefox-*" % install_dir)


