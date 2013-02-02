metadata = """
summary @ A ptrace() wrapper library
homepage @ http://dev.exherbo.org/~alip/pinktrace/
license @ as-is
src_url @ http://dev.exherbo.org/~alip/$name/release/$fullname.tar.bz2
options @ ipv6 python ruby
arch @ ~x86_64
"""

depends = """
build @ dev-util/check
"""

#opt_common = """
#python @ dev-lang/python:2.7
#ruby @ dev-lang/ruby
#"""

# TODO:
# * python-doc, ruby-doc, doxygen, haskell options are going to added

def configure():
    conf("--enable-easy",
            #config_enable("python"),
            #config_enable("python-doc"),
            #config_enable("ruby-doc"),
            config_enable("ipv6"))

install = lambda: (installd(), insdoc("COPYRIGHT"))
