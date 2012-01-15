metadata = """
summary @ A tool for generating text-scanning programs
homepage @ http://flex.sourceforge.net
license @ FLEX
src_url @ http://downloads.sourceforge.net/sourceforge/flex/flex-$version.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc sys-devel/m4
"""

def prepare():
    patch(level=1)

def install():
    linstall()
    insfile(joinpath(filesdir, "lex.sh"), "/usr/bin/lex")
