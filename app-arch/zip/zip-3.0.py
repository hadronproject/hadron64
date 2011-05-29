metadata = """
summary @ Creates PKZIP-compatible .zip files
homepage @ http://www.info-zip.org/pub/infozip/Zip.html
license @ Info-ZIP
src_url @ ftp://ftp.info-zip.org/pub/infozip/src/$name30.zip
arch @ ~x86
"""

standart_procedure = False

srcdir = "zip30"

def build():
    make("-f unix/Makefile LOCAL_ZIP='%s' prefix=/usr generic_gcc" % get_env("CFLAGS"))

def install():
    raw_install("-f unix/Makefile INSTALL=/bin/install prefix=%s/usr \
                 MANDIR=%s/usr/share/man/man1" % (install_dir, install_dir))

    insdoc("LICENSE")
