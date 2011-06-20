# waf utils for lpms

import lpms

from lpms import out

export("JOBS", get_env("JOBS")[2:])

def waf_configure(*args):
    if not system("./waf configure --prefix=/usr %s" % " ".join(args)):
        out.error("waf configure failed.")
        lpms.terminate()

def waf_build(*args, **kwargs):
    if "j" in kwargs:
        export("JOBS", kwargs["j"])

    if not system("./waf build"):
        out.error("waf build failed.")
        lpms.terminate()

def waf_install():
    if not system("./waf install --destdir=%s" %  install_dir):
        out.error("waf install failed.")
        lpms.terminate()
