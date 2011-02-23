metadata = """
summary @ Terminal for XFCE4
license @ GPL-2
homepage @ http://www.xfce.org
src_url @ www.xfce.org/down/$name-$version.tar.bz2
"""
work_dir = "Terminal-0.4.5"


def install():
    raw_install("DESTDIR=%s" % install_dir)
