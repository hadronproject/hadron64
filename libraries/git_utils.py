# Copyright 2009 - 2012 Burak Sezer <purak@hadronproject.org>
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

from lpms import shelltools

def copy_to_build_dir(source):
    '''Copy the cloned or updated local git repository to build directory'''
    copytree(source, build_dir)

def git_clone(*params, **kwargs):
    '''Clone or update a local git repository'''
    if not 'subdir' in kwargs:
        raise BuiltinError("you must give subdir parameter.")
    subdir = kwargs['subdir']
    clone_dir = joinpath(src_cache, fullname)
    shelltools.makedirs(clone_dir)
    current_dir = pwd()
    cd(clone_dir)
    if isdir(subdir):
        if not isempty(subdir):
            cd(subdir)
            notify("updating %s" % subdir)
            notify("running git pull %s" % " ".join(params))
            if not shelltools.system("git pull", sandbox=False):
                raise BuiltinError("git pull failed")
            copy_to_build_dir(joinpath(clone_dir, subdir))
            cd(current_dir)
            return True
    notify("cloning into %s" % pwd())
    notify("running git clone %s" % " ".join(params))
    if not shelltools.system("git clone "+" ".join(params), sandbox=False):
        raise BuiltinError("git clone failed")
    copy_to_build_dir(joinpath(clone_dir, subdir))
    cd(current_dir)
    return True
