import os
import re
import sys
import inspect
import pip
import pip.req
from types import NoneType

from distutils.sysconfig import get_python_lib
from utils import logger


def winlink(source, link_name):
    '''symlink(source, link_name)
       Creates a symbolic link pointing to source named link_name'''

    import ctypes
    csl = ctypes.windll.kernel32.CreateSymbolicLinkW
    csl.argtypes = (ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_uint32)
    csl.restype = ctypes.c_ubyte

    flags = 0
    if source is not None and os.path.isdir(source):
        flags = 1
    if csl(link_name, source, flags) == 0:
        raise ctypes.WinError()


def list(req_file):
    requirements = pip.req.parse_requirements(req_file)

    for requirement in requirements:
        print requirement.req


def link(req_file, lib_dir):
    all_requirements_set = set(pip.req.parse_requirements(req_file) )
    all_installed_packages__set = set(pip.get_installed_distributions())

    make_package_from_links_folder(lib_dir)

    check_if_all_packages_has_names(all_requirements_set)

    for package in all_installed_packages__set:
        for requirement in all_requirements_set:
            if requirement.req.key in package.key:
                create_symlink_for_package_content(package, lib_dir)

def make_package_from_links_folder(lib_dir):
    """Creates folder where symlinks will be stored. And adds __init__.py for it.
    :param lib_dir: Path to folder where symlinks will be stored.
    """
    if not os.path.exists(lib_dir):
        os.makedirs(lib_dir)

    with open(os.path.join(lib_dir, '__init__.py'), 'wb') as f:
        f.write((
                "# Auto generated by gaeenv\n"
                "import sys\n"
                "import os\n"
                "sys.path.insert(0, os.path.dirname(__file__))\n"))


def get_package_folders_names(package):
    return package._get_metadata("top_level.txt")


def make_symlink(pkg_path, sym_path):
    if os.name == 'nt':
        winlink(pkg_path, sym_path)
    else:
        os.symlink(pkg_path, sym_path)


def check_if_all_packages_has_names(all_requirements_set):
    for requirement in all_requirements_set:
        if isinstance(requirement.req, NoneType):
            print("Requirement {} have not assigned package name and will not be linked. Please assign package name.")\
                .format(str(requirement))
            exit()


def create_symlink_for_package_content(package, lib_dir):
    package_folders = get_package_folders_names(package)
    for folder_name in package_folders:
        pkg_path = os.path.join(package.location, folder_name)
        pkg_name = folder_name
        is_file = (not os.path.exists(pkg_path) and os.path.exists(pkg_path + '.py'))
        if is_file:
            """
            Check if item that we want to link is a folder or a file. So we can build right link to it.
            """
            pkg_path = pkg_path +'.py'
            pkg_name = pkg_name + '.py'
        if not os.path.exists(pkg_path):
            continue
        sym_path = os.path.join(lib_dir, pkg_name)
        print "Package {} linking into {}".format(str(pkg_path), str(sym_path))
        make_symlink(str(pkg_path), sym_path)