metadata = """
summary @ console display library
homepage @  http://www.gnu.org/software/ncurses/
license @ GPL-3
src_url @ http://ftp.gnu.org/pub/gnu/$name/$name-$version.tar.gz
options @ nls ada
"""

def configure():
    makedirs("ncurses-build"); cd("ncurses-build")
    conf("--with-shared",
        "--without-debug",
        "--without-profile",
        "--enable-const",
        "--enable-largefile",
        "--disable-termcap",
        "--with-rcs-ids",
        "--enable-symlinks",
        "--with-terminfo-dirs='/etc/terminfo:/usr/share/terminfo'"
        "--without-ada",
        "--enable-overwrite",
        run_dir=build_dir)

def build():
    cd("ncurses-build")
    make()

def install():
    cd("ncurses-build")
    raw_install("DESTDIR=%s" % install_dir)
