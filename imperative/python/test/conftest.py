import os
import sys

import pytest

from megengine.core._imperative_rt.imperative import sync

sys.path.append(os.path.join(os.path.dirname(__file__), "helpers"))


def pytest_runtest_teardown():
    sync()
