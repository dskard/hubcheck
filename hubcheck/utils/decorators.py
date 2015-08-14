import hubcheck.conf
import functools
import unittest
import logging
import re

logger = logging.getLogger(__name__)

def _id(obj):
    return obj

def hub_version(min_version=None,max_version=None):
    """
    run test only if the hub has a version greater than or equal to
    min_version and less than or equal to max_version

    :Args:
    - min_version: minimum version this test is valid for as string
    - max_version: maximum version this test is valid for as string
    """

    # code from http://stackoverflow.com/a/1714190
    def version_cmp(version1, version2):
        def normalize(v):
            return [int(x) for x in re.sub(r'(\.0+)*$','', str(v)).split(".")]
        return cmp(normalize(version1), normalize(version2))


    if (min_version is None) and (max_version is None):
        # invalid inputs
        # run the test
        return _id

    elif (min_version is None) and (max_version is not None):
        # only compare max version
        if version_cmp(hubcheck.conf.settings.hub_version,max_version) <= 0:
            return _id

    elif (min_version is not None) and (max_version is None):
        # only compare min version
        if version_cmp(min_version,hubcheck.conf.settings.hub_version) <= 0:
            return _id

    elif (version_cmp(min_version,hubcheck.conf.settings.hub_version) <= 0) and \
         (version_cmp(hubcheck.conf.settings.hub_version,max_version) <= 0):
        # min_version <= hub_version <= max_version
        # run the test
        return _id

    msg = 'hub_version (%s) is outside of valid range for test (%s,%s)' \
        % (hubcheck.conf.settings.hub_version,min_version,max_version)

    return unittest.skip(msg)


def tool_container_version(*args):
    """
    run test only if the hub is running a compliant tool container version.

    :Args:
    - *args: list of valid tool container types
    """

    args = list(args)
    args.append('_all')

    for tc_version in args:
        if tc_version in hubcheck.conf.settings.tool_container_version:
            return _id

    msg = 'no matching tool_container_version (%s): %s' \
            % (hubcheck.conf.settings.tool_container_version,args)

    return unittest.skip(msg)


def check_hub_version(min_version=None,max_version=None):
    """
    run test only if the hub has a version greater than or equal to
    min_version and less than or equal to max_version

    :Args:
    - min_version: minimum version this test is valid for as string
    - max_version: maximum version this test is valid for as string
    """

    # code from http://stackoverflow.com/a/1714190
    def version_cmp(version1, version2):
        def normalize(v):
            return [int(x) for x in re.sub(r'(\.0+)*$','', str(v)).split(".")]
        return cmp(normalize(version1), normalize(version2))


    if (min_version is None) and (max_version is None):
        # invalid inputs
        # run the test
        return True

    elif (min_version is None) and (max_version is not None):
        # only compare max version
        if version_cmp(hubcheck.conf.settings.hub_version,max_version) <= 0:
            return True

    elif (min_version is not None) and (max_version is None):
        # only compare min version
        if version_cmp(min_version,hubcheck.conf.settings.hub_version) <= 0:
            return True

    elif (version_cmp(min_version,hubcheck.conf.settings.hub_version) <= 0) and \
         (version_cmp(hubcheck.conf.settings.hub_version,max_version) <= 0):
        # min_version <= hub_version <= max_version
        # run the test
        return True

    return False


def check_hub_hostname(hostnames):
    """
    run test only if the hub hostnames is in the provided list
    """

    return hubcheck.conf.settings.hub_hostname in hostnames

