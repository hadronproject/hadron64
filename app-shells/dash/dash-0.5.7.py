metadata = """
summary @ A POSIX compliant shell that aims to be as small as possible
homepage @ http://gondor.apana.org.au/~herbert/dash/
license @ BSD
src_url @ http://gondor.apana.org.au/~herbert/dash/files/$fullname.tar.gz
arch @ ~x86
"""

def install():
    installd()
    insdoc("COPYING")
