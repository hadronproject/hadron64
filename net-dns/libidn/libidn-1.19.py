metadata = """
summary @ Implementation of the Stringprep, Punycode and IDNA specifications
homepage @ http://www.gnu.org/software/libidn
license @ GPL-3 LGPL
src_url @ http://ftp.gnu.org/gnu/$name/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc sys-apps/texinfo
"""

def install():
    raw_install("DESTDIR=%s install" % install_dir)
