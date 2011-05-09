metadata = """
summary @ Expat-based XML parser module for perl
homepage @ http://search.cpan.org/dist/XML-Parser
license @ GPL PerlArtistic
src_url @ http://search.cpan.org/CPAN/authors/id/C/CH/CHORNY/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ dev-lang/perl dev-libs/expat
"""

def configure():
    export("PERL_MM_USE_DEFAULT", "1")
    system("perl Makefile.PL PREFIX=/usr INSTALLDIRS=vendor DESTDIR=%s" % install_dir)

def build():
    make()
    make("test")

#def install():
#    raw_install("DESTDIR=%s" % install_dir)

