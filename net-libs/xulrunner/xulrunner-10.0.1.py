metadata = """
summary @ Mozilla runtime package that can be used to bootstrap XUL+XPCOM applications
homepage @ http://developer.mozilla.org/en/docs/XULRunner
license @ MPL-1.1 GPL-2 LGPL-2.1
src_url @ ftp://ftp.mozilla.org/pub/mozilla.org/firefox/releases/$version/source/firefox-$version.source.tar.bz2
arch @ ~x86_64
"""

depends = """
common @ media-libs/alsa-lib dev-libs/dbus-glib dev-util/desktop-file-utils x11-libs/gtk+:2 x11-themes/hicolor-icon-theme app-text/hunspell
dev-libs/libevent x11-libs/libnotify media-libs/libvpx x11-libs/libXt x11-misc/shared-mime-info dev-libs/nss dev-db/sqlite 
x11-libs/startup-notification media-libs/libpng[apng]
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
    raw_install("-C xulrunner-build-dir DESTDIR=%s" % install_dir)
    makedirs("/usr/lib/mozilla")
    rmdir("/usr/lib/xulrunner-%s/plugins" % raw_version)
    makesym("../mozilla/plugins", "/usr/lib/xulrunner-%s/plugins" % raw_version)
    #setowner("-Rv root:root %s/usr/{include,lib,share/idl}/xulrunner-*" % install_dir)


