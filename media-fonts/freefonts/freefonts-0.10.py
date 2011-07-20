metadata = """
summary @ A Collection of Free Type1 Fonts
homepage @  http://www.gimp.org
license @ FIXME
src_url @ http://distfiles.gentoo.org/distfiles/freefonts-0.10.tar.gz
arch @ ~x86
"""

standart_procedure = False

srcdir = "freefont"

depends = """
runtime @ x11-apps/mkfontdir x11-apps/mkfontscale
"""

def install():
    insinto("*.pfb", "/usr/share/fonts/freefonts")

def post_install():
    notify("updating font cache... ")
    system("fc-cache -f > /dev/null")
    system("mkfontdir /usr/share/fonts/freefonts")
    #    system("xset fp+ /usr/share/doc/freefonts-%s" % version)
#    system("xset fp rehash")

