metadata = """
summary @ Python sandboxing module, formerly catbox
homepage @ http://hadronproject.org
license @ GPL-2
src_url @ http://hadronproject.org/distfiles/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
common @ dev-lang/python
"""

standard_procedure = False

get("python_utils")

def install():
    export("PYTHONDONTWRITEBYTECODE", "1")
    python_utils_install()
    insdoc("README.old", "AUTHORS")
