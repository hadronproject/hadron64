metadata = """
summary @ ACPI client - replacement for apm tool
homepage @ http://sourceforge.net/projects/acpitool/
license @ GPL
src_url @ http://downloads.sourceforge.net/sourceforge/acpitool/$fullname.tar.bz2
arch @ ~x86_64
"""

def install():
    make("DESTDIR=%s install" % install_dir)
    insdoc("AUTHORS", "ChangeLog", "README", "TODO")
