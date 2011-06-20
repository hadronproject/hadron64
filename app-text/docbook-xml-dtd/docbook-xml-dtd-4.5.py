metadata = """
summary @ A widely used XML scheme for writing documentation and help
homepage @ http://www.oasis-open.org/docbook/
license @ MIT
src_url @ http://www.docbook.org/xml/4.5/docbook-xml-4.5.zip
arch @ ~x86
slot @ 4.5
"""

depends = """
runtime @ dev-libs/libxml2
"""

srcdir = ""

standart_procedure = False

def install():
    insinto("*.dtd", "/usr/share/sgml/docbook/xml-dtd-%s" % version)
    insinto("*.mod", "/usr/share/sgml/docbook/xml-dtd-%s" % version)
    insinto("docbook.cat", "/usr/share/sgml/docbook/xml-dtd-%s" % version)
    insinto("ent/*.ent", "/usr/share/sgml/docbook/xml-dtd-%s/ent" % version)

def post_install():
    system("/usr/bin/build-docbook-catalog")
    
    system('/usr/bin/install-catalog --add /etc/sgml/xml-docbook-4.5.cat \
            /etc/sgml/sgml-docbook.cat')
    
    system('/usr/bin/install-catalog --add /etc/sgml/xml-docbook-4.5.cat \
            /usr/share/sgml/docbook/xml-dtd-4.5/docbook.cat')
