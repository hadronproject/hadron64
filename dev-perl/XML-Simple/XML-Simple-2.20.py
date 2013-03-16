metadata = """
summary @ Simple XML parser for stupid Perl
homepage @ http://search.cpan.org/dist/XML-Simple
license @ PerlArtistic
src_url @ http://search.cpan.org/CPAN/authors/id/G/GR/GRANTM/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ dev-perl/XML-Parser dev-lang/perl
"""

def configure():
    export("PERL_MM_USE_DEFAULT", "1")
    system("perl Makefile.PL PREFIX=/usr INSTALLDIRS=vendor DESTDIR=%s" % install_dir)

def install():
    raw_install("DESTDIR=%s" % install_dir)
