metadata = """
summary @ Filesystem baselayout
homepage @ http://hadronproject.org
license @ GPL-3
arch @ ~x86
"""

depends = """
common @ app-misc/iana-etc app-shells/bash sys-apps/coreutils
"""

standard_procedure = False

reserve_files = ["/etc/passwd", "/etc/hosts", "/etc/group", "/etc/fstab", \
        "/etc/resolv.conf", "/etc/shells", "/etc/host.conf", "/etc/issue" \
        "/etc/securetty", "/etc/shadow", "/etc/gshadow"]

def install():
    for d in ('bin', 'boot', 'dev', 'etc', 'home',
            'lib/modules', 'media', 'mnt', 'sbin',
            'usr', 'var', 'sys', 'run'):
        makedirs(d)

    system("install -d -m555 %s/proc" % install_dir)
    system("install -d -m0750 %s/root" % install_dir)
    system("install -d -m1777 %s/tmp" % install_dir)

    for e in ('fstab', 'group', 'host.conf', 'hosts', 'issue',
            'ld.so.conf', 'motd', 'passwd', 'resolv.conf',
            'securetty', 'shells', 'profile'):
        insfile("%s/%s" % (filesdir, e), "/etc")

    for f in ('gshadow', 'shadow'):
        system("install -m600 %s/%s %s/etc" % (filesdir, f, install_dir))

    echo("Hadron Base System Release 0.2", "/etc/hadron-release")

    for i in ('cache/man', 'local', 'opt', 'run', 'log/old', 'lib/misc', 'empty'):
        makedirs("/var/%s" % i)

    for v in ('lock', 'tmp', 'spool/mail'):
        system("install -d -m1777 %s/var/%s" % (install_dir, v))

    for u in ('bin', 'include', 'lib', 'sbin', 'share/misc', 'src'):
        makedirs("/usr/%s" % u)

# FIXME: improve post_install, check group existence 
def post_install():
    cmd = ('optical -g 93', 'optical -g 93', 'audio   -g 92', 'video   -g 91', 'floppy  -g 94',
            'storage -g 95', 'log     -g 19', 'utmp    -g 20', 'power   -g 98', 'network -g 90',
            'games   -g 50', 'uucp    -g 14', 'http    -g 33', 'http    -u 33 -d /srv/http -g http -s /bin/false http',
            'scanner -g 96', 'rfkill  -g 24')
    with open("/etc/passwd") as groupfile:
        groupfile.readlines()
        for c in cmd:
            for x in groupfile:
                if not c.split("-g")[0].strip() in c:
                    system("/usr/sbin/groupadd %s >/dev/null" % c)
    system("/usr/sbin/grpconv")
