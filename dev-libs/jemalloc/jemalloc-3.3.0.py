metadata = """
summary @ Jemalloc is a general-purpose scalable concurrent allocator
homepage @ http://www.canonware.com/jemalloc/
license @ BSD
src_url @ http://www.canonware.com/download/$name/$fullname.tar.bz2
options @ debug stats static-libs
arch @ ~x86_64
"""

def configure():
    conf(config_enable("debug"), config_enable("stats"))

def install():
    installd()
    if not opt("static-libs"):
        rmfile("/usr/lib/libjemalloc_pic.a")
        rmfile("/usr/lib/libjemalloc.a")

