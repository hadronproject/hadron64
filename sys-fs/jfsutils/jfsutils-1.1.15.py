metadata = """
summary @ JFS filesystem utilities
homepage @ http://jfs.sourceforge.net/
license @ GPL
src_url @ http://jfs.sourceforge.net/project/pub/$fullname.tar.gz
arch @ ~x86
"""

depends = """
common @ sys-apps/util-linux
"""

def configure():
    conf("--sbindir=/sbin")

def install():
    installd()
