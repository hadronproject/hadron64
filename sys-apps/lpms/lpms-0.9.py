metadata = """
summary @ Package building and distribution system for Hadron GNU/Linux
homepage @ http://hadronproject.org
license @ GPL-3
src_url @ http://hadronproject.org/distfiles/$name/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ >=dev-lang/python-2.7 (sqlite xml)
        dev-python/catbox

build @ dev-lang/python(sqlite)
"""

standart_procedure = False

srcdir = "lpms"

def install():
    install_path = "/usr/lib/python2.7/site-packages/lpms"
    
    makedirs(install_path[1:])

    insinto("src/*", install_path)
    insinto("bin/*", "/usr/bin")

    makedirs("etc/lpms")
    insinto("data/*", "/etc/lpms")

    for directories in ('var/db/lpms', 'var/cache/lpms/sources', 
            'var/tmp/lpms', 'var/lib/lpms'):
        makedirs(directories)

    insdoc("COPYING", "AUTHORS", "README", "TODO")
