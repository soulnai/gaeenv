__author__ = 'Eva Sokolyanskaya'

import pytest
import sys
import os
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


def test_link():
    # given
    test_dir = "..\\..\\..\\test_dir\\"
    lib_dir = test_dir + 'lib_dir'
    req_file = 'm:\\Projects\\.env\\requirements.txt'

    # preparations
    if not os.path.isdir(test_dir):
        os.mkdir(test_dir)
    if not os.path.isdir(lib_dir):
        os.mkdir(lib_dir)
    f = open(req_file, 'r')
    reqs_list_from_req_file = f.readlines()
    reqs_list_clean = map(lambda req: str(req.split('=')[0].lower()), reqs_list_from_req_file)

    f.close()

    # execute
    requirements.link(req_file, lib_dir)
    links = os.listdir(lib_dir)
    clean_links = map(lambda link: str(link.split('.')[0]), links)

    print "links:"
    print links
    print "reqs_list_clean:"
    print reqs_list_clean

    # verify
    for req in reqs_list_clean:
        if 'antlr' not in req:
            assert req in clean_links






