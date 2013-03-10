metadata ="""
summary @ Text document format for short documents, articles, books and UNIX man pages.
homepage @ http://www.methods.co.nz/asciidoc/
license @ GPL
src_url @ http://downloads.sourceforge.net/$name/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
build @ dev-lang/python:2.7 dev-libs/libxslt app-text/docbook-xsl-stylesheets
"""

def install():
    installd()
    copy("asciidocapi.py", "/usr/lib/python2.7/site-packages/asciidocapi.py")
