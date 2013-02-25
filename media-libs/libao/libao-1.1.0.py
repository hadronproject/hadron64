metadata = """
summary @ A cross-platform audio output library and plugins
homepage @ http://www.xiph.org/ao
license @ GPL
src_url @ http://downloads.xiph.org/releases/ao/$fullname.tar.gz
arch @ ~x86_64
options @ alsa nas mmap static-libs
"""

depends = """
build @ dev-util/pkg-config
"""

opt_runtime = """
alsa @ media-libs/alsa-lib
nas @ media-libs/nas
"""

def prepare():
    sed("-i -e 's:-O20::' configure")

def configure():
	conf(
	config_enable("static-libs", "static"),
	config_enable("alsa"),
	config_enable("mmap", "alsa-mmap"),
	config_enable("nas"),
	"--disable-dependency-tracking",
	"--disable-esd",
	"--disable-arts")

def install():
    raw_install("DESTDIR=%s" % install_dir)
    system("mkdir %s/etc" % install_dir)
    insfile("%s/libao.conf" % filesdir, "/etc/libao.conf")
    insdoc("AUTHORS", "CHANGES", "README", "TODO")

#TODO: option pulseaudio
