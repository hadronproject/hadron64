metadata = """
summary @ The Gnome System Monitor
homepage @ http://www.gnome.org/
license @ GPL2
src_url @ ftp://ftp.gnome.org/pub/gnome/sources/gnome-system-monitor/2.28/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glib gnome-base/gconf x11-libs/libwnck gnome-base/libgtop x11-libs/gtk+:2 
          x11-themes/gnome-icon-theme dev-cpp/gtkmm dev-cpp/glibmm dev-libs/libxml2
          gnome-base/librsvg dev-libs/dbus-glib

build @ dev-util/pkg-config app-text/gnome-doc-utils dev-util/intltool
"""

def configure():
    conf("-disable-scrollkeeper")

def install():
    raw_install("DESTDIR=%s" % install_dir)
