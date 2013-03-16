metadata = """
summary @ A set of additional themes for the Xfce window manager
homepage @ http://www.xfce.org
license @ GPL-2
src_url @ http://archive.xfce.org/src/art/$name/4.10/$fullname.tar.bz2
arch @ ~x86_64
"""

depend = """
common @ xfce-base/xfwm4
"""

install = lambda: installd()
