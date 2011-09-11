metadata = """
summary @ Extensions to Xfce by os-cillation
homepage @ http://www.xfce.org/projects/exo
license @ GPL2 + LGPL
src_url @ http://archive.xfce.org/src/xfce/exo/0.6/$fullname.tar.bz2
arch @ ~x86
options @ debug python
"""

depends = """
runtime @ xfce-base/libxfce4util x11-libs/gtk+ x11-themes/hicolor-icon-theme
build @ dev-util/intltool x11-apps/iceauth dev-perl/URI
"""

opt_build = """
python @ dev-python/pygtk
"""

def prepare():
    rmfile("py-compile")
    makesym("/bin/true", "py-compile")
    system("intltoolize --force --copy --automake")

def configure():
    conf("--libexecdir=/usr/lib/xfce4 \
            --disable-static \
            --enable-gio-unix \
            --disable-gtk-doc",
            config_enable("debug"),
            config_enable("python"))

def build():
    export("PYTHONDONTWRITEBYTECODE", "1")
    make()

def install():
    raw_install("DESTDIR=%s" % install_dir)

def post_install():
    system("gtk-update-icon-cache -q -t -f /usr/share/icons/hicolor")

    system("/usr/bin/gio-querymodules /usr/lib/gio/modules")
