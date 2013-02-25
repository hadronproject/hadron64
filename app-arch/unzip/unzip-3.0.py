metadata = """
summary @ Unpacks .zip archives such as those made by PKZIP
homepage @ http://www.info-zip.org/
license @ Info-ZIP
src_url @ http://downloads.sourceforge.net/infozip/unzip60.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ app-arch/bzip2 app-shells/bash
"""

#append_cflags("-D_FILE_OFFSET_BITS=64 -DACORN_FTYPE_NFS \
#        -DWILD_STOP_AT_DIR -DLARGE_FILE_SUPPORT -DUNICODE_SUPPORT \
#        -DUNICODE_WCHAR -DUTF8_MAYBE_NATIVE -DNO_LCHMOD -DDATE_FORMAT=DF_YMD \
#        -DUSE_BZIP2 -DNATIVE")

srcdir = "unzip60"

standard_procedure = False

def build():
    make('-f unix/Makefile LOCAL_UNZIP="%s" prefix=/usr LF2="" D_USE_BZ2=-DUSE_BZIP2 L_BZ2=-lbz2 unzips' % get_env("CFLAGS"))

def install():
    raw_install("-f unix/Makefile prefix=%s/usr INSTALL_PROGRAM='install'" % install_dir)

    insdoc("LICENSE")
