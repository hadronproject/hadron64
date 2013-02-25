metadata = """
summary @ A full-featured and high-performance event loop
homepage @ http://software.schmorp.de/pkg/libev.html
license @ BSD
src_url @ http://dist.schmorp.de/$name/$name-$version.tar.gz
arch @ ~x86_64
options @ static-libs
"""

depends = """
common @ sys-libs/glibc
"""

#def prepare():
#    patch(level=1)
#    autoreconf()

def configure():
    conf(config_enable("static-libs", "static"))

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("Changes", "README")

#TODO:preserve old lib http://gentoo-overlays.zugaina.org/funtoo/portage/dev-libs/libev/libev-4.04.ebuild
