metadata = """
summary @ Base layout of the filesystem
homepage @ http://hadronproject.org
license @ GPL-3
arch @ ~x86_64
"""


depends = """
runtime @ app-misc/iana-etc
common @ app-shells/bash sys-apps/coreutils
"""

standard_procedure = False

reserve_files = ["/etc/passwd", "/etc/hosts", "/etc/group", "/etc/fstab", \
        "/etc/resolv.conf", "/etc/shells", "/etc/host.conf", "/etc/issue" \
        "/etc/securetty", "/etc/shadow", "/etc/gshadow"]

def install():
    # setup root file system
    for item in ('/bin', '/boot', '/dev', '/etc', '/home',
            '/media', '/mnt', '/sbin',
            '/usr', '/var', '/run', '/opt', '/srv/http'):
        makedirs(item)

    makedirs("/proc")
    setmod("555", "%s/proc" % install_dir)

    makedirs("/sys")
    setmod("555", "%s/sys" % install_dir)

    makedirs("/root")
    setmod("0750", "%s/root" % install_dir)

    makedirs("/tmp")
    setmod("01777", "%s/tmp" % install_dir)

    makedirs("/srv/ftp")
    setmod("555", "%s/srv/ftp" % install_dir)
    setowner("ftp", "%s/srv/ftp" % install_dir)

    # setup /etc
    for item in ('ld.so.conf.d', 'skel', 'profile.d'):
        makedirs("/etc/%s" % item)

    for item in ('fstab', 'group', 'host.conf', 'hosts', 'issue',
            'ld.so.conf', 'motd', 'nsswitch.conf', 'os-release',
            'passwd', 'resolv.conf', 'securetty', 'shells', 'profile'):
        insfile("%s/%s" % (filesdir, item), "/etc")
        setmod("644", "%s/etc/%s" % (install_dir, item))

    makesym("/proc/self/mounts", "/etc/mtab")

    for item in ('gshadow', 'shadow', 'crypttab'):
        insfile("%s/%s" % (filesdir, item), "/etc")
        setmod("600", "%s/etc/%s" % (install_dir, item))

    echo("Hadron Base System Release 0.3", "/etc/hadron-release")

    for item in ('locale.sh', 'dircolors.sh', 'extrapaths.sh', \
            'readline.sh', 'umask.sh'):
        insfile("%s/%s" % (filesdir, item),  "/etc/profile.d/%s" % item)

    for item in ('cache/man', 'local', 'log/old', 'lib/misc', 'empty', 'games'):
        makedirs("/var/%s" % item)

    for item in ('tmp', 'spool/mail'):
        makedirs("/var/%s" % item)
        setmod("1777", "%s/var/%s" % (install_dir, item))

    setgroup("games", "%s/var/games" % install_dir)

    makesym("spool/mail", "/var/mail")
    makesym("../run", "/var/run")
    makesym("../run/lock", "/var/lock")

    for item in ('bin', 'include', 'lib', 'sbin', 'share/misc', 'src'):
        makedirs("/usr/%s" % item)

    for num in xrange(1, 9):
        makedirs("/usr/share/man/man/%d" % num)

    for item in ('bin', 'etc', 'games', 'include', 'lib', 'man', 'sbin', 'share', 'src'):
        makedirs("/usr/local/%s" % item)
    makesym("../man", "/usr/local/share/man")

    # /usr/lib migration
    makesym("usr/lib", "lib")
    makesym("usr/lib", "lib64")
    # FIXME: This is no good.
    cd(joinpath(install_dir, "usr"))
    makesym("lib", "usr/lib64")

# TODO: Write a library function to manage groups, users and passwords
# FIXME: improve post_install, check group existence 
def post_install():
    group_items = ('optical -g 93', 'audio   -g 92', 'video   -g 91', 'floppy  -g 94',
            'storage -g 95', 'log     -g 19', 'utmp    -g 20', 'power   -g 98', 'network -g 90',
            'games   -g 50', 'uucp    -g 14', 'http    -g 33', 'http    -u 33 -d /srv/http -g http -s /bin/false http',
            'scanner -g 96', 'rfkill  -g 24', 'uuidd   -g 68', 'lock    -g 54', 'uuidd    -u 68 -d / -g uuidd -s /sbin/nologin',
            'dbus    -g 81', 'dbus     -u 81 -d / -g dbus -s /sbin/nologin')

    with open("/etc/passwd") as groupfile:
        groupfile.readlines()
        for group_item in group_items:
            for line in groupfile:
                if not group_item.split("-g")[0].strip() in line:
                    system("/usr/sbin/groupadd %s >/dev/null" % group_item)
