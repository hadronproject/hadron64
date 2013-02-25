metadata = """
summary @ YAML 1.1 parser and emitter written in C
homepage @ http://pyyaml.org/wiki/LibYAML
license @ MIT
src_url @ http://pyyaml.org/download/$name/yaml-$version.tar.gz
arch @ ~x86_64
"""

srcdir = "yaml-%s" % version

install = lambda: (installd(), insdoc("LICENSE"))
