metadata = """
summary @ Excellent text file viewer
homepage @ http://www.greenwoodsoftware.com/
license @ GPL-3
src_url @ http://www.greenwoodsoftware.com/$name/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/ncurses dev-libs/pcre
"""

def install():
    linstall()
    insdoc("NEWS", "README", "COPYING")
