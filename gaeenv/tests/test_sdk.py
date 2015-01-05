__author__ = 'user'

import pytest
import gaeenv.sdk
import gaeenv.utils
import logging
import os

def test_get_latest_sdk_version():
    #execute
    latest_version = gaeenv.sdk.get_latest_version()
    #result
    assert latest_version == ("1", "8", "9")


def test_create_logger():
    #execute
    is_logger = gaeenv.utils.create_logger()
    #result
    assert type(is_logger) == logging._loggerClass

def test_download_sdk():
    #execute
    assert os.path.exists(gaeenv.sdk.download())

def test_get_versions():
    #execute
    versions_list = gaeenv.sdk.get_versions()
    #result
    assert len(versions_list) > 0
