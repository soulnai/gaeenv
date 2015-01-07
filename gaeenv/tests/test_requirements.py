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
    # req_file = 'm:\\Projects\\.env\\requirements.txt'
    os.chdir('m:\\Projects\\.env')
    req_file = glob.glob('requirements.txt')[0]

    print req_file

    # preparations
    if not os.path.isdir(test_dir):
        os.mkdir(test_dir)
    if not os.path.isdir(lib_dir):
        os.mkdir(lib_dir)

    # execute
    requirements.link(req_file, lib_dir)
    links = os.listdir(lib_dir)
    clean_links = map(lambda link: str(link.split('.')[0]), links)
    all_requirements_set = set(pip.req.parse_requirements(req_file))
    requirements_name_set = map(lambda req: req.name.lower(), all_requirements_set)

    print "links:"
    print links

    # verify
    for req in requirements_name_set:
        # if 'antlr' not in req.name.lower():
        if '-' in req:
            name_set = req.split('-')
            req = name_set[0] + str(len(name_set))
        assert req in clean_links



