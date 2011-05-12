metadata = """
summary @ LDAP suite of application and development tools
homepage @ http://www.openldap.org/
license @ custom
src_url @ ftp://ftp.openldap.org/pub/OpenLDAP/openldap-release/$fullname.tgz
arch @ ~x86
"""

def prepare():
    patch(level=1)


def configure():
    conf("--enable-crypt \
            --enable-dynamic \
            --with-threads \
            --enable-wrappers \
            --enable-spasswd \
            --with-cyrus-sasl \
            --disable-bdb \
            --disable-hdb")

def install():
    raw_install("DESTDIR=%s" % install_dir)
