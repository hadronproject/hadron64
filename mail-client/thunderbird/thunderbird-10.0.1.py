metadata = """
summary @ Thunderbird Mail Client
homepage @ http://www.mozilla.com/en-US/thunderbird/
license @ MPL-1.1 GPL-2 LGPL-2.1
src_url @ ftp://ftp.mozilla.org/pub/mozilla.org/thunderbird/releases/latest/source/thunderbird-$version.source.tar.bz2
arch @ ~x86
"""

depends = """
common @ media-libs/alsa-lib dev-libs/dbus-glib dev-util/desktop-file-utils x11-libs/gtk+:2 x11-themes/hicolor-icon-theme app-text/hunspell
dev-libs/libevent x11-libs/libnotify media-libs/libvpx x11-libs/libXt x11-misc/shared-mime-info net-libs/xulrunner dev-libs/nss dev-db/sqlite 
x11-libs/startup-notification media-libs/libpng[apng]
build @ dev-lang/yasm
"""

get("extract_utils", "fdo_mime", "gnome2_utils")

standard_procedure = False

srcdir = "comm-release"

def extract():
    tar_extract(fullname+".source.tar.bz2")

def prepare():
    copy("%s/mozconfig" % filesdir, "mozconfig")
    sed("-i 's#VPX_CODEC_USE_INPUT_PARTITION#VPX_CODEC_USE_INPUT_FRAGMENTS#' mozilla/configure")

def build():
    make('-f client.mk build MOZ_MAKE_FLAGS="%s"' % get_env("JOBS"))

def install():
    raw_install("-f client.mk DESTDIR=%s" % install_dir)
    insfile("%s/thunderbird.desktop" % filesdir, \
            "/usr/share/applications/thunderbird.desktop")
    makesym("/usr/lib/thunderbird-%s/chrome/icons/default/default256.png" % raw_version, \
            "/usr/share/pixmaps/thunderbird.png")

def post_install():
    desktop_database_update()
    gnome2_icon_cache_update()

def post_remove():
    desktop_database_update()
    gnome2_icon_cache_update()
