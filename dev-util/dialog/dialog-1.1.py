metadata = """
summary @ A tool to display dialog boxes from shell scripts
homepage @ http://invisible-island.net/dialog/
license @ LGPL2.1
src_url @ ftp://invisible-island.net/$name/$fullname-20110302.tgz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc sys-libs/ncurses
"""

srcdir = "%s-20110302" % fullname

def configure():
    conf(
    "--with-ncursesw --enable-nls")

def install():
    raw_install("DESTDIR=%s" % install_dir)

#hatali noluyu amq http://projects.archlinux.org/svntogit/packages.git/tree/dialog/trunk/PKGBUILD
#install bölümüne bi el atılacak ayrıca
