metadata = """
summary @ A widely used XML scheme for writing documentation and help
homepage @ http://www.oasis-open.org/docbook/
license @ MIT
src_url @ http://www.docbook.org/xml/$version/docbook-xml-$version.zip
arch @ ~x86_64
slot @ 4.4
"""

depends = """
runtime @ dev-libs/libxml2 app-text/build-docbook-catalog
build @ app-text/sgml-common
"""

srcdir = ""

standard_procedure = False

def install():
    insinto("*.dtd", "/usr/share/xml/docbook/xml-dtd-%s" % version)
    insinto("*.mod", "/usr/share/xml/docbook/xml-dtd-%s" % version)
    insinto("docbook.cat", "/usr/share/xml/docbook/xml-dtd-%s" % version)
    insinto("ent/*.ent", "/usr/share/xml/docbook/xml-dtd-%s/ent" % version)
    makedirs("/etc/xml")

def post_install():
    system("/usr/bin/build-docbook-catalog")

