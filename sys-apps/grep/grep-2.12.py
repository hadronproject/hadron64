metadata = """
summary @ A string search utility
homepage @ http://www.gnu.org/software/grep/grep.html
license @ GPL-3
src_url @ ftp://ftp.gnu.org/gnu/$name/$fullname.tar.xz
options @ nls
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc dev-libs/pcre app-shells/bash
build @ sys-apps/texinfo
"""

def configure():
    conf("--bindir=/bin",
        "--without-included-regex",
        config_enable("nls"))

def install():
    raw_install('DESTDIR=%s' % install_dir)
    insdoc("AUTHORS", "ChangeLog", "NEWS", "README", "THANKS", "TODO")
