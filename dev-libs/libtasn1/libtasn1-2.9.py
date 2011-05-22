metadata = """
summary @ The ASN.1 library used in GNUTLS
homepage @ http://www.gnu.org/software/libtasn1/
license @ GPL3 + LGPL
src_url @ ftp://ftp.gnu.org/gnu/libtasn1/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc sys-apps/texinfo
"""

#def configure():
#	conf(
#	'./configure --prefix=/usr \
#      --with-packager=Archlinux \
#      --with-packager-bug-reports="http://hadronproject.org/" \
#      --with-packager-version=$version')

def install():
	raw_install("DESTDIR=%s" % install_dir)

