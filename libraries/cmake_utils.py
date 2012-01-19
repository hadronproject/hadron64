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
# raw_install function needed.

def cmake_decide(function_name):
    case = "".join(function_name.__name__.split("cmake_config_")).upper()
    def wrapper(cmake_option):
        if opt(cmake_option):
            if case != "DISABLE":
                return "-D"+case+"_"+cmake_option.upper()+"=ON"
        return "-D"+case+"_"+cmake_option.upper()+"=OFF"
    return wrapper

@cmake_decide
def cmake_config_enable(cmake_option):
    '''Returns -DENABLE_FOO=ON option is enabled, else -DENABLE_FOO=OFF'''
    return cmake_option

@cmake_decide
def cmake_config_with(cmake_option):
    '''Returns -DWITH_FOO=ON option is enable, else -DWITH_FOO=OFF'''
    return cmake_option

@cmake_decide
def cmake_config_disable(cmake_option):
    '''Returns -DDISABLE_FOO=OFF option is enable, else -DDISABLE_FOO=ON'''
    return cmake_option

@cmake_decide
def cmake_config_no(cmake_option):
    '''Returns -DNO_FOO=OFF option is enable, else -DNO_FOO=ON'''
    return cmake_option

@cmake_decide
def cmake_config_want(cmake_option):
    '''Returns -DWANT_FOO=ON option is enable, else -DWANT_FOO=OFF'''
    return cmake_option

@cmake_decide
def cmake_config_build(cmake_option):
    '''Returns -DBUILD_FOO=ON option is enable, else -DBUILD_FOO=OFF'''
    return cmake_option

@cmake_decide
def cmake_config_have(cmake_option):
    '''Returns -DHAVE_FOO=ON option is enable, else -DHAVE_FOO=OFF'''
    return cmake_option

@cmake_decide
def cmake_config_use(cmake_option):
    '''Returns -DUSE_FOO=ON option is enable, else -DUSE_FOO=OFF'''
    return cmake_option

@cmake_decide
def cmake_config(cmake_option):
    '''Returns -DFOO=ON option is enable, else -DFOO=OFF'''
    return cmake_option

def cmake_conf(*params, **kwargs):
    '''Configures the package with given parameters'''
    installdir = kwargs.get("installdir", "/usr")
    sourcedir = kwargs.get("sourcedir", None)
    cmakelist = "CMakeLists.txt"
    if sourcedir:
        cmakelist = os.path.join(sourcedir, "CMakeLists.txt")
    if os.access(cmakelist, os.F_OK):
        if not sourcedir:
            args = 'cmake -DCMAKE_INSTALL_PREFIX=%s \
                    -DCMAKE_C_FLAGS="%s" \
                    -DCMAKE_CXX_FLAGS="%s" \
                    -DCMAKE_LD_FLAGS="%s" \
                    -DCMAKE_BUILD_TYPE=RelWithDebInfo %s %s' % (installdir, 
                            get_env("CFLAGS"),
                            get_env("CXXFLAGS"),
                            get_env("LDFLAGS"), " ".join(params), build_dir)
        else:
            args = 'cmake %s -DCMAKE_INSTALL_PREFIX=%s \
                    -DCMAKE_C_FLAGS="%s" \
                    -DCMAKE_CXX_FLAGS="%s" \
                    -DCMAKE_LD_FLAGS="%s" \
                    -DCMAKE_BUILD_TYPE=RelWithDebInfo %s %s' % (sourcedir, installdir, 
                            get_env("CFLAGS"),
                            get_env("CXXFLAGS"),
                            get_env("LDFLAGS"), " ".join(params), build_dir)
    else:
        error("no configure script found for cmake.")
        lpms.terminate()

    if not system(args):
        error("configuration failed.")
        lpms.terminate()

def cmake_utils_configure():              
    '''Runs cmake command with standard parameters'''
    cmake_conf()

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
