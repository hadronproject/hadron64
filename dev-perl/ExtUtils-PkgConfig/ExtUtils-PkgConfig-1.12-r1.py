metadata = """
summary @ The Perl Pkgconfig module
homepage @ http://gtk2-perl.sourceforge.net/
license @ LGPL
src_url @ http://downloads.sourceforge.net/sourceforge/gtk2-perl/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ dev-lang/perl
"""

def configure():
	pass

def build():
	system("perl Makefile.PL INSTALLDIRS=vendor")
	make()

def install():
	raw_install("DESTDIR=%s" % install_dir)
        rmfile("/usr/lib/perl5/core_perl/perllocal.pod")
