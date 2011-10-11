metadata = """
summary @ Mount plugin for the Xfce panel
homepage @ http://goodies.xfce.org/projects/panel-plugins/xfce4-mount-plugin
license @ custom
src_url @ http://archive.xfce.org/src/panel-plugins/$name/1.0/$name-$version.tar.bz2
arch @ ~x86
options @ debug
"""

depends = """
common @ >=xfce-base/xfce4-panel-4.8 >=xfce-base/libxfcegui4-4.8
build @ dev-util/pkg-config dev-util/intltool
"""

def configure():
    conf(config_enable("debug"))

def install():
    raw_install("DESTDIR=%s install" % install_dir)
    insdoc("AUTHORS", "ChangeLog", "NEWS", "README", "TODO")
