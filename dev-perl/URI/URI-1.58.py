metadata = """
summary @ Uniform Resource Identifiers (absolute and relative)
homepage @ http://search.cpan.org/dist/$%7B_realname%7D/
license @ PerlArtistic
src_url @ http://cpan.org/CPAN/authors/id/G/GA/GAAS/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ dev-lang/perl
"""

def configure():
    system("perl Makefile.PL INSTALLDIRS=vendor")
    pass

def install():
    raw_install("DESTDIR=%s" % install_dir)
