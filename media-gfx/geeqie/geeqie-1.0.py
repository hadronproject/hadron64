metadata = """
summary @ A lightweight image browser and viewer (fork of GQview)
homepage @ http://geeqie.sourceforge.net/
license @ GPL3
src_url @ http://downloads.sourceforge.net/$name/$fullname.tar.gz
arch @ ~x86
options @ exif lcms
"""

depends = """
runtime @ x11-libs/gtk+ dev-util/desktop-file-utils
build @ dev-util/intltool
"""

opt_runtime = """
exif @ media-gfx/exiv2
lcms @ media-libs/lcms
"""

def configure():
	export("CPPFLAGS", "-D_FILE_OFFSET_BITS=64")
	conf(
	"-disable-dependency-tracking",
	config_enable("lcms"),
	config_enable("exif", "exiv2"))

def install():
	raw_install("DESTDIR=%s" % install_dir)

