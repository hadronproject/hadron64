metadata = """
summary @ Meanwhile (Sametime protocol) library
homepage @ http://meanwhile.sourceforge.net/
license @ LGPL-2
src_url @ http://downloads.sourceforge.net/project/$name/$name/$version/$fullname.tar.gz
arch @ ~x86_64
options @ doc debug
"""

depends = """
runtime @ sys-libs/glib
build @ dev-libs/gmp dev-util/pkg-config
"""

opt_runtime = """
doc @ app-doc/doxygen
"""

def configure():
    options = " "
    if opt("doc"):
        options += "--enable-doxygen=yes"
    else:
        options += "--enable-doxygen=no"
    conf(
    config_enable("debug"), options)

#todo doc support
