metadata = """
summary @ A multi-platform MPEG, VCD/DVD, and DivX player
homepage @ http://www.videolan.org/vlc/
license @ LGPL2.1 + GPL2
src_url @ http://download.videolan.org/pub/videolan/$name/$version/$fullname.tar.xz
arch @ ~x86
options @ a52 aac alsa altivec avcodec avformat cddb dc1394 dvbpsi dvd dvdnav dts flac fontconfig gcrypt gnutls ieee1394 libnotify libsamplerate mp3 mpeg ncurses ogg opengl png qt4 schroedinger sdl sdl-image sqlite svg taglib theora truetype vaapi vorbis X x264 xcb xml lua postproc skins debug kde media-library mmx neon optimisememory run-as-root sse xv
"""

depends = """
build @ app-arch/xz
runtime @ sys-libs/zlib dev-util/pkg-config sys-apps/dbus sys-fs/udev
"""

opt_runtime = """
a52 @ >=media-libs/a52dec-0.7.4-r3
aac @ >=media-libs/faad2-2.6.1
alsa @ >=media-libs/alsa-lib-1.0.23
avcodec @ media-video/ffmpeg
avformat @ media-video/ffmpeg
cddb @ >=media-libs/libcddb-1.2.0
dc1394 @ >=sys-libs/libraw1394-2.0.1 >=media-libs/libdc1394-2.0.2
dts @ media-libs/libdca
dvbpsi @ >=media-libs/libdvbpsi-0.1.6
dvd @ media-libs/libdvdread >=media-libs/libdvdnav-0.1.9
flac @ media-libs/libogg >=media-libs/flac-1.1.2
fontconfig @ media-libs/fontconfig || media-fonts/dejavu
gcrypt @ >=dev-libs/libgcrypt-1.2.0
    gnutls @ >=net-libs/gnutls-2.0.0
ieee1394 @ >=sys-libs/libraw1394-2.0.1 >=sys-libs/libavc1394-0.5.3
kde @ kde-base/kdelibs
libnotify @ x11-libs/libnotify x11-libs/gtk+:2
libsamplerate @ media-libs/libsamplerate
lua @ >=dev-lang/lua-5.1
media-library @ dev-db/sqlite
mp3 @ media-libs/libmad
mpeg @ >=media-libs/libmpeg2-0.3.2
mtp @ >=media-libs/libmtp-1.0.0
ncurses @ sys-libs/ncurses
ogg @ media-libs/libogg
opengl @ media-libs/mesa >=x11-libs/libX11-1.3.99.901
png @ media-libs/libpng sys-libs/zlib
postproc @ media-video/ffmpeg
schroedinger @ >=media-libs/schroedinger-1.0.10
skins @ x11-libs/libXext x11-libs/libXpm
sqlite @ >=dev-db/sqlite-3.6.0
svg @ >=gnome-base/librsvg-2.9.0
taglib @ >=media-libs/taglib-1.5 sys-libs/zlib
theora @ media-libs/libtheora
truetype @ media-libs/freetype
vaapi @ x11-libs/libva
vorbis @ media-libs/libvorbis
X @ x11-libs/libX11
    qt4 @ x11-libs/qt
    sdl @ >=media-libs/SDL-1.2.8
        sdl-image @ media-libs/SDL_image sys-libs/zlib
x264 @ media-libs/x264
xcb @ >=x11-libs/libxcb-1.6 >=x11-misc/xcb-util-0.3.4
    xv @ x11-libs/libXv
xml @ dev-libs/libxml2
"""

#TODO: avcodec and X needed for vaapi

def configure():
    conf(
    config_enable("a52"),
    config_enable("aac", "faad"),
    config_enable("alsa"),
    config_enable("altivec"),
    config_enable("avcodec"),
    config_enable("avformat"),
    config_enable("cddb", "libcddb"),
    config_enable("dc1394"),
    config_enable("debug"),
    config_enable("dts", "dca"),
    config_enable("dvbpsi"),
    config_enable("dvd", "dvdread"),
    config_enable("dvd", "dvdnav"),
    config_enable("flac"),
    config_enable("fontconfig"),
    config_enable("gcrypt", "libgcrypt"),
    config_enable("gnutls"),
    config_enable("ieee1394", "dv"),
    config_with("kde", "kde-solid"),
    config_enable("libnotify", "notify"),
    config_enable("libsamplerate", "samplerate"),
    config_enable("lua"),
    config_enable("media-library"),
    config_enable("mmx"),
    config_enable("mp3", "mad"),
    config_enable("mpeg", "libmpeg2"),
    config_enable("ncurses"),
    config_enable("neon"),
    config_enable("ogg"),
    config_enable("opengl", "glx"),
    config_enable("optimisememory", "optimize-memory"),
    config_enable("png"),
    config_enable("postproc"),
    config_enable("qt4"),
    config_enable("run-as-root"),
    config_enable("schroedinger"),
    config_enable("sdl"),
    config_enable("sdl-image"),
    config_enable("skins", "skins2"),
    config_enable("sqlite"),
    config_enable("sse"),
    config_enable("svg"),
    config_enable("taglib"),
    config_enable("theora"),
    config_enable("truetype", "freetype"),
    config_enable("vaapi", "libva"),
    config_enable("vorbis"),
    config_with("X", "x"),
    config_enable("x264"),
    config_enable("xcb"),
    config_enable("xml", "libxml2"),
    config_enable("xv", "xvideo"),
    "--disable-optimizations",
    "--without-tuning",
    "--enable-fast-install",
    "--enable-dbus --enable-dbus-control",
    "--enable-sout")

def install():
    installd()

    insdoc("README", "AUTHORS", "THANKS", "NEWS")

def post_install():
    warn("** Please run vlc-cache-gen manually **")
