# Copyright 2009 - 2011 Burak Sezer <purak@hadronproject.org>
#
# This file is part of main repository
#
# main repository is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# main repository is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with main repository.  If not, see <http://www.gnu.org/licenses/>.

# KDE4-related build operations

get("main/fdo_mime", "main/cmake_utils", "main/extract_utils")

primary_library = "kde4_utils"

# variable checks
try:
    subdir
except NameError:
    subdir = ""

try:
    source_archive
except NameError:
    source_archive = None

def kde4_utils_extract():
    if source_archive:
        tar_extract("%s" % source_archive)
    else:
        for item in extract_plan:
            tar_extract(basename(item))

# Functions
def kde4_utils_prepare():
    makedirs("build")

def kde4_utils_configure():
    cd("build")
    cmake_conf(sourcedir=build_dir+"/%s" % subdir)

def kde4_utils_build():
    cd("build")
    make()

def kde4_utils_install():
    cd("build/%s" % subdir)
    installd()

def kde4_utils_post_install():
    xdg_icon_resource()

