metadata = """
summary @ Sources for time zone and daylight saving time data
homepage @ http://www.twinsun.com/tz/tz-link.htm
license @ BSD public-domain
src_url @ ftp://elsie.nci.nih.gov/pub/tzdata$version.tar.gz http://pkgs.fedoraproject.org/lookaside/pkgs/tzdata/tzcode2011i.tar.gz/cf7f4335b7c8682899fa2814e711c1b2/tzcode2011i.tar.gz
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
    cd(dirname(build_dir))
    raw_install('DESTDIR=%s install' % install_dir)
    rmfile("/usr/share/zoneinfo/localtime")
