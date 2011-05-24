metadata = """
summary @ Base ISO character entities and utilities for SGML
homepage @ http://www.linuxfromscratch.org/blfs/view/svn/pst/sgml-common.html
license @ GPL-2
src_url @ http://gd.tuwien.ac.at/hci/kde/devel/docbook/SOURCES/sgml-common-0.6.3.tgz
arch @ ~x86
"""

standart_procedure = False

def prepare():
    patch(level=1)

def configure():
    autoreconf("-fi")
    conf()

def install():
    raw_install("DESTDIR=%s" % install_dir)

def post_install():
    system("/usr/bin/install-catalog --add /etc/sgml/sgml-ent.cat /usr/share/sgml/sgml-iso-entities-8879.1986/catalog")
            
    system("/usr/bin/install-catalog --add /etc/sgml/sgml-docbook.cat /etc/sgml/sgml-ent.cat")
