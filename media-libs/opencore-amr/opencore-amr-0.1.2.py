metadata = """
summary @ Open source implementation of the Adaptive Multi Rate (AMR) speech codec 
homepage @ http://opencore-amr.sourceforge.net/ 
license @ APACHE 
src_url @ http://downloads.sourceforge.net/sourceforge/$name/$name-$version.tar.gz 
arch @ ~x86
"""

depends = """
runtime @ sys-devel/gcc
"""

def configure():
    conf(
    "--disable-dependency-tracking",
    "--disable-static")

def install():
	raw_install("DESTDIR=%s" % install_dir)

	insdoc("AUTHORS", "ChangeLog", "README")

