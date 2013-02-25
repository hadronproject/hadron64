metadata = """
summary @ An enhanced Interactive Python shell.
homepage @ http://ipython.scipy.org/
license @ custom
src_url @ http://ipython.scipy.org/dist/$version/$fullname.tar.gz
arch @ ~x86_64
"""

standard_procedure = False

get("python_utils")

def install():
    python_utils_install()
    #system("python setup.py install --prefix=/usr --root=%s" % install_dir)
