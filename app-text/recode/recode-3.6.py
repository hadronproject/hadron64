metadata ="""
summary @ File character set converter
homepage @ http://recode.progiciels-bpi.ca/index.html
license @ GPL-2
src_url @ http://sourceforge.net/projects/hadron-sources/files/recode-3.6.tar.gz
options @ nls static-libs
arch @ ~x86
"""

depends = """
build @ sys-devel/flex
"""

opt_build = """
nls @ sys-devel/gettext
"""

def prepare():
    patch("recode-3.6-gettextfix.diff",level=1)
    patch("recode-3.6-as-if.patch",level=1)
    patch("recode_3.6-15.diff",level=1)
    system("sed -i '1i#include <stdlib.h>' src/argmatch.c")
    rmfile("acinclude.m4")
    autoreconf("-fi")
    libtoolize()

def configure():
    raw_configure("--prefix=/usr",
            "--without-included-gettext",
            "--mandir=/usr/share/man",
            "--infodir=/usr/share/info",
            config_enable("static-libs","static"),
            config_enable("nls"))

def install():
    raw_install("DESTDIR=%s install" % install_dir)
    insdoc("AUTHORS", "BACKLOG", "ChangeLog", "NEWS", "README", "THANKS", "TODO")
