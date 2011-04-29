metadata = """
summary @ Password Checking library
homepage @ http://sourceforge.net/projects/cracklib
license @ GPL-3
src_url @ http://downloads.sourceforge.net/sourceforge/$name/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc sys-libs/zlib
"""

def configure():
    conf("--without-python")

def install():
    raw_install("DESTDIR=%s install" % install_dir)

    insfile("dicts/cracklib-small", "/usr/share/dict/cracklib-small")
    system("sh ./util/cracklib-format dicts/cracklib-small \
                | sh ./util/cracklib-packer $pkgdir/usr/share/cracklib/pw_dict")
