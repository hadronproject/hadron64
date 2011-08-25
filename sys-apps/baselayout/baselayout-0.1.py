metadata = """
summary @ Filesystem baselayout
homepage @ http://hadronproject.org
license @ GPL-3
arch @ ~x86
"""

standard_procedure = False

def install():
    for d in ('bin', 'boot', 'dev', 'etc', 'home',
            'lib/modules', 'media', 'mnt', 'sbin',
            'usr', 'var', 'sys'):
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

    echo("Hadron Base System Release 0.1", "%s/etc/hadron-release" % install_dir)

    for i in ('cache/man', 'local', 'opt', 'run', 'log/old', 'lib/misc', 'empty'):
        makedirs("/var/%s" % i)

    for v in ('lock', 'tmp', 'spool/mail'):
        system("install -d -m1777 %s/var/%s" % (install_dir, v))

    for u in ('bin', 'include', 'lib', 'sbin', 'share/misc', 'src'):
        makedirs("/usr/%s" % u)

def post_install():
    cmd = ('optical -g 93', 'optical -g 93', 'audio   -g 92', 'video   -g 91', 'floppy  -g 94',
            'storage -g 95', 'log     -g 19', 'utmp    -g 20', 'power   -g 98', 'network -g 90',
            'games   -g 50', 'uucp    -g 14', 'http    -g 33', 'http    -u 33 -d /srv/http -g http -s /bin/false http',
            'scanner -g 96', 'rfkill  -g 24')
    groupfile = open("/etc/passwd").readlines()
    for c in cmd:
        for x in groupfile:
            if not c.split("-g")[0].strip() in c:
                system("/usr/sbin/groupadd %s >/dev/null" % c)
    system("/usr/sbin/grpconv")
