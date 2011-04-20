metadata = """
summary @ A GNU tool for automatically creating Makefiles
homepage @ http://www.gnu.org/software/automake
license @ GPL-2
src_url @ ftp://ftp.gnu.org/gnu/$name/$name-$version.tar.gz
"""

def install():
    raw_install('DESTDIR=%s' % install_dir)
