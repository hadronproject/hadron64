metadata = """
summary @ Sophisticated and powerful Object-Relational DBMS
homepage @ http://www.postgresql.org/
license @ POSTGRESQL
src_url @ ftp://ftp.postgresql.org/pub/source/v$version/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
common @ dev-libs/libxml2 dev-lang/python:2.7 dev-lang/perl dev-libs/openssl
"""

def prepare():
    patch("postgresql-run-socket.patch", level=1)

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

    insfile("%s/postgresql.tmpfiles.conf" % filesdir, \
            "/usr/lib/tmpfiles.d/postgresql.conf")
    insfile("%s/postgresql.service" % filesdir, \
            "/usr/lib/systemd/system/postgresql.service")
    insfile("%s/postgresql.pam" % filesdir, \
            "/etc/pam.d/postgresql")
    insfile("%s/postgresql.logrotate" % filesdir,
            "/etc/logrotate.d/postgresql")
    insexe("%s/postgresql-check-db-dir" % filesdir, \
            "/usr/bin/postgresql-check-db-dir")

def post_install():
    if not isdir("/var/lib/postgres"):
        makedirs('/var/lib/postgres')
    
    # FIXME: Crappy hacks for user management
    # user, group and password management must be done in lpms or a
    # helper library
    system("groupadd -g 88 postgres")
    system("useradd -c 'PostgreSQL user' -u 88 -g postgres -d '/var/lib/postgres' -s /bin/bash postgres")
    system("passwd -l postgres")
    system("systemd-tmpfiles --create postgresql.conf")

    notify("You should assign a password for postgres user.")
    notify("Also you should run the following commands:\n")
    notify("Create the data directory (acordingly with the PGROOT variable set before in the config file)")
    notify("# mkdir /var/lib/postgres/data")
    notify("Set /var/lib/postgres/data ownership to user 'postgres'")
    notify("# chown -c postgres:postgres /var/lib/postgres/data\n")
    
    notify("As user 'postgres' start the database")
    notify("su - postgres")
    notify("initdb -D /var/lib/postgres/data/\n")
    
    notify("Start PostgreSQL ")
    notify("# systemctl start postgresql\n")

    notify("Add PostgreSQL to the list of daemons that start on system startup")
    notify("# systemctl enable postgresql\n")
