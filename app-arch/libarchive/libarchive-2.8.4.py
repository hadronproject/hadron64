metadata = """
summary @ Library that can create and read several streaming archive formats
homepage @ http://libarchive.googlecode.com/
license @ BSD
src_url @ http://libarchive.googlecode.com/files/libarchive-$version.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-libs/zlib app-arch/bzip2 app-arch/xz sys-apps/acl 
          dev-libs/openssl dev-libs/expat
"""

def configure():
    conf("--without-xml2")

def install():
    raw_install("DESTDIR=%s" % install_dir)

