metadata = """
summary @ Command-line interface to various pastebins
homepage @ http://wgetpaste.zlin.dk/
license @ public-domain
src_url @ http://wgetpaste.zlin.dk/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ net-misc/wget
"""

standart_procedure=False

def install():
    insexe("%s/wgetpaste" % build_dir, "/usr/bin/wgetpaste")
