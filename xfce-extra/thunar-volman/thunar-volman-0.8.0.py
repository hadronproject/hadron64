metadata = """
summary @ automatic management for removeable devices in thunar
homepage @ http://foo-projects.org/~benny/projects/thunar-volman
license @ GPL2
src_url @ http://archive.xfce.org/src/apps/$name/0.8/$fullname.tar.bz2
arch @ ~x86_64
options @ debug libnotify
"""

depends = """
runtime @ xfce-base/thunar xfce-base/libxfce4ui x11-themes/hicolor-icon-theme
"""

opt_runtime = """
libnotify @ x11-libs/libnotify
"""

def configure():
    raw_configure("--prefix=/usr",
            "--sysconfdir=/etc",
            "--libexecdir=/usr/lib/xfce4",
            "--localstatedir=/var",
            "--disable-static",
            config_enable("debug"),
            config_enable("libnotify", "notifications"))

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("AUTHORS", "ChangeLog", "NEWS", "README", "THANKS")

def post_install():
    system("gtk-update-icon-cache -q -t -f /usr/share/icons/hicolor")
