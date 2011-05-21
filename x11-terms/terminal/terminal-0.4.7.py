metadata = """
summary @ Terminal for XFCE4
license @ GPL-2
homepage @ http://www.xfce.org
src_url @ http://archive.xfce.org/src/apps/$name/0.4/Terminal-$version.tar.bz2
options @ debug
"""

srcdir = "Terminal-%s" % version

def configure():
    conf("--libexecdir=/usr/lib/xfce4",
            "--disable-static",
            "--disable-debug")
def install():
    raw_install("DESTDIR=%s" % install_dir)

