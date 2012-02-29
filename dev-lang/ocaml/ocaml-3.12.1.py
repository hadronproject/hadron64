metadata = """
summary @ A functional language with OO extensions
homepage @ http://caml.inria.fr/
license @ LGPL-2 QPL-1.0
src_url @ http://caml.inria.fr/distrib/ocaml-3.12/$fullname.tar.gz
arch @ ~x86
"""

depends = """
build @ sys-libs/gdbm
"""

def configure():
    raw_configure("-prefix /usr")

def build():
    make("world.opt", j=1)

def install():
    raw_install('PREFIX="%s/usr" MANDIR="%s/usr/share/man"' \
            % (install_dir, install_dir))
    insdoc("LICENSE")
