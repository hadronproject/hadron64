metadata = """
summary @ A C library for reading and writing files containing sampled sound
homepage @ http://www.mega-nerd.com/libsndfile
license @ LGPL
src_url @ http://www.mega-nerd.com/libsndfile/files/$fullname.tar.gz
arch @ ~x86
options @ alsa sqlite static-libs
"""

depends = """
runtime @ dev-util/pkg-config
"""

opt_runtime = """
sqlite @ dev-db/sqlite
alsa @ media-libs/alsa-lib
"""

def configure():
    conf(
	config_enable("sqlite"),
	config_enable("static-libs", "static"),
	config_enable("alsa"),
	"--enable-external-libs",
	"--disable-octave",
	"--disable-gcc-werror",
	"--disable-gcc-pipe")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("AUTHORS", "ChangeLog", "NEWS", "README")

