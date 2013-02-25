metadata = """
summary @ Utility to fix your .la files
homepage @ http://www.gentoo.org/
license @ MIT
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc app-shells/bash sys-apps/findutils
"""

standard_procedure = False

def install():
    insexe("%s/lafilefixer-0.5" % filesdir, "/usr/bin/lafilefixer")

    notify("""
    *************************************************************************
    This simple utility will fix your .la files to not point to other .la files.
    This is desirable because it will ensure your packages are not broken when
    .la files are removed from other packages.
    For most uses, lafilefixer --justfixit should 'just work'. This will
    recurse through the most commonly used library folders and fix all .la
    files it encounters.

    Read lafilefixer --help for a full description of all options.
    *************************************************************************""")
