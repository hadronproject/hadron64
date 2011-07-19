metadata = """
summary @ A console based real time MPEG Audio Player for Layer 1, 2 and 3
homepage @ http://sourceforge.net/projects/mpg123
license @ GPL2 LGPL2.1
src_url @ http://downloads.sourceforge.net/sourceforge/$name/$name-$version.tar.bz2
arch @ ~x86
options @ ipv6
"""

depends = """
build @ dev-util/pkg-config sys-devel/libtool media-libs/alsa-lib
"""

def configure():
    conf(
    config_enable("ipv6"),
    '--with-audio="alsa"',
    "--with-cpu=x86")
