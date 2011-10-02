metadata = """
summary @ A collection of tools and libraries for many image formats
homepage @ http://www.imagemagick.org/
license @ custom
src_url @ ftp://ftp.imagemagick.org/pub/ImageMagick/ImageMagick-$version-9.tar.bz2
arch @ ~x86
options @ bzip2 fontconfig jpeg lcms perl png svg tiff truetype X xml lzma zlib static-libs
"""

depends = """
runtime @ sys-devel/libtool
"""

opt_runtime = """
bzip2 @ app-arch/bzip2
fontconfig @ media-libs/fontconfig
jpeg @ media-libs/jpeg
lcms @ media-libs/lcms
perl @ dev-lang/perl
png @ media-libs/libpng
tiff @ media-libs/tiff
truetype @ media-libs/freetype
X @ x11-libs/libXext x11-libs/libXt x11-libs/libICE x11-libs/libSM
xml @ dev-libs/libxml2
lzma @ app-arch/xz
zlib @ sys-libs/zlib
svg @ gnome-base/librsvg
"""

srcdir = "ImageMagick-"+version+"-9"

def configure():
    conf("--with-modules",
            config_enable("static-libs", "static"),
            "--enable-openmp",
            "--with-wmf",
            "--with-gslib",
            "--with-gs-font-dir=/usr/share/fonts/Type1",
            config_with("perl"),
            '--with-perl-options="INSTALLDIRS=vendor"',
            "--without-gvc",
            "--without-djvu",
            "--without-autotrace",
            "--with-jp2",
            "--without-jbig",
            "--without-fpx",
            "--without-dps",
            "--without-fftw",
            "--with-magick-plus-plus",
            config_with("bzip2", "bzlib"),
            config_with("X", "x"),
            config_with("zlib"),
            config_with("fontconfig"),
            config_with("truetype", "freetype"),
            config_with("jpeg"),
            "--without-lcms",
            config_with("lcms", "lcms2"),
            config_with("lzma"),
            config_with("png"),
            config_with("svg", "rsvg"),
            config_with("tiff"),
            config_with("xml"))

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("LICENSE", "NOTICE", "AUTHORS.txt", "ChangeLog", "NEWS.txt")
