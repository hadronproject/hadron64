metadata = """
summary @ A high-level Python Web framework.
homepage @ http://www.djangoproject.com/
license @ BSD
src_url @ http://media.djangoproject.com/releases/1.3/Django-$version.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ dev-lang/python
build @ dev-lang/python
"""

srcdir = "Django-%s" % version

standard_procedure = False

def install():
    system("python setup.py install --root=%s --optimize=1" % install_dir)

    insfile("extras/django_bash_completion", "/etc/bash_completion.d/django")

    insdoc("LICENSE")
