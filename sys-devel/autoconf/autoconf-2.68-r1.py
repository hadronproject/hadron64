metadata = """
summary @ A GNU tool for automatically configuring source code
homepage @ http://www.gnu.org/software/autoconf
license @ GPL-2
src_url @ ftp://ftp.gnu.org/gnu/$name/$name-$version.tar.gz
"""

depends = """
runtime @ sys-devel/m4 dev-lang/perl sys-apps/diffutils
        sys-apps/texinfo app-shells/bash sys-apps/gawk
"""

def install():
    raw_install('DESTDIR=%s' % install_dir)
    insdoc("COPYING.EXCEPTION")
    rmfile("/usr/share/info/standards.info")
