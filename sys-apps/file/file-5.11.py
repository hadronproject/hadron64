metadata = """
summary @ File type identification utility
homepage @ http://www.darwinsys.com/file/
license @ as-is
src_url @ ftp://ftp.astron.com/pub/$name/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
build @ dev-lang/python

runtime @ sys-libs/glibc
        sys-libs/zlib
"""

#def prepare():
#    patch(level=1)

def install():
    export("PYTHONDONTWRITEBYTECODE", "1")
    raw_install('DESTDIR=%s' % install_dir)
    insdoc("README", "ChangeLog", "MAINT")
    # install magic library
    cd("python")
    system("python setup.py install --root=%s --no-compile -O0" % install_dir)
