metadata = """
summary @ framework for testing other programs
homepage @ http://www.gnu.org/software/dejagnu/
license @ GPL-2
src_url @ ftp://mirrors.kernel.org/gnu/dejagnu/dejagnu-1.4.4.tar.gz
options @ doc
"""

def prepare():
    patch("dejagnu-1.4.4-consolidated-1.patch", level=1)
