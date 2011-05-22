metadata = """
summary @ Utilities and scripts for suspend and hibernate power management
homepage @ http://pm-utils.freedesktop.org
license @ GPL
src_url @ http://pm-utils.freedesktop.org/releases/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-process/procps sys-power/pm-quirks
"""

def prepare():
    patch(level=1)

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insfile("%s/11netcfg" % filesdir, "/usr/lib/pm-utils/sleep.d/11netcfg")
