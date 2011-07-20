metadata = """
summary @ Quirks data for pm-utils
homepage @ http://pm-utils.freedesktop.org/wiki/
license @ GPL
src_url @ http://pm-utils.freedesktop.org/releases/$fullname.tar.gz
arch @ ~x86
"""

srcdir = "video-quirks"

standard_procedure = False

def install():
    makedirs("/usr/lib/pm-utils/video-quirks")

    insinto("*.quirkdb", "/usr/lib/pm-utils/video-quirks")

