metadata = """
summary @ Perl wrappers for the GLib utility and Object libraries
homepage @ http://gtk2-perl.sf.net/
license @ LGPL-2.1
src_url @ http://downloads.sourceforge.net/sourceforge/gtk2-perl/Glib-$version.tar.gz
arch @ ~x86
"""

depends = """
common @ dev-lang/perl sys-libs/glib
build @ >=dev-perl/ExtUtils-PkgConfig-1.0 
>=dev-perl/ExtUtils-Depends-0.300
"""

srcdir = "Glib-%s" % version

def build():
    system("perl Makefile.PL INSTALLDIRS=vendor")

install = lambda: (installd(), rmfile("/usr/lib/perl5/core_perl/perllocal.pod"))
