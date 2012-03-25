metadata = """
summary @ Documentation tool for public library API
homepage @ http://www.gtk.org/gtk-doc/
license @ GPL + FDL
src_url @ http://ftp.gnome.org/pub/gnome/sources/$name/$version/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ app-text/docbook-xsl-stylesheets dev-lang/perl
build @ dev-util/pkg-config
"""

def configure():
    conf('--with-xml-catalog="/etc/xml/docbook-xml"')

def build():
    installd()
