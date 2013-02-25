metadata = """
summary @ Command-line interface to various pastebins
homepage @ http://wgetpaste.zlin.dk/
license @ public-domain
src_url @ http://wgetpaste.zlin.dk/$fullname.tar.bz2
arch @ ~x86
options @ zsh-completion
"""

depends = """
runtime @ net-misc/wget
"""

standard_procedure=False

def install():
    insexe("%s/wgetpaste" % build_dir, "/usr/bin/wgetpaste")
    if opt("zsh-completion"):
        insfile("%s/_wgetpaste" % filesdir, "/usr/share/zsh/site-functions/_wgetpaste")
