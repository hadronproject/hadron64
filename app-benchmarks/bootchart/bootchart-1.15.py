metadata = """
summary @ a startup graphing tool
homepage @ https://meego.gitorious.org/meego-developer-tools/bootchart
license @ GPL2
src_url @ http://foo-projects.org/~sofar/$name/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
rumtime @ sys-libs/glibc
"""

def prepare():
    patch("build.patch", level=1)

def install():
    installd()
