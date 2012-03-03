metadata = """
summary @ Faster merging drop-in for slocate
license @ GPL
homepage @ http://carolina.mff.cuni.cz/~trmac/blog/mlocate
src_url @ https://fedorahosted.org/releases/m/l/mlocate/$fullname.tar.xz
arch @ ~x86
options @ nls
"""

depends = """
build @ app-arch/xz
"""

opt_runtime = """
nls @ sys-devel/gettext
"""

reserve_files = ["/etc/updatedb.conf"]

def configure():
    sed("""-i '/^groupname /s/mlocate/locate/' Makefile.in""")
    conf(config_enable('nls'))

def install():
    installd()
    insfile("%s/updatedb.conf" % filesdir, "/etc/updatedb.conf")

def post_install():
    system("""getent group slocate &>/dev/null && usr/sbin/groupdel slocate &>/dev/null""")
    system("""getent group mlocate &>/dev/null && usr/sbin/groupdel mlocate &>/dev/null""")
    system("""getent group locate &>/dev/null || usr/sbin/groupadd -g 21 locate &>/dev/null""")
    system("""chown -R root:locate /var/lib/mlocate""")

    notify("Edit /etc/updatedb.conf if you want and run updatedb as root.")

def post_upgrade():
    post_install()

#TODO: lpms-ize the post install
#TODO: when we can manage cronjobs and/or have a policy for it, use cronjob file
