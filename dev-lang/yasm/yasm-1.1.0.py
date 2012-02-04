metadata = """
summary @ A rewrite of NASM to allow for multiple syntax supported (NASM, TASM, GAS, etc.)
homepage @ http://www.tortall.net/projects/yasm/
license @ BSD-2 BSD
src_url @ http://www.tortall.net/projects/yasm/releases/$fullname.tar.gz
arch @ ~x86
options @ nls
"""

depends = """
runtime @ sys-libs/glibc
"""

opt_build = """
nls @ sys-devel/gettext
"""

def configure():
    export("PYTHONDONTWRITEBYTECODE", "1")
    conf(
    config_enable("nls"),
    "--disable-dependency-tracking")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("AUTHORS")

#TODO add python option via cython package: http://gpo.zugaina.org/AJAX/Ebuild/2238441/View
