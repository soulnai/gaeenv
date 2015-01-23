__author__ = 'Eva Sokolyanskaya'

import pytest
import sys
import os
import glob
import pip
from gaeenv import requirements

def test_list_print(capsys):
    # given
    data = 'qwerty\nasdfg'
    file_name = 'c:\\temp\\test_file.txt'
    f = open(file_name, 'w')
    f.write(data)
    f.close()

     # execute
    requirements.list(file_name)
    out, err = capsys.readouterr()
    out = out.strip('\n')
    # os.remove(file_name)

    # verify
    assert out == data


def test_link_comparing_pip_installed():
    # given
    test_dir = "..\\..\\..\\test_dir\\"
    lib_dir = test_dir + 'lib_dir'
    path = os.path.dirname(__file__)
    print path
    print os.getcwd()
    os.chdir(path)
    print os.getcwd()
    os.chdir(os.path.dirname(os.getcwd()))
    os.chdir(os.path.dirname(os.getcwd()))
    print os.getcwd()


    req_file = glob.glob('requirements.txt')[0]

    # preparations
    if not os.path.isdir(test_dir):
        os.mkdir(test_dir)
    if not os.path.isdir(lib_dir):
        os.mkdir(lib_dir)

    # execute
    requirements.link(req_file, lib_dir)
    links = os.listdir(lib_dir)
    clean_links = map(lambda link: str(link.split('.')[0]), links)
    all_requirements_set = set(pip.req.parse_requirements(req_file, session=pip.download.PipSession()))
    requirements_name_set = map(lambda req: req.name.lower(), all_requirements_set)

    print "links:"
    print links
    print "requirements_name_set"
    print requirements_name_set

    # verify
    for req in requirements_name_set:
        if 'antlr' not in req:
            assert req in clean_links


def test_winlink_file():
    # given
    req_file = glob.glob('requirements.txt')[0]
    test_dir = 'test_dir\\'
    link_file = test_dir + 'req'

    if not os.path.isdir(test_dir):
        os.mkdir(test_dir)

    # execute
    requirements.make_symlink(req_file, link_file)

    # verify
    assert os.path.exists(link_file)

    # finalize
    os.remove(link_file)

@pytest.mark.skipif(os.name != 'nt', reason="test for Windows")
def test_winlink_dirrectory():
    # given
    test_dir = 'test_dir'
    link_file = os.path.join(test_dir, "test_link.l")

    if not os.path.isdir(test_dir):
        os.mkdir(test_dir)

    # execute
    requirements.make_symlink(test_dir, link_file)

    # verify
    assert os.path.exists(link_file)

    # finalize
    os.removedirs(link_file)
