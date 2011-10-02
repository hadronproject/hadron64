url_prefix = "http://www.cimitan.com/murrine/files"

metadata = """
summary @ Themes for the Murrine GTK+2 Cairo Engine
homepage @ Themes for the Murrine GTK+2 Cairo Engine
license @ GPL-2
src_url @ $url_prefix/MurrinaAquaIsh.tar.bz2 $url_prefix/MurrinaBlu-0.32.tar.gz
$url_prefix/MurrinaLoveGray.tar.bz2 $url_prefix/MurrineThemePack.tar.bz2 $url_prefix/MurrinaCandido.tar.gz
$url_prefix/MurrinaVerdeOlivo.tar.bz2 $url_prefix/MurrinaGilouche.tar.bz2
$url_prefix/MurrinaCream.tar.gz $url_prefix/NOX-svn-r22.tar.gz $url_prefix/MurrinaFancyCandy.tar.bz2
http://gnome-look.org/CONTENT/content-files/93558-Murreza.tar.gz
arch @ ~x86
"""

standard_procedure = False

depends = """
runtime @ >=x11-themes/gtk-engines-murrine-0.98.0
"""

def install():
    makedirs("/usr/share/themes")
    for item in ls(dirname(build_dir)):
        if item != fullname:
            copy(dirname(build_dir)+"/"+item, "/usr/share/themes")
