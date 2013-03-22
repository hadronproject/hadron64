metadata = """
summary @ A persistent caching system, key-value and data structures database.
homepage @ http://redis.io/
license @ BSD
src_url @ http://redis.googlecode.com/files/$fullname.tar.gz
arch @ ~x86_64
"""

# TODO:
# * jemalloc
# * tcmalloc
# I couldnt add these options to redis package because of lpms has no a feature 
# that handles option option/package conflict mix.

def build():
    make("MALLOC=libs")
    sed("-i 's|# bind 127.0.0.1|bind 127.0.0.1|' redis.conf")

def install():
    makedirs("/usr/bin")
    raw_install("INSTALL_BIN='/usr/bin' PREFIX=/usr")
    insdoc("COPYING")
    insfile("%s/redis.service" % filesdir, \
            "/usr/lib/systemd/system/redis.service")
    insfile("%s/redis.logrotate" % filesdir, \
            "/etc/logrotate.d/redis")
    sed("-i 's|daemonize no|daemonize yes|;s|dir \./|dir /var/lib/redis/|;s|logfile stdout|logfile /var/log/redis.log| ' redis.conf")
    insfile("redis.conf", "/etc/redis.conf")
