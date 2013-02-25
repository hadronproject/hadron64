metadata = """
summary @ PolyGlotMan man page translator AKA RosettaMan
homepage @ http://sourceforge.net/projects/polyglotman/
license @ Artistic
src_url @ http://downloads.sourceforge.net/project/polyglotman/polyglotman/3.2/rman-3.2.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc
"""

standard_procedure = False

def build():
    make()

def install():
    insexe(name, "/usr/bin/%s" % name)
