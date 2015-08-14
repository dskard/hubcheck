#!/usr/bin/env python
#
# updated version of junit_xml_merge from:
#
# Corey Goldberg, Dec 2012
# https://gist.github.com/cgoldberg/4320815
#

import os
import sys
import xml.etree.ElementTree as ET


"""Merge multiple JUnit XML files into a single results file.

Output dumps to sdtdout.

example usage:
    $ python merge_junit_results.py results1.xml results2.xml > results.xml
"""


def main():
    args = sys.argv[1:]
    if not args:
        usage()
        sys.exit(2)
    if '-h' in args or '--help' in args:
        usage()
        sys.exit(2)
    juxm = JUnitXMLMerger()
    juxm.merge_results(args[:])


class JUnitXMLMerger(object):

    def __init__(self):

        self.failures = 0
        self.errors = 0
        self.skips = 0
        self.tests = 0
        self.time = 0.0

        self.testsuites = []


    def merge_results(self,xml_files):

        for file_name in xml_files:
            tree = ET.parse(file_name)
            root = tree.getroot()
            if root.tag == 'testsuites':
                for testsuite in  root.getchildren():
                    self.process_testsuite(testsuite)
            elif root.tag == 'testsuite':
                self.process_testsuite(root)
            else:
                # unrecognized root note
                pass

        # write the new xml file out
        new_root = ET.Element('testsuites')
#        new_root.attrib['failures'] = '%s' % failures
#        new_root.attrib['tests'] = '%s' % tests
#        new_root.attrib['errors'] = '%s' % errors
#        new_root.attrib['time'] = '%s' % time
        for testsuite in self.testsuites:
            new_root.append(testsuite)
        new_tree = ET.ElementTree(new_root)
        ET.dump(new_tree)

    def process_testsuite(self,test_suite):

        if 'failures' in test_suite.attrib:
            self.failures += int(test_suite.attrib['failures'])
        if 'tests' in test_suite.attrib:
            self.tests += int(test_suite.attrib['tests'])
        if 'errors' in test_suite.attrib:
            self.errors += int(test_suite.attrib['errors'])
        if 'time' in test_suite.attrib:
            self.time += float(test_suite.attrib['time'])

        self.testsuites.append(test_suite)



def usage():
    this_file = os.path.basename(__file__)
    print 'Usage: %s results1.xml results2.xml' % this_file


if __name__ == '__main__':
    main()
