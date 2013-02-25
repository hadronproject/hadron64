metadata = """
summary @ lightweight HTTP server and IMAP/POP3 proxy server
homepage @ http://nginx.org
license @ as-is BSD BSD-2 GPL-2 MIT
src_url @ http://nginx.org/download/nginx-$version.tar.gz
arch @ ~x86_64
options @ ipv6 debug ssl pcre http-cache nginx_modules_http_access nginx_modules_http_auth_basic nginx_modules_http_autoindex nginx_modules_http_browser nginx_modules_http_charset nginx_modules_http_empty_gif nginx_modules_http_fastcgi nginx_modules_http_geo nginx_modules_http_gzip nginx_modules_http_limit_req nginx_modules_http_limit_zone nginx_modules_http_map nginx_modules_http_memcached nginx_modules_http_proxy nginx_modules_http_referer nginx_modules_http_rewrite nginx_modules_http_scgi nginx_modules_http_ssi nginx_modules_http_split_clients nginx_modules_http_upstream_ip_hash nginx_modules_http_userid nginx_modules_http_uwsgi nginx_modules_http_addition nginx_modules_http_dav nginx_modules_http_degradation nginx_modules_http_flv nginx_modules_http_geoip nginx_modules_http_gzip_static nginx_modules_http_image_filter nginx_modules_http_mp4 nginx_modules_http_perl nginx_modules_http_random_index nginx_modules_http_realip nginx_modules_http_secure_link nginx_modules_http_stub_status nginx_modules_http_sub nginx_modules_http_xslt nginx_modules_mail_imap nginx_modules_mail_pop3 nginx_modules_mail_smtp nginx_modules_http_upload_progress nginx_modules_http_headers_more nginx_modules_http_passenger nginx_modules_http_push nginx_modules_http_cache_purge nginx_modules_http_upload nginx_modules_http_slowfs_cache
"""

depends = """
runtime @ sys-libs/glibc
"""

opt_runtime = """
pcre @ >=dev-libs/pcre-4.2
ssl @ dev-libs/openssl
http-cache @ dev-libs/openssl
nginx_modules_http_gzip @ sys-libs/zlib
nginx_modules_http_geo @ dev-libs/GeoIP
nginx_modules_http_gzip_static @ sys-libs/zlib
nginx_modules_http_image_filter @ media-libs/gdjpeg media-libs/gdpng
nginx_modules_http_perl @  >=dev-lang/perl-5.8
nginx_modules_http_rewrite @ >=dev-libs/pcre-4.2
nginx_modules_http_secure_link @ dev-libs/openssl
nginx_modules_http_xslt @ dev-libs/libxml2 dev-libs/libxslt
"""

def prepare():
    sed("""-i -e "s/\<user\s\+\w\+;/user http;/g" conf/nginx.conf""")

def configure():
    myconf = ""
    mail_enabled = 0
    http_enabled = 0
    
    if opt("aio"):
        myconf += " --with-file-aio --with-aio_module "
    if opt("debug"):
        myconf += " --with-debug "
    if opt("ipv6"):
        myconf += " --with-ipv6 "
    if opt("pcre"):
        myconf += " --with-pcre "
    
    #standards
    for modsta in ("http_access", "http_auth_basic",
            "http_autoindex", "http_browser",
            "http_charset", "http_empty_gif", 
            "http_fastcgi", "http_geo", "http_gzip", 
            "http_limit_req", "http_limit_zone", 
            "http_map", "http_memcached", "http_proxy", 
            "http_referer", "http_rewrite", "http_scgi",
            "http_ssi", "http_split_clients", 
            "http_upstream_ip_hash", "http_userid", "http_uwsgi"):
        if not opt("nginx_modules_%s" % modsta):
            myconf += " --without-%s_module " % modsta
        else:
            http_enabled = 1

    #optionals    
    for modop in ("http_gzip_static", "http_image_filter",
            "http_perl", "http_geoip",
            "http_secure_link", "http_xslt",
            "http_addition", "http_dav",
            "http_degradation", "http_flv",
            "http_mp4", "nginx_modules_http_random_index",
            "http_random_realip", "http_random_stub_status",
            "http_random_stub_sub", "http_perl"):
        if opt("nginx_modules_%s" % modop ):
            myconf += " --with-%s_module " % modop
            http_enabled = 1

    #mail
    for modmail in ("mail_imap", "mail_pop3", "mail_smtp"):
        if opt("nginx_modules_%s" % modmail):
            mail_enabled = 1
        else:
            myconf += " --without-%s_module " % modmail

    if http_enabled == 1:
        if not opt("http-cache"):
            myconf += " --without-http-cache "
        if opt("ssl"):
            myconf += " --with-http_ssl_module "
    else:
        myconf += " --without-http --without-http-cache "

    if mail_enabled == 1:
        myconf += " --with-mail "
        if opt("ssl"):
            myconf += " --with-mail_ssl_module "


    raw_configure(
    "--prefix=/usr",
    "--sbin-path=/usr/sbin/nginx",
    "--conf-path=/etc/nginx/nginx.conf",
    "--error-log-path=/var/log/nginx/error.log",
    "--pid-path=/var/run/nginx.pid",
    "--user=http",
    "--group=http",
    "--lock-path=/var/lock/nginx.lock",
    "--http-log-path=/var/log/nginx/access.log",
    "--http-client-body-temp-path=/var/spool/nginx/client",
    "--http-proxy-temp-path=/var/spool/nginx/proxy",
    "--http-fastcgi-temp-path=/var/spool/nginx/fastcgi",
    "--http-scgi-temp-path=/var/spool/nginx/scgi",
    "--http-uwsgi-temp-path=/var/spool/nginx/uwsgi", myconf)

def build():
    export("LANG", "C")
    export("LC_ALL", "C")
    make()

def install():
    insdoc("CHANGES*", "README")
    insfile("%s/nginx.logrotate" % filesdir, "/etc/logrotate.d/nginx")
    raw_install("DESTDIR=%s" % install_dir)
    insexe("%s/nginx" % filesdir, "/etc/rc.d/nginx")
    insfile("%s/nginx.confd" % filesdir, "/etc/conf.d/nginx")

#TODO: 3rd party plugins could be added http://gpo.zugaina.org/AJAX/Ebuild/2428387/View
