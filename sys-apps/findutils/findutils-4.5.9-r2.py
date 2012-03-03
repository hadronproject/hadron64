metadata = """
summary @ GNU utilities for finding files
homepage @ http://www.gnu.org/software/findutils/
license @ GPL-2
src_url @ ftp://alpha.gnu.org/gnu/findutils/findutils-4.5.9.tar.gz
arch @ ~x86
options @ locate
"""

depends = """
runtime @ sys-libs/glibc
"""

opt_postmerge = """
locate @ sys-apps/mlocate
"""

def configure():
    #don't build slocate, we like mlocate
    sed("""-i '/^SUBDIRS/s/locate//' Makefile.in""")

    append_cflags('-D_GNU_SOURCE')
    conf()

def install():
    installd()

def post_install():
    notify("If you want locate functionality, use the locate option which installs mlocate")
