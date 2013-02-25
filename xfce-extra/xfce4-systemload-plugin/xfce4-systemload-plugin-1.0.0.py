metadata = """
summary @ A system load plugin for the Xfce4 panel
homepage @ http://goodies.xfce.org/projects/panel-plugins/xfce4-systemload-plugin
license @ custom
src_url @ http://archive.xfce.org/src/panel-plugins/$name/1.0/$name-$version.tar.bz2
arch @ ~x86_64
options @ debug
"""

depends = """
common @ >=x11-libs/gtk+-2.6:2 >=xfce-base/xfce4-panel-4.8 >=xfce-base/libxfcegui4-4.8
>=xfce-base/libxfce4util-4.8
build @ dev-util/pkg-config dev-util/intltool
"""

def configure():
    conf(config_enable("debug"))

def install():
    raw_install("DESTDIR=%s install" % install_dir)
    insdoc("AUTHORS", "ChangeLog", "NEWS", "README")
