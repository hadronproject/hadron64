metadata = """
summary @ A daemon which implements the Point-to-Point Protocol for dial-up networking
homepage @ http://www.samba.org/ppp/
license @ custom:GPL/BSD
src_url @ ftp://ftp.samba.org/pub/ppp/ppp-$version.tar.gz
arch @ ~x86
options @ activefilter ipv6
"""

depends = """
runtime @ sys-libs/glibc
"""

def configure():
    system('sed -i "s:-O2 -pipe -Wall -g:${CFLAGS}:" pppd/Makefile.linux')
    system('sed -i "s:-g -O2:${CFLAGS}:" pppd/plugins/Makefile.linux')
    system('sed -i "s:-O2:${CFLAGS}:" pppstats/Makefile.linux')
    system('sed -i "s:-O2 -g -pipe:${CFLAGS}:" chat/Makefile.linux')
    system('sed -i "s:-O:${CFLAGS}:" pppdump/Makefile.linux')
    if opt("activefilter"):
        system('sed -i "s:^#FILTER=y:FILTER=y:" pppd/Makefile.linux')
    if opt("ipv6"):
        system('sed -i "s:^#HAVE_INET6=y:HAVE_INET6=y:" pppd/Makefile.linux')
    system('sed -i "s:^#CBCP=y:CBCP=y:" pppd/Makefile.linux ')
    system('rm include/linux/if_pppol2tp.h ')

    conf()

def install():

    raw_install("DESTDIR=%s/usr" % install_dir)

    for bu in ("ip-down", "ip-down.d.dns.sh", "ip-up", "ip-up.d.dns.sh", "options"):
        insfile("%s/%s" % (filesdir, bu), "/etc/ppp/%s" % bu)

    for su in ("pon", "poff"):
        insexe("%s/%s" % (filesdir, su), "/usr/bin/%s" % su)

    insexe("%s/plog" % filesdir, "/usr/sbin/plog")
    insexe("%s/ppp" % filesdir, "/etc/rc.d/ppp")



#TODO WTF? http://gpo.zugaina.org/AJAX/Ebuild/2233671/View
