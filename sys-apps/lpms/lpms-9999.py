metadata = """
summary @ Package building and distribution system for Hadron GNU/Linux
homepage @ http://hadronproject.org
license @ GPL-3
arch @ ~x86
"""

depends = """
runtime @ dev-lang/python dev-python/catbox

build @ dev-lang/python
"""

standart_procedure = False

def prepare():
    notify("cloning git://gitorious.org/hadron/lpms.git")
    if not system("git clone git://gitorious.org/hadron/lpms.git"):
        error("git clone failed.")

def install():
    install_path = "/usr/lib/python2.7/site-packages/lpms"

    cd("lpms")

    makedirs(install_path[1:])

    insinto("src/*", install_path)
    insinto("bin/*", "/usr/bin")

    makedirs("etc/lpms")
    insinto("data/*", "/etc/lpms")

    for directories in ('/var/db/lpms', '/var/cache/lpms/sources', 
            '/var/tmp/lpms', '/var/lib/lpms', '/var/tmp/merge-conf'):
        makedirs(directories)

    insdoc("COPYING", "AUTHORS", "README", "TODO")
