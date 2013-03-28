metadata = """
summary @ Utility used to store, backup and transport files
homepage @ http://www.gnu.org/software/tar/tar.html
license @ GPL-3
src_url @ ftp://ftp.gnu.org/gnu/$name/$fullname.tar.xz
options @ nls static
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc app-shells/bash
"""

def configure():
    export("FORCE_UNSAFE_CONFIGURE", "1")
    if opt("static"): append-ldflags("-static")
    # fix build failure with glibc-2.16
    system("sed -i -e '/gets is a/d' gnu/stdio.in.h")
    conf("--bindir=/bin",
        config_enable('nls'))

def install():
    raw_install('DESTDIR=%s' % install_dir)
