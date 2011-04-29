metadata = """
summary @ A GNU tool for automatically creating Makefiles
homepage @ http://www.gnu.org/software/automake
license @ GPL-2
src_url @ ftp://ftp.gnu.org/gnu/$name/$name-$version.tar.gz
"""

depends = """
build @ dev-lang/perl sys-devel/autoconf 
        sys-devel/patch

runtime @ dev-lang/perl sys-devel/autoconf
"""

def install():
    raw_install('DESTDIR=%s' % install_dir)
