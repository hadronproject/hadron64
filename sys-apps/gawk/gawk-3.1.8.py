metadata = """
summary @ GNU version of AWK
homepage @ http://www.gnu.org/directory/GNU/gawk.html
license @ GPL-2
src_url @ ftp://ftp.gnu.org/pub/gnu/$name/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc app-shells/bash
"""

def install():
    raw_install("DESTDIR=%s install" % install_dir)
    insdoc("AUTHORS", "ChangeLog", "FUTURES", "LIMITATIONS",
            "NEWS", "PROBLEMS", "POSIX.STD", "README", "README_d/*.*")
