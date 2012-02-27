metadata = """
summary @ Sophisticated and powerful Object-Relational DBMS
homepage @ http://www.postgresql.org/
license @ POSTGRESQL
src_url @ ftp://ftp.postgresql.org/pub/source/v$version/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
common @ dev-libs/libxml2 dev-lang/python:2.7 dev-lang/perl dev-libs/openssl
"""

def configure():
    raw_configure("--prefix=/usr", 
            "--mandir=/usr/share/man",
            "--datadir=/usr/share/postgresql",
            "--with-libxml", 
            "--with-openssl", 
            "--with-perl",
            "--with-python", 
            "--with-pam",
            "--with-system-tzdata=/usr/share/zoneinfo", 
            "--enable-nls",
            "--enable-thread-safety")

build = lambda: make("world")

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("COPYRIGHT")

    insexe("%s/postgresql.rcd" % filesdir, "/etc/rc.d/postgresql")
    insfile("%s/postgresql.confd" % filesdir, "/etc/conf.d/postgresql")
    insfile("%s/postgresql.pam" % filesdir, "/etc/pam.d/postgresql")
    insfile("%s/postgresql.logrotate" % filesdir,
            "/etc/logrotate.d/postgresql.d")

def post_install():
    if not isdir("/var/lib/postgres"):
        makedirs('/var/lib/postgres')
    
    # FIXME: user, group and password management must be done in lpms or a
    # helper library
    system("getent group postgres >/dev/null || groupadd -g 88 postgres")
    system("getent passwd postgres >/dev/null || useradd -c 'PostgreSQL user' -u 88 -g postgres -d '/var/lib/postgres' -s /bin/bash postgres")
    system("passwd -l postgres >/dev/null")

    notify("you should assign a password for postgres user.")
    notify("also you should run the following commands:")
    notify("su - postgresql")
    notify("initdb -D /var/lib/postgres/data/")
