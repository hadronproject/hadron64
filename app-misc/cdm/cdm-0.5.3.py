metadata = """
summary @ The Console Display Manager
homepage @ http://cdm.ghost1227.com/X11
license @ GPL
src_url @ http://cdm.ghost1227.com/repo/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ dev-util/dialog
"""

reserve_files = ['/etc/cdmrc']

standard_procedure = False

def install():
    insfile("src/cdmrc", "/etc/cdmrc")
    insinto("src/xinitrc*", "/usr/share/cdm")
    insexe("src/cdm", "/usr/bin/cdm")
    insexe("src/zzz-cdm-profile.sh", "/etc/profile.d/zzz-cdm-profile.sh")
    insinto("src/themes", "/usr/share/cdm/")

def post_install():
    notify("For configuration information, check: https://wiki.archlinux.org/index.php/CDM")
