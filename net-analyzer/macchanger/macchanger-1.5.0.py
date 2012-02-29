metadata = """
summary @ A small utility to change you NIC's MAC address
homepage @ http://ftp.gnu.org/gnu/macchanger
license @ GPL
src_url @ http://ftp.gnu.org/gnu/$name/$fullname.tar.gz
arch @ ~x86
"""

install = lambda: (installd(), insdoc("AUTHORS", "ChangeLog", "NEWS", "README"))
