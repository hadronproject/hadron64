metadata = """
summary @ Documentation tool for public library API
homepage @ http://www.gtk.org/gtk-doc/
license @ GPL + FDL
src_url @ http://ftp.gnome.org/pub/gnome/sources/$name/$version/$fullname.tar.xz
arch @ ~x86_64
"""

depends = """
common @ app-text/docbook-xsl-stylesheets
runtime @ dev-lang/perl
build @ dev-util/pkg-config
"""

def configure():
    conf('--with-xml-catalog="/etc/xml/docbook-xml"')

def build():
    installd()
