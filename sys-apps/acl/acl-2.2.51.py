metadata = """
summary @ Access control list utilities, libraries and headers
homepage @ http://savannah.nongnu.org/projects/acl
license @ LGPL-2
src_url @ http://mirrors.zerg.biz/nongnu/$name/$fullname.src.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ >=sys-apps/attr-2.4.46
"""

def configure():
    variables = {"INSTALL_USER": "root",
        "INSTALL_GROUP": "root"}
    for key in variables:
        export(key, variables[key])
    conf()

def install():
    raw_install("DIST_ROOT='%s' install install-lib install-dev" % install_dir)
