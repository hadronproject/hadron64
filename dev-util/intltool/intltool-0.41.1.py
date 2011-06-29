metadata = """
summary @ The internationalization tool collection
homepage @ https://edge.launchpad.net/intltool
license @ GPL
src_url @ http://edge.launchpad.net/intltool/trunk/$version/+download/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ dev-perl/XML-Parser
"""

def configure():
    system('perl -e "require XML::Parser"')
    conf()

def install():
    raw_install("DESTDIR=%s" % install_dir)

