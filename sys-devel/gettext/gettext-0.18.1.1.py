metadata = """
summary @ GNU internationalization library
homepage @ http://www.gnu.org/software/gettext
license @ GPL-3
src_url @ ftp://ftp.gnu.org/pub/gnu/$name/$fullname.tar.gz
options @ nls git static-libs openmp emacs
arch @ ~x86_64
"""

# FIXME: Check options and depends

depends = """
runtime @ sys-apps/acl
        sys-libs/ncurses
        sys-devel/gcc
"""

def configure():
    # fix build issue with glibc-2.16
    system("sed -i -e '/gets is a/d' gettext-*/*/stdio.in.h")

    conf(
        "--disable-java",
        "--enable-shared",
        "--disable-native-java",
        "--disable-csharp",
        "--without-included-gettext",
        "--with-included-libcroco",
        "--with-included-glib",
        "--with-included-libxml",
        "--with-pic=yes",
        config_enable("nls"),
        config_enable("git"),
        config_enable("openmp"),
        config_enable("static-libs", "static"),
        config_with("emacs"))

def install():
    raw_install('DESTDIR=%s install' % install_dir)
