metadata = """
summary @ Userspace tools for the kernel cpufreq subsystem
homepage @ http://www.kernel.org/pub/linux/utils/kernel/cpufreq/cpufrequtils.html
license @ GPL
src_url @ ftp://ftp.archlinux.org/other/$name/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-fs/sysfsutils
"""

def prepare():
    patch("cpufrequtils-008-remove-pipe-from-CFLAGS.patch")
    patch("cpufrequtils-008-cpuid.patch", level=1)
    patch("cpufrequtils-008-fix-compilation-on-x86-32-with-fPIC.patch", level=1)
    patch("cpufrequtils-008-increase-MAX_LINE_LEN.patch", level=1)
    patch("cpufrequtils-008-fix-msr-read.patch", level=1)
    patch("cpufrequtils-007-build.patch")
    patch("cpufrequtils-007-nls.patch", level=1)

def configure():
    pass

def build():
    make(j=1)

def install():
    raw_install("INSTALL='/bin/install -c' mandir=/usr/share/man DESTDIR=%s" % install_dir)
    insfile("%s/cpufreq.confd" % filesdir, "/etc/conf.d/cpufreq")
    insexe("%s/cpufreq.rcd" % filesdir, "/etc/rc.d/cpufrequtils")
