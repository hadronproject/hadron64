metadata = """
summary @ Object Oriented Scripting Language
homepage @ http://www.python.org
license @ GPL-2
src_url @ http://www.python.org/ftp/python/2.7.1/Python-2.7.1.tar.bz2 
options @ berkdb gdbm ipv6 ncurses readline sqlite ssl threads tk wide-unicode xml build doc examples wininst
"""
srcdir = "Python-2.7.1"

def install():
    raw_install("DESTDIR=%s" % install_dir)

    for doc in ('ACKS', 'HISTORY', 'NEWS'):
        insdoc(joinpath("Misc", doc))
