metadata = """
summary @ GNU internationalization library
homepage @ http://www.gnu.org/software/gettext
license @ GPL-3
src_url @ ftp://ftp.gnu.org/pub/gnu/$name/$fullname.tar.gz
options @ nls git static-libs openmp emacs
arch @ ~x86
"""

depends = """
runtime @ sys-apps/acl sys-libs/glib
"""

#def prepare():
#    patch(level=1)

def configure():
    export("LC_ALL", "C")
    conf("--disable-java",
        "--enable-shared",
        "--disable-native-java",
        "--disable-csharp",
        "--without-included-gettext",
        "--with-included-libcroco",
        "--with-included-glib",
        "--with-included-libxml",
        "--with-pic=yes",
        "--disable-rpath",
        config_enable("git"),
        config_enable("openmp"),
        config_enable("static-libs", "static"),
        config_with("emacs"))

def build():
    make("CFLAGS='%s -U_FORTIFY_SOURCE'" % get_env("CFLAGS"))

def install():
    raw_install('DESTDIR=%s install' % install_dir)
