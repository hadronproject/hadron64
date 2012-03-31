metadata = """
summary @ The standard GNU Bourne again shell
homepage @ http://tiswww.case.edu/php/chet/bash/bashtop.html
license @ GPL-3
src_url @ http://ftp.gnu.org/gnu/$name/$fullname.tar.gz
options @ net nls afs mem-scramble plugins
arch @ ~x86
"""

depends = """
common @ sys-libs/ncurses
build @ sys-libs/readline
"""

# from Pardus GNU/Linux
# BEGIN
cfgsettings = """-DDEFAULT_PATH_VALUE=\'\"/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\"\' \
                 -DSTANDARD_UTILS_PATH=\'\"/bin:/usr/bin:/sbin:/usr/sbin\"\' \
                 -DSYS_BASHRC=\'\"/etc/bash/bashrc\"\' \
                 -DSYS_BASH_LOGOUT=\'\"/etc/bash/bash_logout\"\' \
                 -DNON_INTERACTIVE_LOGIN_SHELLS \
                 -DSSH_SOURCE_BASHRC"""

# END

def prepare():
    for i in xrange(1, 25):
        fetch("http://ftp.gnu.org/gnu/bash/bash-4.2-patches/bash42-%03d" % i, location=build_dir)

    for f in xrange(1, 25):
        patch("bash42-%03d" % f, location=build_dir)

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
        myconf)

def build():
    append_cflags("-D_GNU_SOURCE -DRECYCLES_PIDS %s" % cfgsettings)
    make()

def install():
    if opt("plugins"):
        make("-C examples/loadables all others")

    raw_install("DESTDIR=%s install" % install_dir)

    makedirs("/bin")
    move("%s/usr/bin/bash" % install_dir, "/bin/bash")
    makesym("/bin/bash", "/bin/sh")

    makedirs("/etc/skel")
    insexe(joinpath(filesdir, "bashrc"), "/etc/bash/bashrc")
    insfile(joinpath(filesdir, "bash_logout"), "/etc/bash/bash_logout")
    insfile(joinpath(filesdir, "dot-bashrc"), "/etc/skel/.bashrc")
    insfile(joinpath(filesdir, "dot-bash_profile"), "/etc/skel/.bash_profile")
    insfile(joinpath(filesdir, "dot-bash_logout"), "/etc/skel/.bash_logout")

    insdoc("README", "NEWS", "AUTHORS", "CHANGES", "COMPAT", "Y2K", "doc/FAQ", "doc/INTRO")
