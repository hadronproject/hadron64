metadata = """
summary @ Utility used to store, backup and transport files
homepage @ http://www.gnu.org/software/tar/tar.html
license @ GPL-3
src_url @ ftp://ftp.gnu.org/gnu/$name/$fullname.tar.bz2
options @ nls static
"""

def configure():
    export("FORCE_UNSAFE_CONFIGURE", "1")
    if opt("static"): append-ldflags("-static")
    conf("--bindir=/bin",
        config_enable('nls'))

def install():
    raw_install('DESTDIR=%s' % install_dir)
