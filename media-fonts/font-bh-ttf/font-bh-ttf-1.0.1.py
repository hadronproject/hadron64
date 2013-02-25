metadata = """
summary @ X.org Luxi Truetype fonts
homepage @ http://xorg.freedesktop.org
license @ custom
src_url @ http://xorg.freedesktop.org/releases/individual/font/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ media-fonts/font-alias media-fonts/font-util media-libs/fontconfig
          media-fonts/encodings x11-apps/mkfontdir x11-apps/mkfontscale

"""

def configure():
    conf("--with-mapfiles=/usr/share/fonts/util",
        "--with-fontdir=/usr/share/fonts/TTF")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")

def post_install():
    notify("updating font cache... ")
    system("fc-cache -f > /dev/null")
    system("mkfontscale /usr/share/fonts/TTF")
    system("mkfontdir /usr/share/fonts/TTF")
