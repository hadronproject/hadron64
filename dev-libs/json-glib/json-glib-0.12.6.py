metadata = """
summary @ JSON library built on GLib 
homepage @ http://live.gnome.org/JsonGlib 
license @ GPL 
src_url @ http://ftp.gnome.org/pub/GNOME/sources/$name/0.12/$name-$version.tar.bz2 
arch @ ~x86
options @ introspection
"""

depends = """
runtime @ >=sys-libs/glib-2.16:2
"""

opt_build = """
introspection @ >=dev-libs/gobject-introspection-0.9.5
"""

def configure():
    conf("--disable-gcov", config_enable("introspection"))

def build():
	export("HOME", build_dir)
	make()
