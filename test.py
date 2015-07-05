# Tests one project.  Must be run from a subdirectory of /Algorithms.  
# Looks for a main.py to run, with inputs in the file "input" and expected
# outputs in the file "output".
# If a test subdirectory exists, run all tests in that directory.  
# On any failure, stop immediately- do not run the other tests.

import pdb

import os
import subprocess
import filecmp

import sys

def main(argv):
    rootDir = os.getcwd()
    leafDir = rootDir.split("/")[-1]

    tempOutput = rootDir.split("/")[:-1]
    tempOutput.append(".testOutput")
    tempOutputFile = "/".join(tempOutput)

    if leafDir == "Algorithms":
        print "Error: Must run this script in a subdirectory of Algorithms"
        exit(-1)

    testName = argv[0]
    if testName.endswith('.py'):
        testName = testName.replace('.py', "")
    filePath = rootDir + "/%s.py" % testName

    if not os.path.isfile(filePath):
        print "Error: Cannot find %s.py in subdirectory %s" % (testName, leafDir)
        exit(-1)


    def runOneTest(inpt, ExpectedOutput, testNumber):
        cmd = "python %s" % filePath
        if inpt:
            cmd = cmd + " < " + inpt
        print "Running %s ...\n" % cmd

        with open(tempOutputFile, "w") as outfile:
            subprocess.call(cmd, stdout=outfile, stderr=outfile, shell=True)

        success = filecmp.cmp(tempOutputFile, ExpectedOutput)

        if success:
            print "Test %d Pass\n" % testNumber
            return True
        else:
            print "Test %d Fail" % testNumber
            print "Your Output:"
            print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
            with open(tempOutputFile, "r") as f:
                print f.read()
            print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
            print "Expected Output:"
            print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
            with open(ExpectedOutput, "r") as f:
                print f.read()
            print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
            exit(-1)
            return False

    testCase = 0
    def findTestCase(root=False):
        #Looks in root directory, or root/test directory for input and output files
        if root:

            output = rootDir + "/output"
            if not os.path.isfile(output):
                return False
            
            inpt = rootDir + "/input"
            if not os.path.isfile(inpt):
                #some projects will have no input
                print "Warning: No input file found"
                inpt = None
            
        else:
            output = rootDir + "/tests/output%d" % testCase
            if not os.path.isfile(output):
                return False
            inpt = rootDir + "/tests/input%d" % testCase
            if not os.path.isfile(inpt):
                #some projects will have no input
                print "Warning: No input file found"
                inpt = None

        return runOneTest(inpt, output, testCase)

    if findTestCase(True):
        testCase += 1
    else:
        print "Did not find any tests in %s" % rootDir
        print "Trying %s/tests/" % rootDir
        #exit(-1)

    # Tests in /project/tests/ can be 1-indexed.  So don't fail immediately if
    # we don't find test 0.
    findTestCase(root=False)
    testCase += 1
    while findTestCase(root=False):
        testCase += 1

    print "All tests Passed"


if __name__ == "__main__":
    main(sys.argv[1:])

