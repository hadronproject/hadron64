metadata = """
summary @ Base ISO character entities and utilities for SGML
homepage @ http://www.linuxfromscratch.org/blfs/view/svn/pst/sgml-common.html
license @ GPL-2
src_url @ ftp://sources.redhat.com/pub/docbook-tools/new-trials/SOURCES/$fullname.tgz
arch @ ~x86_64
"""

def prepare():
    patch(level=1)
    autoreconf("-fi")

def install():
    raw_install("DESTDIR=%s" % install_dir)

def post_install():
    if not system("/usr/bin/install-catalog --add /etc/sgml/sgml-ent.cat \
            /usr/share/sgml/sgml-iso-entities-8879.1986/catalog"):
        error("install catalog command has failed.")
    if not system("/usr/bin/install-catalog --add /etc/sgml/sgml-docbook.cat \
            /etc/sgml/sgml-ent.cat"):
        error("install catalog command has failed.")

# TODO: how to run post_remove while removing this package?
