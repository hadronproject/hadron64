metadata = """
summary @ Library and command line tools for XZ and LZMA compressed files
homepage @ http://tukaani.org/xz/
license @ GPL LGPL custom
src_url @ http://tukaani.org/$name/$fullname.tar.gz
arch @ ~x86_64
options @ nls static-libs threads
"""

def configure():
    conf(config_enable("nls"),
        config_enable("static-libs"),
        config_enable("threads"))

def install():
    raw_install('DESTDIR=%s' % install_dir)
    insdoc('AUTHORS', 'ChangeLog', 'NEWS', 'README', 'THANKS')
