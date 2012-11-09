metadata = """
summary @ System V Release 4.0 curses emulation library
homepage @  http://www.gnu.org/software/ncurses/
license @ MIT
src_url @ http://ftp.gnu.org/pub/gnu/$name/$name-$version.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc
"""
standard_procedure = False

# debug option is going to be added.

def build():
    conf("--with-shared", 
            "--with-normal", 
            "--without-debug", 
            "--without-ada",
            "--with-install-prefix=%s" % install_dir,
            "--enable-widec",
            "--with-chtype=long")
    make()

def install():
    raw_install()
