metadata = """
summary @ Free Lossless Audio Codec
homepage @ http://flac.sourceforge.net/
license @ Xiph + LGPL + GPL + FDL
src_url @ http://downloads.sf.net/sourceforge/$name/$fullname.tar.gz
arch @ ~x86
options @ 3dnow altivec cxx debug ogg sse static-libs
"""

depends = """
build @ dev-lang/yasm sys-devel/gettext dev-util/pkg-config
"""

opt_runtime = """
ogg @ media-libs/libogg
"""

def prepare():
    patch(level=1)

def configure():
    conf(
    "--enable-shared",
    "--with-pic",
    "--disable-doxygen-docs",
        "--disable-xmms-plugin ",
        "--disable-dependency-tracking",
        config_enable("static-libs", "static"),
        config_enable("debug"),
        config_enable("sse"),
        config_enable("3dnow"),
        config_enable("altivec"),
        config_enable("cxx", "cpplibs"),
        config_enable("ogg"))

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("AUTHORS", "README")
