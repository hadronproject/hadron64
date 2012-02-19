metadata = """
summary @ Collection of user space tools for general SMBus access and hardware monitoring
homepage @ http://www.lm-sensors.org/
license @ GPL-2 LGPL-2.1
src_url @ http://dl.lm-sensors.org/lm-sensors/releases/$fullname.tar.bz2
options @ sensord
arch @ ~x86
"""

depends = """
common @ dev-lang/perl
build @ sys-apps/sed sys-devel/bison sys-devel/flex
"""

opt_common = """
sensord @ net-analyzer/rrdtool
"""

def prepare():
    notify("%s requires CONFIG_HWMON to be enabled for use." % name)
    notify("sensors-detect requires CONFIG_I2C_CHARDEV to be enabled.")
    notify("%s requires CONFIG_I2C to be enabled for most sensors." % name)

    if opt("sensord"):
        sed("-i -e 's:^#\(PROG_EXTRA.*\):\1:' Makefile")
    sed("-i -e 's/\$(LIBDIR)$/\$(LIBDIR) \$(LDFLAGS)/g' Makefile")
    sed("-i -e 's|/etc/sysconfig|/etc/conf.d|' \
                     -e 's|/etc/init.d/lm_sensors|/etc/rc.d/sensors|' \
                     prog/{detect/sensors-detect,init/lm_sensors.service}")
    patch("daemonarg.patch", level=1)
    patch("linux_3.0.patch")

def build():
    make("PREFIX=/usr")

def install():
    raw_install("PROG_EXTRA=sensord BUILD_STATIC_LIB=0 \
                PREFIX=/usr MANDIR=/usr/share/man DESTDIR='%s'" % install_dir)
    insfile("prog/init/lm_sensors.service", "/lib/systemd/system/lm_sensors.service")
    insfile("%s/sensors.rc" % filesdir, "/etc/rc.d/sensors")
    insfile("%s/fancontrol.rc" % filesdir, "/etc/rc.d/fancontrol")
    insfile("%s/healthd" % filesdir, "/usr/sbin/healthd")
    insfile("%s/healthd.rc" % filesdir, "/etc/rc.d/healthd")
    insfile("%s/healthd.conf" % filesdir, "/etc/conf.d/healthd")
    if opt("sensord"):
        insfile("%s/sensord.rc" % filesdir, "/etc/rc.d/sensord")
        insfile("%s/sensord.conf" % filesdir, "/etc/conf.d/sensord")
