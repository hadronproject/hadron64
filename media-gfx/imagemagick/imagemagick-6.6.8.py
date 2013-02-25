metadata = """
summary @ A collection of tools and libraries for many image formats
homepage @ http://www.imagemagick.org/
license @ custom
src_url @ ftp://ftp.imagemagick.org/pub/ImageMagick/ImageMagick-$version-10.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-devel/libtool media-libs/freetype x11-libs/libXext x11-libs/libXt
          x11-libs/libICE x11-libs/libSM dev-libs/libxml2 media-libs/libpng gnome-base/librsvg
"""

srcdir = "ImageMagick-"+version+"-10"

def configure():
    conf("--with-modules",
            "--disable-static",
            "--enable-openmp",
            "--with-wmf",
            "--with-xml",
            "--with-gslib",
            "--with-gs-font-dir=/usr/share/fonts/Type1"
            "--with-perl",
            '--with-perl-options="INSTALLDIRS=vendor"'
            "--without-gvc",
            "--without-djvu",
            "--without-autotrace",
            "--with-jp2",
            "--without-jbig",
            "--without-fpx",
            "--without-dps",
            "--without-fftw")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("LICENSE", "NOTICE", "AUTHORS.txt", "ChangeLog", "NEWS.txt")
