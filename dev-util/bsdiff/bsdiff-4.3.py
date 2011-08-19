metadata = """
summary @ bsdiff and bspatch are tools for building and applying patches to binary files
homepage @ http://www.daemonology.net/bsdiff/
license @ BSD
src_url @ http://www.daemonology.net/$name/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc app-arch/bzip2
"""
standard_procedure = False

def install():
    system("gcc -o bsdiff bsdiff.c -lbz2")
    system("gcc -o bspatch bspatch.c -lbz2")
    insexe("bsdiff", "/usr/bin/")
    insexe("bspatch", "/usr/bin/")
