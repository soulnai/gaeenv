__author__ = 'user'

import pytest
import gaeenv.sdk
import gaeenv.utils
import logging

def test_latest_sdk_version():
    #execute
    latest_version = gaeenv.sdk.get_latest_version()
    #result
    assert latest_version == ("1", "8", "9")


def test_create_logger():
    #execute
    is_logger = gaeenv.utils.create_logger()
    #result
    assert type(is_logger) == logging._loggerClass

