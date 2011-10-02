metadata = """
summary @ A high-quality data compressor
homepage @ http://www.bzip2.org
license @ BZIP2
src_url @ http://bzip.org/$version/$fullname.tar.gz
arch @ ~x86
"""
depends = """runtime @ sys-libs/glibc"""

standard_procedure = False

def build():
    make('CC=%s AR=%s RANLIB=%s CFLAGS="%s -D_FILE_OFFSET_BITS=64 -fPIC"' % (binutils_cmd("gcc"), binutils_cmd('ar'), binutils_cmd('ranlib'), get_env('CFLAGS')))
    make('CFLAGS="%s -D_FILE_OFFSET_BITS=64 -fPIC" -f Makefile-libbz2_so' % get_env('CFLAGS'))

def install():
    raw_install('PREFIX=%s/usr' % install_dir)
    insfile("libbz2.so.1.0.6", "/lib/libbz2.so.1.0.6")
    makesym("/lib/libbz2.so.1.0.6", "/lib/libbz2.so")
    makesym("/lib/libbz2.so.1.0.6", "/lib/libbz2.so.1")
    makesym("/lib/libbz2.so.1.0.6", "/lib/libbz2.so.1.0")
    insdoc("README", "CHANGES", "bzip2.txt")
