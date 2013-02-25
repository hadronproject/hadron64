metadata = """
summary @ Cantarell fonts, default fontset for GNOME Shell
homepage @ http://live.gnome.org/CantarellFonts
license @ OFL-1.1
src_url @ http://ftp.gnome.org/pub/GNOME/sources/cantarell-fonts/0.0/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ media-libs/fontconfig
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)

    makedirs("/etc/fonts/conf.d")

    makesym("fontconfig/conf.avail/31-cantarell.conf", 
            "/etc/fonts/conf.d/31-cantarell.conf")
