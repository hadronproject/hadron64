metadata = """
summary @ Convert xml to many other formats
homepage @ http://cyberelk.net/tim/software/xmlto/
license @ GPL
src_url @ https://fedorahosted.org/releases/x/m/xmlto/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ dev-libs/libxslt dev-perl/Test-Pod dev-perl/YAML-Syck
build @ app-text/docbook-xsl-stylesheets
"""
