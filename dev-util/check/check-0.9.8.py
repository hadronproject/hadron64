metadata = """
summary @ A unit test framework for C
homepage @ http://sourceforge.net/projects/check/
license @ LGPL-2.1
src_url @ http://garr.dl.sourceforge.net/project/check/check/$version/$fullname.tar.gz
arch @ ~x86
"""

# TODO: add subunit option

def configure():
    conf("--disable-dependency-tracking")

def install():
    installd()
    insdoc("AUTHORS", "*ChangeLog*", "NEWS", "README", "THANKS", "TODO")

