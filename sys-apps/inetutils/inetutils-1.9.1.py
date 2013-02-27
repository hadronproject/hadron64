metadata = """
summary @ GNU common networking utilities and servers
homepage @ https://www.gnu.org/software/inetutils/
license @ GPL-3
src_url @ ftp://ftp.gnu.org/gnu/$name/$fullname.tar.gz
options @ ipv6 ncurses pam tcpd
arch @ ~x86_64
"""

opt_common = """
ncurses @ sys-libs/ncurses
pam @ sys-libs/pam
tcpd @ sys-apps/tcp-wrappers
"""

def prepare():
    patch(level=1)

def configure():
    conf("--without-krb4",
    "--without-krb5",
    "--disable-encryption",
    "--disable-hostname",
    "--disable-ifconfig",
    "--disable-logger",
    "--disable-tftpd",
    config_enable("ipv6"),
    config_enable("ncurses"),
    config_with("pam"),
    config_with("tcpd", "wrap"))

install = lambda: installd()

