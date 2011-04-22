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
    conf("--without-debug",
        "--without-profile",
        "--disable-rpath",
        "--enable-const",
        "--enable-largefile",
        "--enable-widec",
        "--with-terminfo-dirs='/etc/terminfo:/usr/share/terminfo'",
        "--disable-termcap",
        "--enable-hard-tabs",
        "--enable-xmc-glitch",
        "--enable-colorfgbg",
        "--with-shared",
        "--with-rcs-ids",
        "--with-chtype='long'",
        "--with-mmask-t='long'",
        "--without-ada",
        "--enable-symlinks")

def install():
    raw_install("DESTDIR=%s" % install_dir)
    
    for lib in ls("%s/usr/lib/*w.*" % install_dir):
        target = basename(lib).replace("w.", ".")
        makesym(basename(lib), joinpath("/usr/lib", target))
        
    terminfo = ["ansi", "console", "dumb", "linux", "rxvt", "screen", "sun", \
            "vt52", "vt100", "vt102", "vt200", "vt220", "xterm", "xterm-color", "xterm-xfree86"]
    
    for f in terminfo:
        termfile = f[0] + "/" + f
        if isexists("%s/usr/share/terminfo/%s" % (install_dir, termfile)):
            makedirs("/etc/terminfo/%s" % f[0])
            move("%s/usr/share/terminfo/%s" % (install_dir, termfile), "/etc/terminfo/%s" % f[0])
            makesym("/etc/terminfo/%s/%s" % (f[0], f), "/usr/share/terminfo/%s/%s" % (f[0], f))
