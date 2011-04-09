metadata = """
summary @ Sources for time zone and daylight saving time data
homepage @ http://www.twinsun.com/tz/tz-link.htm
license @ BSD public-domain
src_url @ ftp://elsie.nci.nih.gov/pub/tzdata$version.tar.gz ftp://elsie.nci.nih.gov/pub/tzcode$version.tar.gz
arch @ ~x86
"""

standart_procedure = False

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
