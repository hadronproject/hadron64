metadata = """
summary @ System V Release 4.0 curses emulation library
homepage @  http://www.gnu.org/software/ncurses/
license @ MIT
src_url @ http://ftp.gnu.org/pub/gnu/$name/$name-$version.tar.gz
options @ terminfo trace cxx debug profile
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc
"""


def configure():
    conf("--with-shared",
            "--with-terminfo-dirs='/etc/terminfo:/usr/share/terminfo'",
            "--without-hashed-db",
            "--disable-termcap",
            "--enable-symlinks",
            "--with-rcs-ids",
            "--with-manpage-format=normal",
            "--enable-const",
            "--enable-colorfgbg",
            "--enable-echo",
            "--enable-pc-files",
            "--with-normal",
            config_with("profile"),
            config_with("terminfo"),
            config_with("trace"),
            config_with("cxx"),
            config_with("cxx-binding"),
            config_with("debug"),
            config_with("debug", "expanded"),
            config_with("debug", "assertions"),
            config_enable("debug", "leaks"),
            "--without-ada",
            "--with-install-prefix=%s" % install_dir,
            "--enable-widec",
            "--with-chtype=long",
            "--with-mmask-t=long",
            "--disable-ext-colors",
            "--disable-ext-mouse",
            "--without-pthread",
            "--without-reentrant")

install = lambda: installd()
