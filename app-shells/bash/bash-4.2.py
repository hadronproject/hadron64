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

    conf(config_with("afs"),
        config_enable("mem-scramble"),
        config_with("mem-scramble", "bash-malloc"),
        config_enable("net", "net-redirections"),
        "--with-curses",
        "--disable-profiling",
        "--without-installed-readline",
        "--without-bash-malloc",
        myconf)

def install():
    if opt("plugins"):
        make("-C examples/loadables all others")
    
    # install bash
    raw_install("DESTDIR=%s install" % install_dir)
    
    # postinstall
    makedirs("/bin")
    move("%s/usr/bin/bash" % install_dir, "/bin/bash")
    makesym("/bin/bash", "/bin/sh")

    makedirs("/etc/skel")
    insfile(joinpath(filesdir, "system.bashrc"), "/etc/bash.bashrc")
    insfile(joinpath(filesdir, "system.bash_logout"), "/etc/bash.bash_logout")
    insfile(joinpath(filesdir, "dot.bashrc"), "/etc/skel/.bashrc")
    insfile(joinpath(filesdir, "dot.bash_profile"), "/etc/skel/.bash_profile")
    insfile(joinpath(filesdir, "dot.bash_logout"), "/etc/skel/.bash_logout")

    insdoc("README", "NEWS", "AUTHORS", "CHANGES", "COMPAT", "Y2K", "doc/FAQ", "doc/INTRO")
