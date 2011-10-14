metadata = """
summary @ Common development macros for GNOME
homepage @ http://www.gnome.org
license @ GPL
src_url @ http://ftp.gnome.org/pub/gnome/sources/$name/3.1/$name-$version.tar.bz2
arch @ ~x86
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)
    system("mv doc-build/README README.doc-build")
    insdoc("ChangeLog", "README*", "doc/usage.txt")
