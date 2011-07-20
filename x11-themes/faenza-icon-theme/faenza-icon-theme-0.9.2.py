metadata = """
summary @ A scalable icon theme called Faenza
homepage @ http://code.google.com/p/faenza-icon-theme/
license @ GPL3
src_url @ http://faenza-icon-theme.googlecode.com/files/$name_$version.tar.gz
arch @ ~x86
"""

standard_procedure = False

def install():
    cd("..")
    for i in ("Faenza",  "Faenza-Dark",  "Faenza-Darker",  "Faenza-Darkest"):
        copytree(i, "/usr/share/icons/%s" % i)

    insdoc("AUTHORS", "ChangeLog", "README")
