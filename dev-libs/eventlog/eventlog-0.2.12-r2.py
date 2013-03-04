metadata = """
summary @ API to format and send structured log messages
homepage @ http://www.balabit.com/support/community/products/
license @ BSD
src_url @ http://www.balabit.com/downloads/files/syslog-ng/open-source-edition/3.4.1/source/eventlog_0.2.12+20120504+1700.tar.gz 
arch @ ~x86_64
"""

srcdir='eventlog-0.2.12+20120504+1700'

def install():
    raw_install("DESTDIR=%s install" % install_dir)
