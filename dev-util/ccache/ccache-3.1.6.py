metadata = """
summary @ fast compiler cache
homepage @ http://ccache.samba.org/
license @ GPL-3
src_url @ http://samba.org/ftp/$name/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
common @ sys-libs/zlib
"""

prepare = lambda: rmdir("zlib")

def install():
    insexe("ccache", "/usr/bin/ccache")
    insfile("ccache.1", "/usr/share/man/man1/ccache.1")

    links = ('cc', 'gcc', 'g++', 'cpp', 'c++')

    for item in links:
        makesym("/usr/bin/ccache", "/usr/lib/ccache/bin/%s" % item)
        makesym("/usr/bin/ccache", "/usr/lib/ccache/bin/%s-%s" \
                % (get_env('HOST'), item))

