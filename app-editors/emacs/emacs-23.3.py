metadata = """
summary @ The extensible, customizable, self-documenting real-time display editor
homepage @ http://www.gnu.org/software/emacs/emacs.html
license @ GPL-3
src_url @ ftp://ftp.gnu.org/gnu/emacs/emacs-23.3b.tar.gz
arch @ ~x86
"""

# options will be added. gtk+, X and etc...

depends = """
common @ sys-libs/ncurses
"""

srcdir = "emacs-23.3"

def configure():
    conf("--without-x --without-ns")

def install():
    installd()
    move("%s/usr/bin/ctags" % install_dir, "/usr/bin/ctags.emacs")
    move("%s/usr/share/man/man1/ctags.1" % install_dir, "/usr/share/man/man1/ctags.emacs.1")
    setmod("775 %s/var/games" % install_dir)
    setmod("775 %s/var/games/emacs" % install_dir)
    setmod("664 %s/var/games/emacs/*" % install_dir)
    setowner("-R root:games %s/var/games" % install_dir)
