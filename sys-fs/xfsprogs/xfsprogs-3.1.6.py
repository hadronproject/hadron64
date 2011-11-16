metadata = """
summary @ XFS filesystem utilities
homepage @ http://oss.sgi.com/projects/xfs/
license @ LGPL
src_url @ ftp://ftp.archlinux.org/other/xfsprogs/$fullname.tar.gz
arch @ ~x86
"""

depends = """
common @ sys-apps/util-linux
"""

standard_procedure = False

def build():
    export("OPTIMIZER", "-march=i686 -O1")
    export("DEBUG", "-DNDEBUG")
    make()

def install():
    raw_install("install install-dev DIST_ROOT=%s" % install_dir)
