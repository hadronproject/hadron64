metadata = """
summary @ A PostgreSQL database adapter for the Python programming language.
homepage @ http://initd.org/psycopg/
license @ LGPL-3
src_url @ http://initd.org/psycopg/tarballs/PSYCOPG-2-4/psycopg2-$version.tar.gz
arch @ ~x86_64
"""

depends = """
common @ dev-lang/python:2* dev-db/postgresql
"""

get("python_utils")

standard_procedure = False

def install():
    python_utils_install()
