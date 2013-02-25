metadata = """
summary @ A free codec for free speech
homepage @ http://www.speex.org/
license @ BSD
src_url @ http://downloads.us.xiph.org/releases/$name/$fullnamerc1.tar.gz
arch @ ~x86_64
options @ ogg sse static-libs
"""

opt_runtime = """
ogg @ media-libs/libogg
"""

opt_build = """
ogg @ media-libs/libogg
"""

srcdir = fullname+"rc1"

def prepare():
    patch("configure.patch",level=1)
    patch("constant.patch",level=1)
    system("sed -i 's:noinst_PROGRAMS:check_PROGRAMS:' \
        libspeex/Makefile.am")
    libtoolize()
    autoreconf()

def configure():
    raw_configure("--prefix=/usr",
                "--sysconfdir=/etc",
                "--localstatedir=/var",
                "--disable-dependency-tracking",
                config_enable("ogg"),
                config_enable("sse"),
                config_enable("static_libs", "static"))
    system("sed -i 's:^hardcode_libdir_flag_spec=.*:hardcode_libdir_flag_spec=\"\":' libtool")
    system("sed -i 's:^runpath_var=LD_RUN_PATH:runpath_var=DIE_RPATH_DIE:' libtool")

def install():
    raw_install("DESTDIR=%s docdir=/usr/share/doc/speex" % install_dir)
    insdoc("AUTHORS","ChangeLog","NEWS","COPYING","README*","TODO")
