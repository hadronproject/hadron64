metadata = """
summary @ GNU stream editor
homepage @ http://www.gnu.org/software/sed
license @ GPL-3
src_url @ ftp://ftp.gnu.org/pub/gnu/$name/$fullname.tar.gz
options @ acl nls
arch @ ~x86_64
"""
depends = """
runtime @ sys-apps/acl app-shells/bash
"""

def configure():
    conf("--bindir=/bin",
        config_enable('acl'),
        config_enable('nls'))

def install():
    raw_install('DESTDIR=%s' % install_dir)
