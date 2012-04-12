metadata = """
summary @ Sources for time zone and daylight saving time data
homepage @ http://www.twinsun.com/tz/tz-link.htm
license @ BSD public-domain
src_url @ http://www.iana.org/time-zones/repository/releases/tzdata2012c.tar.gz 
http://www.iana.org/time-zones/repository/releases/tzcode2012b.tar.gz
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
