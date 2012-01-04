metadata = """
summary @ Sources for time zone and daylight saving time data
homepage @ http://www.twinsun.com/tz/tz-link.htm
license @ BSD public-domain
src_url @ http://tx-us.lunar-linux.org/lunar/mirrors/tzdata2011n.tar.gz http://tx-us.lunar-linux.org/lunar/mirrors/tzcode2011i.tar.gz
arch @ ~x86
"""

standard_procedure = False

def prepare():
    cd(dirname(build_dir))
    patch(level=1)

def build():
    cd(dirname(build_dir))
    make()

def install():
    cd("..")
    raw_install('DESTDIR=%s' % install_dir)
    rmfile("/usr/share/zoneinfo/localtime")
