metadata = """
summary @ Complete and free Internet live audio and video broadcasting solution for Linux/Unix
homepage @ http://ffmpeg.org/
license @ GPL
src_url @ http://www.ffmpeg.org/releases/$fullname.tar.bz2
arch @ ~x86_64
options @ lame rtmp vdpau vorbis xvid x264 vpx theora amr schroedinger jpeg2k cpudetection ieee1394 X vaapi
"""

depends = """
runtime @ x11-libs/libXfixes media-libs/alsa-lib app-arch/bzip2
        sys-libs/zlib
        media-libs/SDL_image media-libs/SDL
"""

opt_runtime = """
rtmp @ media-video/rtmpdump dev-util/pkg-config
ieee1394 @ media-libs/libdc1394 sys-libs/libraw1394
lame @ media-sound/lame
vorbis @ media-libs/libvorbis
xvid @ media-libs/xvidcore
x264 @ media-libs/x264
vpx @ media-libs/libvpx
theora @ media-libs/libtheora
amr @ media-libs/opencore-amr
schroedinger @ media-libs/schroedinger dev-util/pkg-config
jpeg2k @ media-libs/openjpeg
X @ x11-libs/libX11 x11-libs/libXext
vaapi @ x11-libs/libva
vdpau @ x11-libs/libvdpau
"""

def configure():
    raw_configure(
    "--prefix=/usr",
"--enable-postproc",
"--enable-shared",
"--enable-gpl",
"--enable-version3",
"--disable-debug",
"--disable-doc",
config_enable("vdpau"),
config_enable("vaapi"),
config_enable("rtmp", "librtmp"),
config_enable("X", "x11grab"),
config_enable("ieee1394", "libdc1394"),
config_enable("cpudetection", "runtime-cpudetect"),
config_enable("xvid", "libxvid"),
config_enable("vorbis", "libvorbis"),
config_enable("theora", "libtheora"),
config_enable("amr", "libopencore_amrwb"),
config_enable("amr", "libopencore_amrnb"),
config_enable("lame", "libmp3lame"))

def build():
    make()
    make("tools/qt-faststart")
    make("doc/ff{mpeg,play,server}.1")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insexe("tools/qt-faststart", "/usr/bin/qt-faststart")


# more options, install-man etc
