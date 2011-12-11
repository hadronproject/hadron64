metadata = """
summary @ XML parsing library, version 2
homepage @ http://www.xmlsoft.org/
license @ custom
src_url @ ftp://ftp.xmlsoft.org/libxml2/$fullname.tar.gz
arch @ ~x86
options @ icu debug ipv6 readline
"""

depends = """
runtime @ sys-libs/glibc sys-libs/ncurses sys-libs/zlib
build @ dev-lang/perl[ithreads]
"""

opt_runtime = """
readline @ sys-apps/readline
icu @ dev-libs/icu
"""

def prepare():
    patch(level=1)

def configure():
    autoreconf("-fi")
    conf(
        "--with-threads",
        config_enable("ipv6"),
        "--with-python=/usr/bin/python2.7",
        config_with("readline"),
        config_with("readline", "history"),
        config_with("debug", "run-debug"),
        config_with("icu"))

def build():
    export("PYTHONDONTWRITEBYTECODE", "1")
    make()

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
