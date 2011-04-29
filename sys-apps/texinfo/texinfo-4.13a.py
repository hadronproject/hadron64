metadata = """
summary @ The GNU info program and utilities
homepage @ http://www.gnu.org/software/texinfo/
license @ GPL-3
src_url @ ftp://ftp.gnu.org/pub/gnu/$name/$fullname.tar.gz
options @ nls static
"""

depends = """
runtime @ sys-libs/ncurses sys-apps/findutils 
          app-arch/gzip
"""

srcdir = name+"-"+version[:-1]

def configure():
    if opt("static"): append-ldflags("-static")
    conf(config_enable("nls"))

def install():
    raw_install('DESTDIR=%s' % install_dir)
