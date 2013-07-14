metadata = """
summary @ Utility programs used for creating patch files
homepage @ http://www.gnu.org/software/diffutils
license @ GPL-3
src_url @ ftp://ftp.gnu.org/gnu/$name/$fullname.tar.gz
options @ nls static-libs
arch @ ~x86_64
"""

depends = """
common @ sys-libs/glibc app-shells/bash
"""

def configure():
    # fix glibc-2.16 build issue
    system("sed -i -e '/gets is a/d' lib/stdio.in.h")
    if opt('static-libs'): append_ldflags('-static')
    conf("--with-packager='Hadron'",
        config_enable("nls"))

def install():
    raw_install('DESTDIR=%s' % install_dir)
    insdoc("AUTHORS", "ChangeLog", "NEWS", "README", "THANKS", "TODO")
