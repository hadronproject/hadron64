metadata = """
summary @ XML stylesheets for Docbook-xml transformations.
homepage @ http://docbook.sourceforge.net/
license @ custom
src_url @ http://downloads.sourceforge.net/sourceforge/docbook/docbook-xsl-$version.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ dev-libs/libxml2 dev-libs/libxslt app-text/docbook-xml-dtd
"""

srcdir = "docbook-xsl-"+version

standart_procedure = False

def install():
    raw_install("DESTDIR=%s/usr/share/sgml/docbook/xsl-stylesheets" % install_dir)

    insdoc("AUTHORS", "BUGS", "COPYING", "NEWS", "README", 
            "RELEASE-NOTES.txt", "TODO", "VERSION")
