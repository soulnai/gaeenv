__author__ = 'user'

import pytest
import sdk
import utils
import logging

def test_latest_sdk_version():
    #execute
    func_response = sdk.get_latest_version()
    #result
    assert func_response == ("1", "8", "9")


def test_create_logger():
    #execute
    func_response = utils.create_logger()
    #result
    assert type(func_response) == logging._loggerClass

