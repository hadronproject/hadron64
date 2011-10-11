metadata = """
summary @ DocBook XML catalog auto-updater
homepage @ http://www.gentoo.org/
license @ GPL2
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc
"""

standard_procedure = False

def install():
	insexe("%s/build-docbook-catalog" % filesdir, "/usr/bin/build-docbook-catalog")

