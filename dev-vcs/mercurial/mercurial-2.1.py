metadata = """
summary @ A scalable distributed SCM tool
homepage @ http://www.selenic.com/mercurial
license @ GPL
src_url @ http://www.selenic.com/mercurial/release/$fullname.tar.gz
arch @ ~x86
"""

# FIXME: zsh, bash, emacs and vim options will be added.

depends = """
common @ dev-lang/python:2.7
"""

get("python_utils")

standard_procedure = False

def install():
    python_utils_install()

    man_data = {"hg.1": "man1", "hgrc.5": "man5", "hgignore.5": "man5"}

    for key in man_data:
        insfile("doc/%s" % key, "/usr/share/man/%s/%s" % (man_data[key], key))

    insexe("contrib/hgk", "/usr/bin/hgk")
    insexe("%s/mercurial.profile" % filesdir, "/etc/profile.d/mercurial.sh")

    insfile("contrib/sample.hgrc", "/etc/mercurial/hgrc")
