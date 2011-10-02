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

import os
import glob

import lpms

# TODO:
# enable/with functions will be implemented
# http://sources.gentoo.org/cgi-bin/viewvc.cgi/gentoo-x86/eclass/cmake-utils.eclass?view=markup
# raw_install function needed.
# configure function will be improved

def cmake_utils_configure(*params, **kwargs):
    installdir = kwargs.get("installdir", install_dir)
    '''Configures the package with given parameters'''
    if os.access("CMakeLists.txt", os.F_OK):
        args = 'cmake -DCMAKE_INSTALL_PREFIX=%s \
                -DCMAKE_C_FLAGS="%s" \
                -DCMAKE_CXX_FLAGS="%s" \
                -DCMAKE_LD_FLAGS="%s" \
                -DCMAKE_BUILD_TYPE=RelWithDebInfo %s %s' % ("/usr", 
                        get_env("CFLAGS"),
                        get_env("CXXFLAGS"),
                        get_env("LDFLAGS"), " ".join(params), build_dir)
                
        if not system(args):
            error("configuration failed.")
            lpms.terminate()
    else:
        error("no configure script found for cmake.")
        lpms.terminate()

def cmake_utils_build(*params):
    '''Builds the package with given parameters'''
    # TODO: verbose and debug options will be added
    if not system("make %s" % " ".join(params)):
        error("building failed.")
        lpms.terminate()

def cmake_utils_install(*params, **kwargs):
    '''Installs the package with given parameters'''
    argument = kwargs.get("argument", "install")
    args = 'make DESTDIR="%(destdir)s" \
                 %(parameters)s \
                 %(argument)s' % {
                                     'destdir'      : install_dir,
                                     'parameters'   : " ".join(params),
                                     'argument'     : argument,
                                }
    
    if not system(args):
        error("installation failed.")
        lpms.terminate()
