metadata = """
summary @ Compilation of tools to manage Hadron GNU/Linux better.
homepage @ http://www.hadronproject.org/
license @ GPL-2
arch @ ~x86
"""

depends = """
runtime @ sys-apps/lpms dev-lang/perl sys-apps/sed sys-apps/grep
"""

standard_procedure = False

def install():
    insexe("%s/revdep-rebuild" % filesdir, "/usr/bin/revdep-rebuild")
    insexe("%s/clear-lpms-cache" % filesdir, "/usr/bin/clear-lpms-cache")
