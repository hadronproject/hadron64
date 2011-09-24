metadata = """
summary @ This little program lets you change your Gtk+ 2.0 theme. A better alternative to switch2
homepage @ http://plasmasturm.org/programs/gtk-chtheme/
license @  GPL
src_url @  http://plasmasturm.org/programs/gtk-chtheme/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
common @ x11-libs/gtk+
build @ dev-util/pkg-config
"""

def prepare():
    system('sed -i -e "s:strip:true:" Makefile')
    patch(level=1)

def configure():
    pass

def install():
	insexe("gtk-chtheme", "/usr/bin/gtk-chtheme")
	pass


#todo sed
