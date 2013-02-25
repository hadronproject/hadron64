metadata = """
summary @ Simple helper tools to manage Hadron
homepage @ http://hadronproject.org
license @ GPL-3
src_url @ http://hadronproject.org/distfiles/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-apps/lpms
"""

standard_procedure = False

def install():
    raw_install("DESTDIR=%s" % install_dir)
