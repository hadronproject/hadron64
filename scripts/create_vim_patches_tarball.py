#!/usr/bin/env python2

import os
import sys

sys.path.insert(0, "/root/Projects/hadron/lpms")

from lpms.fetcher import URLFetcher

# A simple script to fetch vim patches and to create a patch set tarball.

patch_level = None
major_version = None

for cmd in sys.argv:
    if cmd.startswith("--major"):
        major_version = cmd.split("=")[1]
    elif cmd.startswith("--patch-level"):
        patch_level = cmd.split("=")[1]

if not patch_level or not major_version:
    print("invalid operation!")
    print("% ./create_vim_patches_tarball.py --major=7.3 --patch-level=390")
    exit()

vim_ftp= "ftp://ftp.vim.org/pub/vim/patches"
tarball = "vim-patches-%s.%s" % (major_version, patch_level)
target = os.path.join("/tmp", tarball)

if not os.path.isdir(target):
    os.makedirs(target)

def fetch_patches():
    for patch_num in xrange(1, int(patch_level)+1):
        url = "%s/%s/%s.%03d" % (vim_ftp, major_version, major_version, patch_num)
        URLFetcher().run([url], location=target)

def create_tarball():
    os.chdir("/tmp")
    os.popen("tar -czf %s %s" % (tarball + ".tar.gz", tarball))
    print("patch set created: /tmp/%s" % tarball+".tar.gz")

fetch_patches()
create_tarball()
