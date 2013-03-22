metadata = """
summary @ Implementation for atomic memory update operations
homepage @ http://www.hpl.hp.com/research/linux/atomic_ops/
license @ MIT boehm-gc GPL-2+
src_url @ http://www.hpl.hp.com/personal/Hans_Boehm/gc/gc_source/gc-$version.tar.gz
arch @ ~x86_64
"""

srcdir = "gc-7.2"

install = lambda: installd()
