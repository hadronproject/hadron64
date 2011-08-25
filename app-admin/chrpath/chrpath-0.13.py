metadata = """
summary @ Change or delete the rpath or runpath in ELF files
homepage @ http://packages.debian.org/chrpath
license @ GPL2
src_url @ http://ftp.debian.org/debian/pool/main/c/$name/$name_$version.orig.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("ChangeLog", "AUTHORS", "NEWS", "README")
