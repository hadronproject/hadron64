get("python_utils")

metadata = """
summary @ HARMAN is a free software that can be used to merge, split and cut PDF documents.
homepage @ http://www.istihza.com
license @ GPL-3
src_url @ http://istihza.com/$name/$name-$version/anakaynak/$name-$version.tar.gz
"""

def post_install():
    notify("Packaged by Burak Sezer")
