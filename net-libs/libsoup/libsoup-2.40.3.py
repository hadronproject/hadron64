metadata = """
summary @ An HTTP library implementation in C
homepage @ http://live.gnome.org/LibSoup
license @ LGPL-2
src_url @ ftp://ftp.gnome.org/pub/gnome/sources/libsoup/2.40/$fullname.tar.xz
arch @ ~x86_64
options @ introspection ssl
"""

depends = """
common @ dev-libs/libxml2 sys-libs/glib
build @ dev-util/gtk-doc dev-util/intltool
"""

opt_common = """
introspection @ net-libs/glib-networking
"""

def configure():
    conf("--disable-static",
            "--disable-tls-check",
            "--without-gnome",
            "--without-apache-httpd",
            config_enable("introspection"))

def build():
    export("HOME", build_dir)
    make()

def install():
    raw_install("DESTDIR=%s" % install_dir)
