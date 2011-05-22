metadata = """
summary @ Abstraction for enumerating power devices, listening to device events and querying history and statistics
homepage @ http://upower.freedesktop.org
license @ GPL
src_url @ http://upower.freedesktop.org/releases/$fullname.tar.bz2
arch @ ~x86
"""

def configure():
    autoreconf("-fi")
    raw_configure("--prefix=/usr", 
            "--sysconfdir=/etc", 
            "--localstatedir=/var",
            "--libexecdir=/usr/lib/upower", 
            "--disable-static",
            "--disable-man-pages",
            "--disable-gtk-doc")

def build():
    # For g-i-r
    export("HOME", build_dir)
    make()

def install():
    export("HOME", build_dir)
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("ChangeLog", "COPYING", "README")
