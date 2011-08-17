metadata ="""
summary @ ENCA detects the character coding of a file and converts it if desired
homepage @ http://gitorious.org/enca
license @ GPL-2
src_url @ http://dl.cihar.com/$name/$name-$version.tar.bz2
options @ doc recode
arch @ ~x86
"""

opt_build = """
recode @ app-text/recode
"""

opt_runtime = """
recode @ app-text/recode
"""

def configure():
    raw_configure("--prefix=/usr",
            "--enable-external",
            config_enable("doc", "gtk-doc"),
            config_with("recode", "librecode"))

def install():
    raw_install("DESTDIR=%s install" % install_dir)
    
 
