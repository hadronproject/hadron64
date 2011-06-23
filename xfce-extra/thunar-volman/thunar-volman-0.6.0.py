metadata = """
summary @ automatic management for removeable devices in thunar
homepage @ http://foo-projects.org/~benny/projects/thunar-volman
license @ GPL2
src_url @ http://archive.xfce.org/src/apps/$name/0.6/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ xfce-base/thunar xfce-base/libxfce4ui x11-themes/hicolor-icon-theme
"""

def configure():
    raw_configure("--prefix=/usr",
            "--sysconfdir=/etc",
            "--libexecdir=/usr/lib/xfce4",
            "--localstatedir=/var",
            "--disable-static",
            "--disable-debug")

def install():
    raw_install("DESTDIR=%s" % install_dir)

def post_install():
    system("gtk-update-icon-cache -q -t -f /usr/share/icons/hicolor")
