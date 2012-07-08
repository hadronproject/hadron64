metadata = """
summary @ Package building and distribution system for Hadron GNU/Linux
homepage @ http://hadronproject.org
license @ GPL-3
arch @ ~x86_64
"""

depends = """
runtime @ dev-lang/python:2.7 sys-apps/sydbox net-misc/wget sys-apps/file
common @ dev-lang/python:2.7
"""

get("git_utils")

standard_procedure = False

reserve_files = ["/etc/lpms/build.conf", "/etc/lpms/repo.conf"]

def prepare():
    git_clone("git://gitorious.org/hadron/lpms.git", subdir=name)

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
    setmod("+x %s/usr/sbin/insert_slot_filesdb.py" % install_dir)

    makedirs("etc/lpms")
    insinto("data/*", "/etc/lpms")

    for directories in ('/var/db/lpms', '/var/cache/lpms/sources',
            '/var/tmp/lpms', '/var/lib/lpms', '/var/tmp/merge-conf',
            '/etc/lpms/user'):
        makedirs(directories)

    user_readme = """
    # this is the directory for fucking with options like 'app-editors/nano nls'
    # the files that you can define 
    # * lock
    # * unlock
    # * options
    # * ldflags
    # * cflags
    # * cxxflags 
    """
    
    echo(user_readme, "/etc/lpms/user/README")

    insdoc("COPYING", "AUTHORS", "README", "TODO")
