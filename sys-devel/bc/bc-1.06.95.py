metadata = """
summary @ Handy console-based calculator utility
homepage @ http://www.gnu.org/software/bc/bc.html
license @ GPL-2 LGPL-2.1
src_url @ ftp://alpha.gnu.org/gnu/bc/$fullname.tar.bz2
arch @ ~x86_64
options @ libedit readline static
"""

depends = """
build @ sys-devel/flex
"""

opt_runtime = """
readline @ >=sys-libs/readline-4.1 >=sys-libs/ncurses-5.2
libedit @ dev-libs/libedit
"""

def configure():
    if opt("readline"):
        myconf = "--with-readline --without-libedit"
    elif opt("libedit"):
        myconf = "--without-readline --with-libedit"
    else:
        myconf = "--without-readline --without-libedit"

    if opt("static"): append_ldflags("-static")

    conf(myconf)

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("AUTHORS", "FAQ", "NEWS", "README", "ChangeLog")
