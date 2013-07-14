metadata = """
summary @ Linux ACPI client providing battery, AC power, and thermal readings
homepage @ http://sourceforge.net/projects/acpiclient
license @ GPL2
src_url @ http://downloads.sourceforge.net/acpiclient/$fullname.tar.gz
arch @ ~x86_64
"""

def configure():
    conf(
    "--disable-dependency-tracking")

def install():
    make("DESTDIR=%s install" % install_dir)
    insdoc("AUTHORS", "ChangeLog")
