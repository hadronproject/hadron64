metadata = """
summary @ A widely used XML scheme for writing documentation and help
homepage @ http://www.oasis-open.org/docbook/
license @ MIT
src_url @ http://www.docbook.org/xml/4.5/docbook-xml-4.5.zip
arch @ ~x86
slot @ 4.5
"""

depends = """
runtime @ dev-libs/libxml2 app-text/build-docbook-catalog app-text/docbook-xml-dtd:4.2
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
    system("xmlcatalog --noout --create %s/etc/xml/docbook-xml" % install_dir)

    system('xmlcatalog --noout --add "public" \
    "-//OASIS//DTD DocBook XML V4.1.2//EN" \
    "http://www.oasis-open.org/docbook/xml/4.1.2/docbookx.dtd" \
    "%s/etc/xml/docbook-xml"' % install_dir)
    system('xmlcatalog --noout --add "public" \
    "-//OASIS//DTD DocBook XML CALS Table Model V4.1.2//EN" \
    "http://www.oasis-open.org/docbook/xml/4.1.2/calstblx.dtd" \
    "%s/etc/xml/docbook-xml"' % install_dir)
    system('xmlcatalog --noout --add "public" \
    "-//OASIS//DTD DocBook XML CALS Table Model V4.1.2//EN" \
    "http://www.oasis-open.org/docbook/xml/4.1.2/calstblx.dtd" \
    "%s/etc/xml/docbook-xml"' % install_dir)
    system('xmlcatalog --noout --add "public" \
    "-//OASIS//DTD XML Exchange Table Model 19990315//EN" \
    "http://www.oasis-open.org/docbook/xml/4.1.2/soextblx.dtd" \
    "%s/etc/xml/docbook-xml"' % install_dir)
    system('xmlcatalog --noout --add "public" \
    "-//OASIS//ELEMENTS DocBook XML Information Pool V4.1.2//EN" \
    "http://www.oasis-open.org/docbook/xml/4.1.2/dbpoolx.mod" \
    "%s/etc/xml/docbook-xml"' % install_dir)
    system('xmlcatalog --noout --add "public" \
    "-//OASIS//ELEMENTS DocBook XML Document Hierarchy V4.1.2//EN" \
    "http://www.oasis-open.org/docbook/xml/4.1.2/dbhierx.mod" \
    "%s/etc/xml/docbook-xml"' % install_dir)
    system('xmlcatalog --noout --add "public" \
    "-//OASIS//ENTITIES DocBook XML Additional General Entities V4.1.2//EN" \
    "http://www.oasis-open.org/docbook/xml/4.1.2/dbgenent.mod" \
    "%s/etc/xml/docbook-xml"' % install_dir)
    system('xmlcatalog --noout --add "public" \
    "-//OASIS//ENTITIES DocBook XML Notations V4.1.2//EN" \
    "http://www.oasis-open.org/docbook/xml/4.1.2/dbnotnx.mod" \
    "%s/etc/xml/docbook-xml"' % install_dir)
    system('xmlcatalog --noout --add "public" \
    "-//OASIS//ENTITIES DocBook XML Character Entities V4.1.2//EN" \
    "http://www.oasis-open.org/docbook/xml/4.1.2/dbcentx.mod" \
    "%s/etc/xml/docbook-xml"' % install_dir)
    system('xmlcatalog --noout --add "rewriteSystem" \
    "http://www.oasis-open.org/docbook/xml/4.1.2" \
    "file:///usr/share/xml/docbook/xml-dtd-4.1.2" \
    "%s/etc/xml/docbook-xml"' % install_dir)
    system('xmlcatalog --noout --add "rewriteURI" \
    "http://www.oasis-open.org/docbook/xml/4.1.2" \
    "file:///usr/share/xml/docbook/xml-dtd-4.1.2" \
    "%s/etc/xml/docbook-xml"' % install_dir)

  # V4.2
    system('xmlcatalog --noout --add "public" \
    "-//OASIS//DTD DocBook XML V4.2//EN" \
    "http://www.oasis-open.org/docbook/xml/4.2/docbookx.dtd" \
    "%s/etc/xml/docbook-xml"' % install_dir)
    system('xmlcatalog --noout --add "public" \
    "-//OASIS//DTD DocBook CALS Table Model V4.2//EN" \
    "http://www.oasis-open.org/docbook/xml/4.2/calstblx.dtd" \
    "%s/etc/xml/docbook-xml"' % install_dir)
    system('xmlcatalog --noout --add "public" \
    "-//OASIS//DTD XML Exchange Table Model 19990315//EN" \
    "http://www.oasis-open.org/docbook/xml/4.2/soextblx.dtd" \
    "%s/etc/xml/docbook-xml"' % install_dir)
    system('xmlcatalog --noout --add "public" \
    "-//OASIS//ELEMENTS DocBook Information Pool V4.2//EN" \
    "http://www.oasis-open.org/docbook/xml/4.2/dbpoolx.mod" \
    "%s/etc/xml/docbook-xml"' % install_dir)
    system('xmlcatalog --noout --add "public" \
    "-//OASIS//ELEMENTS DocBook Document Hierarchy V4.2//EN" \
    "http://www.oasis-open.org/docbook/xml/4.2/dbhierx.mod" \
    "%s/etc/xml/docbook-xml"' % install_dir)
    system('xmlcatalog --noout --add "public" \
    "-//OASIS//ENTITIES DocBook Additional General Entities V4.2//EN" \
    "http://www.oasis-open.org/docbook/xml/4.2/dbgenent.mod" \
    "%s/etc/xml/docbook-xml"' % install_dir)
    system('xmlcatalog --noout --add "public" \
    "-//OASIS//ENTITIES DocBook Notations V4.2//EN" \
    "http://www.oasis-open.org/docbook/xml/4.2/dbnotnx.mod" \
    "%s/etc/xml/docbook-xml"' % install_dir)
    system('xmlcatalog --noout --add "public" \
    "-//OASIS//ENTITIES DocBook Character Entities V4.2//EN" \
    "http://www.oasis-open.org/docbook/xml/4.2/dbcentx.mod" \
    "%s/etc/xml/docbook-xml"' % install_dir)
    system('xmlcatalog --noout --add "rewriteSystem" \
    "http://www.oasis-open.org/docbook/xml/4.2" \
    "file:///usr/share/xml/docbook/xml-dtd-4.2" \
    "%s/etc/xml/docbook-xml"' % install_dir)
    system('xmlcatalog --noout --add "rewriteURI" \
    "http://www.oasis-open.org/docbook/xml/4.2" \
    "file:///usr/share/xml/docbook/xml-dtd-4.2" \
    "%s/etc/xml/docbook-xml"' % install_dir)

  # V4.3
    system('xmlcatalog --noout --add "public" \
    "-//OASIS//DTD DocBook XML V4.3//EN" \
    "http://www.oasis-open.org/docbook/xml/4.3/docbookx.dtd" \
    "%s/etc/xml/docbook-xml"' % install_dir)
    system('xmlcatalog --noout --add "public" \
    "-//OASIS//DTD DocBook CALS Table Model V4.3//EN" \
    "http://www.oasis-open.org/docbook/xml/4.3/calstblx.dtd" \
    "%s/etc/xml/docbook-xml"' % install_dir)
    system('xmlcatalog --noout --add "public" \
    "-//OASIS//DTD XML Exchange Table Model 19990315//EN" \
    "http://www.oasis-open.org/docbook/xml/4.3/soextblx.dtd" \
    "%s/etc/xml/docbook-xml"' % install_dir)
    system('xmlcatalog --noout --add "public" \
    "-//OASIS//ELEMENTS DocBook Information Pool V4.3//EN" \
    "http://www.oasis-open.org/docbook/xml/4.3/dbpoolx.mod" \
    "%s/etc/xml/docbook-xml"' % install_dir)
    system('xmlcatalog --noout --add "public" \
    "-//OASIS//ELEMENTS DocBook Document Hierarchy V4.3//EN" \
    "http://www.oasis-open.org/docbook/xml/4.3/dbhierx.mod" \
    "%s/etc/xml/docbook-xml"' % install_dir)
    system('xmlcatalog --noout --add "public" \
    "-//OASIS//ENTITIES DocBook Additional General Entities V4.3//EN" \
    "http://www.oasis-open.org/docbook/xml/4.3/dbgenent.mod" \
    "%s/etc/xml/docbook-xml"' % install_dir)
    system('xmlcatalog --noout --add "public" \
    "-//OASIS//ENTITIES DocBook Notations V4.3//EN" \
    "http://www.oasis-open.org/docbook/xml/4.3/dbnotnx.mod" \
    "%s/etc/xml/docbook-xml"' % install_dir)
    system('xmlcatalog --noout --add "public" \
    "-//OASIS//ENTITIES DocBook Character Entities V4.3//EN" \
    "http://www.oasis-open.org/docbook/xml/4.3/dbcentx.mod" \
    "%s/etc/xml/docbook-xml"' % install_dir)
    system('xmlcatalog --noout --add "rewriteSystem" \
    "http://www.oasis-open.org/docbook/xml/4.3" \
    "file:///usr/share/xml/docbook/xml-dtd-4.3" \
    "%s/etc/xml/docbook-xml"' % install_dir)
    system('xmlcatalog --noout --add "rewriteURI" \
    "http://www.oasis-open.org/docbook/xml/4.3" \
    "file:///usr/share/xml/docbook/xml-dtd-4.3" \
    "%s/etc/xml/docbook-xml"' % install_dir)

  # V4.4
    system('xmlcatalog --noout --add "public" \
    "-//OASIS//DTD DocBook XML V4.4//EN" \
    "http://www.oasis-open.org/docbook/xml/4.4/docbookx.dtd" \
    "%s/etc/xml/docbook-xml"' % install_dir)
    system('xmlcatalog --noout --add "public" \
    "-//OASIS//DTD DocBook CALS Table Model V4.4//EN" \
    "http://www.oasis-open.org/docbook/xml/4.4/calstblx.dtd" \
    "%s/etc/xml/docbook-xml"' % install_dir)
    system('xmlcatalog --noout --add "public" \
    "-//OASIS//ELEMENTS DocBook XML HTML Tables V4.4//EN" \
    "http://www.oasis-open.org/docbook/xml/4.4/htmltblx.mod" \
    "%s/etc/xml/docbook-xml"' % install_dir)
    system('xmlcatalog --noout --add "public" \
    "-//OASIS//DTD XML Exchange Table Model 19990315//EN" \
    "http://www.oasis-open.org/docbook/xml/4.4/soextblx.dtd" \
    "%s/etc/xml/docbook-xml"' % install_dir)
    system('xmlcatalog --noout --add "public" \
    "-//OASIS//ELEMENTS DocBook Information Pool V4.4//EN" \
    "http://www.oasis-open.org/docbook/xml/4.4/dbpoolx.mod" \
    "%s/etc/xml/docbook-xml"' % install_dir)
    system('xmlcatalog --noout --add "public" \
    "-//OASIS//ELEMENTS DocBook Document Hierarchy V4.4//EN" \
    "http://www.oasis-open.org/docbook/xml/4.4/dbhierx.mod" \
    "%s/etc/xml/docbook-xml"' % install_dir)
    system('xmlcatalog --noout --add "public" \
    "-//OASIS//ENTITIES DocBook Additional General Entities V4.4//EN" \
    "http://www.oasis-open.org/docbook/xml/4.4/dbgenent.mod" \
    "%s/etc/xml/docbook-xml"' % install_dir)
    system('xmlcatalog --noout --add "public" \
    "-//OASIS//ENTITIES DocBook Notations V4.4//EN" \
    "http://www.oasis-open.org/docbook/xml/4.4/dbnotnx.mod" \
    "%s/etc/xml/docbook-xml"' % install_dir)
    system('xmlcatalog --noout --add "public" \
    "-//OASIS//ENTITIES DocBook Character Entities V4.4//EN" \
    "http://www.oasis-open.org/docbook/xml/4.4/dbcentx.mod" \
    "%s/etc/xml/docbook-xml"' % install_dir)
    system('xmlcatalog --noout --add "rewriteSystem" \
    "http://www.oasis-open.org/docbook/xml/4.4" \
    "file:///usr/share/xml/docbook/xml-dtd-4.4" \
    "%s/etc/xml/docbook-xml"' % install_dir)
    system('xmlcatalog --noout --add "rewriteURI" \
    "http://www.oasis-open.org/docbook/xml/4.4" \
    "file:///usr/share/xml/docbook/xml-dtd-4.4" \
    "%s/etc/xml/docbook-xml"' % install_dir)

  # V4.5
    system('xmlcatalog --noout --add "public" \
    "-//OASIS//DTD DocBook XML V4.5//EN" \
    "http://www.oasis-open.org/docbook/xml/4.5/docbookx.dtd" \
    "%s/etc/xml/docbook-xml"' % install_dir)
    system('xmlcatalog --noout --add "public" \
    "-//OASIS//DTD DocBook XML CALS Table Model V4.5//EN" \
    "file:///usr/share/xml/docbook/xml-dtd-4.5/calstblx.dtd" \
    "%s/etc/xml/docbook-xml"' % install_dir)
    system('xmlcatalog --noout --add "public" \
    "-//OASIS//DTD XML Exchange Table Model 19990315//EN" \
    "file:///usr/share/xml/docbook/xml-dtd-4.5/soextblx.dtd" \
    "%s/etc/xml/docbook-xml"' % install_dir)
    system('xmlcatalog --noout --add "public" \
    "-//OASIS//ELEMENTS DocBook XML Information Pool V4.5//EN" \
    "file:///usr/share/xml/docbook/xml-dtd-4.5/dbpoolx.mod" \
    "%s/etc/xml/docbook-xml"' % install_dir)
    system('xmlcatalog --noout --add "public" \
    "-//OASIS//ELEMENTS DocBook XML Document Hierarchy V4.5//EN" \
    "file:///usr/share/xml/docbook/xml-dtd-4.5/dbhierx.mod" \
    "%s/etc/xml/docbook-xml"' % install_dir)
    system('xmlcatalog --noout --add "public" \
    "-//OASIS//ELEMENTS DocBook XML HTML Tables V4.5//EN" \
    "file:///usr/share/xml/docbook/xml-dtd-4.5/htmltblx.mod" \
    "%s/etc/xml/docbook-xml"' % install_dir)
    system('xmlcatalog --noout --add "public" \
    "-//OASIS//ENTITIES DocBook XML Notations V4.5//EN" \
    "file:///usr/share/xml/docbook/xml-dtd-4.5/dbnotnx.mod" \
    "%s/etc/xml/docbook-xml"' % install_dir)
    system('xmlcatalog --noout --add "public" \
    "-//OASIS//ENTITIES DocBook XML Character Entities V4.5//EN" \
    "file:///usr/share/xml/docbook/xml-dtd-4.5/dbcentx.mod" \
    "%s/etc/xml/docbook-xml"' % install_dir)
    system('xmlcatalog --noout --add "public" \
    "-//OASIS//ENTITIES DocBook XML Additional General Entities V4.5//EN" \
    "file:///usr/share/xml/docbook/xml-dtd-4.5/dbgenent.mod" \
    "%s/etc/xml/docbook-xml"' % install_dir)
    system('xmlcatalog --noout --add "rewriteSystem" \
    "http://www.oasis-open.org/docbook/xml/4.5" \
    "file:///usr/share/xml/docbook/xml-dtd-4.5" \
    "%s/etc/xml/docbook-xml"' % install_dir)
    system('xmlcatalog --noout --add "rewriteURI" \
    "http://www.oasis-open.org/docbook/xml/4.5" \
    "file:///usr/share/xml/docbook/xml-dtd-4.5" \
    "%s/etc/xml/docbook-xml"' % install_dir)


def post_install():
    system("/usr/bin/build-docbook-catalog")

    #system('/usr/bin/install-catalog --add /etc/sgml/xml-docbook-4.5.cat \
    #        /etc/sgml/sgml-docbook.cat')

    #system('/usr/bin/install-catalog --add /etc/sgml/xml-docbook-4.5.cat \
    #        /usr/share/sgml/docbook/xml-dtd-4.5/docbook.cat')
