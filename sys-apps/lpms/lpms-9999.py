metadata = """
summary @ Package building and distribution system for Hadron GNU/Linux
homepage @ http://hadronproject.org
license @ GPL-3
arch @ ~x86_64
"""

# TODO: lpms uses python-file to handle mime types now. So we can remove sys-apps/file dependency

depends = """
runtime @ dev-lang/python:2.7 sys-apps/sydbox net-misc/wget sys-apps/file
common @ dev-lang/python:2.7
"""

get("git_utils")

standard_procedure = False

reserve_files = ["/etc/lpms/build.conf", "/etc/lpms/repo.conf"]

def prepare():
    git_clone("git://github.com/hadronproject/lpms.git", subdir=name)

def install():
    install_path = "/usr/lib/hadron/python/lpms"

    cd("lpms")

    makedirs(install_path)

    insinto("lpms/*", install_path)
    copytree("bin", install_path+"/../")

    makesym("../lib/hadron/python/bin/lpms", "/usr/bin/lpms")
    makesym("../lib/hadron/python/bin/merge-conf", "/usr/bin/merge-conf")

    makedirs("/etc/lpms")
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
