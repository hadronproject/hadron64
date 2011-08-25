metadata = """
summary @ Backdrops for the Xfce4 desktop
homepage @ http://xfce-goodies.berlios.de/
license @ GPL2
src_url @ http://download2.berlios.de/xfce-goodies/$fullname.tar.gz
arch @ ~x86
"""

standard_procedure = False

def install():
    cd("backdrops")
    for suffix in ("png", "jpg"):
        insinto("*.%s" % suffix, "/usr/share/xfce4/backdrops")
