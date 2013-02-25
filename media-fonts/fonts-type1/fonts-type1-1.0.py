metadata = """
summary @ X.Org Type1 Fonts
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org//releases/individual/font/font-adobe-utopia-type1-1.0.2.tar.bz2 http://xorg.freedesktop.org/releases/individual/font/font-bh-type1-1.0.1.tar.bz2 http://xorg.freedesktop.org/releases/individual/font/font-bitstream-type1-1.0.1.tar.bz2 http://xorg.freedesktop.org/releases/individual/font/font-ibm-type1-1.0.1.tar.bz2 http://xorg.freedesktop.org/releases/individual/font/font-xfree86-type1-1.0.2.tar.bz2
arch @ ~x86_64
"""

def configure():
    for pack in ("font-adobe-utopia-type1-1.0.2",  "font-bitstream-type1-1.0.1",  "font-bh-type1-1.0.1", "font-ibm-type1-1.0.1", "font-xfree86-type1-1.0.2"):
        cd("../%s" % pack)
        conf("--with-fontdir=/usr/share/fonts/Type1")
        make()
        raw_install("DESTDIR=%s" % install_dir)
    pass

def build():
    pass

def install():
    pass

def post_install():
    notify("Updating font cache...")
    system("fc-cache -f > /dev/null")
    system("mkfontscale /usr/share/fonts/Type1")
    system("mkfontdir /usr/share/fonts/Type1")
