metadata = """
summary @ A network utility to retrieve files from the Web
homepage @ http://www.gnu.org/software/wget/wget.html
license @ GPL-3
src_url @ ftp://ftp.gnu.org/gnu/$name/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc
        dev-libs/openssl
"""

def prepare():
    patch(level=1)

def configure():
    conf("--with-ssl")

def install():
    raw_install("DESTDIR=%s install" % install_dir)
    insdoc("AUTHORS", "COPYING", "ChangeLog*", "NEWS", "README", "MAILING-LIST")

