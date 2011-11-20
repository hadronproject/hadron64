metadata = """
summary @ Package building and distribution system for Hadron GNU/Linux
homepage @ http://hadronproject.org
license @ GPL-3
arch @ ~x86
"""

depends = """
runtime @ dev-lang/python:2.7 dev-python/catbox net-misc/wget sys-apps/file
build @ dev-lang/python
"""

standard_procedure = False

reserve_files = ["/etc/lpms/build.conf", "/etc/lpms/repo.conf"]

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
    insinto("scripts/*", "/usr/sbin")
    
    setmod("+x %s/usr/sbin/create_file_relationsdb.py" % install_dir)
    setmod("+x %s/usr/sbin/create_reverse_dependsdb.py" % install_dir)
    setmod("+x %s/usr/sbin/migrate_filesdb.py" % install_dir)

    makedirs("etc/lpms")
    insinto("data/*", "/etc/lpms")

    for directories in ('/var/db/lpms', '/var/cache/lpms/sources',
            '/var/tmp/lpms', '/var/lib/lpms', '/var/tmp/merge-conf'):
        makedirs(directories)

    insdoc("COPYING", "AUTHORS", "README", "TODO")
