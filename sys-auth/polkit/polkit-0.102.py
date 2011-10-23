metadata = """
summary @ Application development toolkit for controlling system-wide privileges
homepage @ http://www.freedesktop.org/wiki/Software/PolicyKit
license @ LGPL
src_url @ http://hal.freedesktop.org/releases/$fullname.tar.gz
arch @ ~x86 
options @ introspection
"""

depends = """
runtime @ sys-libs/pam dev-libs/expat sys-libs/glib
build @ dev-util/intltool
"""

opt_runtime = """
introspection @ dev-libs/gobject-introspection
"""

def configure():
    conf("--with-pam-module-dir=/lib/security/",
            "--libexecdir=/usr/lib/polkit-1",
            "--disable-man-pages",
            "--disable-gtk-doc",
            "--disable-static",
            "--enable-examples",
            config_enable("introspection"))

def build():
    export("HOME", build_dir)
    make()

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insfile("%s/polkit.pam" % filesdir, "/etc/pam.d/polkit-1")
