metadata = """
summary @  A comprehensive design and management interface for PostgreSQL database
homepage @ http://www.pgadmin.org
license @ POSTGRESQL
src_url @ ftp://ftp.de.postgresql.org/pub/packages/databases/PostgreSQL/pgadmin3/release/v$version/src/pgadmin3-$version.tar.gz
arch @ ~x86
"""

depends = """
common @ x11-libs/wxgtk >=dev-libs/libxml2-2.6.18 >=dev-libs/libxslt-1.1 dev-db/postgresql
"""

def install():
    installd()
    insfile("i18n/pgadmin3.lng", "/usr/share/pgadmin3/i18n")
    insdoc("LICENSE")
    insfile("pgadmin/include/images/pgAdmin3.ico", "/usr/share/pgadmin3/pixmaps/pgAdmin3.ico")
    insfile("%s/pgadmin3.desktop" % filesdir, "/usr/share/applications/pgadmin3.desktop")


