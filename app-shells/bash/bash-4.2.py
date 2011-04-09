metadata = """
summary @ The standard GNU Bourne again shell
homepage @ http://tiswww.case.edu/php/chet/bash/bashtop.html
license @ GPL-3
src_url @ http://ftp.gnu.org/gnu/$name/$fullname.tar.gz
options @ net nls afs mem-scramble plugins
arch @ ~x86
"""
depends = """
build @ sys-libs/ncurses 
runtime @ sys-libs/ncurses
"""

def configure():
    myconf = ""
    if not opt("nls"):
        myconf += " --disable-nls"

    conf("--without-bash-malloc")
    conf(config_with("afs"),
        config_enable("mem-scramble"),
        config_with("mem-scramble", "bash-malloc"),
        config_enable("net", "net-redirections"),
        "--with-curses",
        "--disable-profiling",
        "--without-installed-readline",
        "--without-lispdir",
        myconf)

def install():
    if opt("plugins"):
        make("-C examples/loadables all others")
    
    raw_install("DESTDIR=%s install" % install_dir)
    makedirs("/bin")
    move("%s/usr/bin/bash" % install_dir, "/bin/bash")
    insdoc("README", "NEWS", "AUTHORS", "CHANGES", "COMPAT", "Y2K", "doc/FAQ", "doc/INTRO")
