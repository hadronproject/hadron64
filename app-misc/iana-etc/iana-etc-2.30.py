metadata = """
summary @ /etc/protocols and /etc/services provided by IANA
homepage @ http://sethwklein.net/iana-etc
license @ custom
src_url @ http://sethwklein.net/$fullname.tar.bz2
arch @ ~x86_64
"""

def prepare():
    patch()

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("COPYING")
