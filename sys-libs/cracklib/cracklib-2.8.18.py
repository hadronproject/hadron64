metadata = """
summary @ Password Checking library
homepage @ http://sourceforge.net/projects/cracklib
license @ GPL-3
src_url @ http://downloads.sourceforge.net/sourceforge/$name/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc sys-libs/zlib
"""

def prepare():
    patch(level=1)

def configure():
    conf("--without-python",
        "--with-default-dict=/usr/share/cracklib/pw_dict")

def install():
    raw_install("DESTDIR=%s install" % install_dir)

    insfile("dicts/cracklib-small", "/usr/share/dict/cracklib-small")
    system("sh ./util/cracklib-format dicts/cracklib-small \
                | sh ./util/cracklib-packer %s/usr/share/cracklib/pw_dict" % install_dir)
