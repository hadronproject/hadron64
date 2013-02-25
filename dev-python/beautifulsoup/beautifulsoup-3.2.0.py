metadata = """
summary @ A Python HTML/XML parser designed for quick turnaround projects like screen-scraping
homepage @ http://www.crummy.com/software/BeautifulSoup/index.html
license @ PSF
src_url @ http://www.crummy.com/software/BeautifulSoup/download/3.x/BeautifulSoup-$version.tar.gz
arch @ ~x86_64
slot @ 2
"""

# slot-2: this package for python2 series

srcdir = "BeautifulSoup-%s" % version
standard_procedure = False
get("main/python_utils")
install = lambda: python_utils_install()

