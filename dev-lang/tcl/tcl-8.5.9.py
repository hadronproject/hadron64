metadata = """
summary @  Tool Command Language, a weird scripting language
homepage @ http://tcl.sourceforge.net
license @ BSD
src_url @ http://downloads.sourceforge.net/sourceforge/$name/$name$version-src.tar.gz
options @ debug threads
"""

srcdir = "tcl8.5.9"

def configure():
    cd("unix")
    conf(config_enable('threads'),
        config_enable('debug', 'symbols'))

def build():
    cd("unix")
    make()

def install():
    cd("unix")
    raw_install('DESTDIR=%s install install-private-headers' % install_dir)
