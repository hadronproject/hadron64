metadata = """
summary @ A collection of routines used to create and manipulate MNG format graphics files
homepage @ http://www.libmng.com/
license @ custom
src_url @ http://downloads.sourceforge.net/sourceforge/$name/$fullname.tar.gz
arch @ ~x86
options @ lcms static-libs
"""

depends = """
runtime @ sys-libs/zlib media-libs/jpeg
"""

opt_runtime = """
lcms @ media-libs/lcms
"""

def configure():
	makesym("makefiles/configure.in", "configure.in")
	makesym("makefiles/Makefile.am", "Makefile.am")
	autoreconf("-fi")
	conf(
	"--disable-dependency-tracking",
	"--with-jpeg",
	config_with("lcms"),
    config_enable("static-libs", "static"))

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("CHANGES")
