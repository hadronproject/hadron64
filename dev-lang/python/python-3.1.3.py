metadata = """
summary @ Object Oriented Scripting Language
homepage @ http://www.python.org
license @ GPL-2
src_url @ http://python.org/ftp/$name/$version/Python-$version.tar.bz2 
options @ berkdb gdbm ipv6 ncurses readline sqlite ssl threads tk wide-unicode xml build doc examples wininst
"""

work_dir = "Python-3.1.3"

def install():
    raw_install("DESTDIR=%s" % install_dir)

    for doc in ('ACKS', 'HISTORY', 'NEWS'):
        insdoc(joinpath("Misc", doc))
