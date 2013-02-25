metadata = """
summary @ X authority file utility
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/releases/individual/app/$fullname.tar.bz2
arch @ ~x86_64
options @ ipv6
"""

depends = """
runtime @ x11-libs/libX11 x11-libs/libXau x11-libs/libXext x11-libs/libXmu
"""

def configure():
    conf(config_enable("ipv6"))
