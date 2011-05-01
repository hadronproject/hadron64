metadata = """
summary @ GNU readline library
homepage @ http://tiswww.case.edu/php/chet/readline/rltop.html
license @ GPL
src_url @ http://ftp.gnu.org/gnu/readline/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-libs/ncurses
build @ sys-libs/ncurses
"""

def prepare():
    system("sed -i 's|-Wl,-rpath,$(libdir) ||g' support/shobj-conf")

def build():
    make("SHLIB_LIBS=-lncurses")

def install():
    raw_install("DESTDIR=%")

    insfile("%s/inputrc" % filesdir, "/etc/inputrc")

    makedirs("/usr/lib")

    #move("%s/lib/*.a" % install_dir, "%s/usr/lib/" % install_dir)

    cd("%s/usr/lib" % install_dir)

    makesym("/lib/readline.so", "readline.so")
    makesym("/lib/libhistory", "libhistory.so")

