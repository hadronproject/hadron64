metadata = """
summary @ Python sandboxing module, formerly catbox
homepage @ http://hadronproject.org
license @ GPL-2
arch @ ~x86_64
"""

depends = """
common @ dev-lang/python
"""

standard_procedure = False

get("python_utils", "git_utils")

def prepare():
    git_clone("git://github.com/Pardus-Linux/catbox.git", subdir=name)

def install():
    cd("catbox")
    export("PYTHONDONTWRITEBYTECODE", "1")
    python_utils_install()
    insdoc("README.old", "AUTHORS")
