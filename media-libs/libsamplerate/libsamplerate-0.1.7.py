metadata = """
summary @ Secret Rabbit Code - aka Sample Rate Converter for audio
homepage @ http://www.mega-nerd.com/SRC/index.html
license @ GPL
src_url @ http://www.mega-nerd.com/SRC/$fullname.tar.gz
arch @ ~x86
options @ sndfile
"""

depends = """
build @ dev-util/pkg-config
"""

opt_runtime = """
sndfile @ media-libs/libsndfile
"""

def configure():
    conf(
    "--disable-fftw",
        config_enable("sndfile"),
        "--disable-dependency-tracking")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("AUTHORS", "ChangeLog", "NEWS", "README")
