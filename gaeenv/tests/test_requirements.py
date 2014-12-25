__author__ = 'Eva Sokolyanskaya'

import pytest
import sys
import os
from gaeenv import requirements


def test_list_print(capsys):
    # given
    data = 'qwerty\nasdfg'
    file_name = 'c:\\temp\\test_file.txt'

    # execute
    f = open(file_name, 'w')
    f.write(data)
    f.close()

    requirements.list(file_name)
    out, err = capsys.readouterr()
    out = out.strip('\n')
    # os.remove(file_name)

    # verify
    assert out == data




