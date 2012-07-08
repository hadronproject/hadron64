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
    makedirs("ncursesw-build")
    cd("ncursesw-build")
    conf("--with-shared", 
            "--with-normal", 
            "--without-debug", 
            "--without-ada",
            "--with-install-prefix=%s" % install_dir,
            "--enable-widec", run_dir=build_dir)
    make()

    makedirs("../ncurses-build")
    cd("../ncurses-build")
    conf("--with-shared", 
            "--with-normal", 
            "--without-debug", 
            "--without-ada",
            "--with-install-prefix=%s" % install_dir,
            run_dir=build_dir)
    make()


def install():
    cd("ncursesw-build")
    raw_install()
    
    #makedirs("/lib64")
    #for item in glob.glob("%s/usr/lib/libncursesw.so.5*" % install_dir):
    #    move(item, "/lib64/"+basename(item))
    #rmfile("/usr/lib/libncursesw.so")
    #makesym("/lib64/libncursesw.so.5", "/usr/lib/libncursesw.so")
    
    for lib in ('ncurses', 'form', 'panel', 'menu'):
        if isexists("/usr/lib/lib"+lib+".so"):
            rmfile("/usr/lib/lib"+lib+".so")
        echo("INPUT(-l"+lib+"w)", "/usr/lib/lib"+lib+".so")
        makesym("lib"+lib+"w.a", "/usr/lib/lib"+lib+".a")

    makesym("libncurses++w.a", "/usr/lib/libncurses++.a")
    
    if isexists("/usr/lib/libcursesw.so"):
        rmfile("/usr/lib/libcursesw.so")
    echo("INPUT(-lncursesw)", "/usr/lib/libcursesw.so")
    makesym("libncurses.so", "/usr/lib/libcurses.so")
    makesym("libncursesw.a", "/usr/lib/libcursesw.a")
    makesym("libncurses.a", "/usr/lib/libcurses.a")
    
    cd("../ncurses-build")
    insfile("lib/libncurses.so.5.9", "/usr/lib/libncurses.so.5.9")
    makesym("libncurses.so.5.9", "/usr/lib/libncurses.so.5")
