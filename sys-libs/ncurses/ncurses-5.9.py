metadata = """
summary @ System V Release 4.0 curses emulation library
homepage @  http://www.gnu.org/software/ncurses/
license @ MIT
src_url @ http://ftp.gnu.org/pub/gnu/$name/$name-$version.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc
"""

def configure():
    makedirs("../ncursesw-build"); cd("../ncursesw-build")
    conf("--with-shared",
        "--without-debug",
        "--with-normal",
        "--without-ada",
        "--with-install-prefix=%s" % install_dir,
        "--enable-widec",
        run_dir=build_dir)

    makedirs("../ncurses-build"); cd("../ncurses-build")
    conf("--with-shared",
        "--with-normal",
        "--without-debug",
        "--without-ada",
        "--with-install-prefix=%s" % install_dir,
        run_dir=build_dir)

def build():
    cd("ncursesw-build")
    make()
    
    cd("ncurses-build")
    make()

def install():
    cd("ncursesw-build")
    linstall()

    makedirs("/lib")
    move("%s/usr/lib/libncursesw.so.5*" % install_dir, "/lib")
    makesym("./../lib/libncursesw.so.5", "/usr/lib/libncursesw.so")

    #raw_install("DESTDIR=%s" % install_dir)
    insdoc("../AUTHORS", "../ANNOUNCE", "../NEWS", "../README*", "../TO-DO")
