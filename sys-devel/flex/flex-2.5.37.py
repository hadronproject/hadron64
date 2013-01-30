metadata = """
summary @ A tool for generating text-scanning programs
homepage @ http://flex.sourceforge.net
license @ FLEX
src_url @ http://downloads.sourceforge.net/sourceforge/flex/flex-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc sys-devel/m4
"""

def install():
    installd()
    insfile(joinpath(filesdir, "lex.sh"), "/usr/bin/lex")
