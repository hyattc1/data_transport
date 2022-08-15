import unittest
from challenge2_json_new import *

# Testing to see if program accepts non-json files. 

def test_func1():
    trials = JSON("trials.html")

# Testing to see if program accepts empty json files

def test_func2():
    trials = JSON("emptyfile.json")
    trials.write_csv("attackers", ['attackerNum', 'type', "omega"], [49], "attackerNum", "attacker1_info.csv")

# Testing to see if program accepts json files with empty dictionary 

def test_func3():
    trials = JSON("emptydictfile.json")
    trials.write_csv("attackers", ['attackerNum', 'type', "omega"], [49], "attackerNum", "attacker1_info.csv")

# Testing to see if program accepts empty values and non-empty specific field

def test_func4():
    trials = JSON("trials.json")
    trials.write_csv("attackers", ['attackerNum', 'type', "omega"], None, "attackerNum", "attacker_info.csv")

# Testing to see if program accepts non-empty values and empty specific field

def test_func5():
    trials = JSON("trials.json")
    trials.write_csv("attackers", ['attackerNum', 'type', "omega"], [49, 21, 7, 30], None, "attacker_info.csv")

# Testing to see if program accepts attribute string that doesn't exist

def test_func6():
    trials = JSON("trials.json")
    trials.write_csv("rando", ['attackerNum', 'type', "omega"], [49, 7, 26, 33], "attackerNum", "attacker_info.csv")

# Testing to see if program accepts attribute of type that is not string

def test_func7():
    trials = JSON("trials.json")
    trials.write_csv(10, ['attackerNum', 'type', "omega"], [49, 7, 26, 33], "attackerNum", "attacker_info.csv")

# Testing to see if program accepts fields list that does not contain strings

def test_func8():
    trials = JSON("trials.json")
    trials.write_csv("attackers", [{'attackerNum'}, {'talent'}], [49, 7, 26, 33], "attackerNum", "attacker_info.csv")

# Testing to see if program accepts fields list that is not a list

def test_func9():
    trials = JSON("trials.json")
    trials.write_csv("attackers", {'attackerNum', 'talent'}, [49, 7, 26, 33], "attackerNum", "attacker_info.csv")

# Testing to see if program accepts values list that is not a list

def test_func10():
    trials = JSON("trials.json")
    trials.write_csv("attackers", ['attackerNum', 'type', "omega"], {49, 21, 7, 30}, "attackerNum", "attacker_info.csv")

# Testing to see if program accepts fields list which contains integers

def test_func11():
    trials = JSON("trials.json")
    trials.write_csv("attackers", [11, 12, 45, 67], [49, 7, 26, 33], "attackerNum", "attacker_info.csv")

# Testing to see if program returns data for specifications that don't yield any results

def test_func12():
    trials = JSON("trials.json")
    trials.write_csv("attackers", ['attackerNum', 'x'], [49], "attackerNum", "attacker_info.csv")

# Testing to see if program returns data for fields that do not exist under certain values

def test_func13():
    trials = JSON("trials.json")
    trials.write_csv("attackers", ['connor'], [49], "attackerNum", "attacker_info.csv")

# Testing to see if program returns data for fields that do not exist under all values

def test_func14():
    trials = JSON("trials.json")
    trials.write_csv("attackers", ['connor'], None, None, "attacker_info.csv")

# Testing to see if program runs with non-specified output field

def test_func15():
    trials = JSON("trials.json")
    trials.write_csv("attackers", ['attackerNum', 'type', "omega"], [49], "attackerNum", None)

# Testing to see if program runs under non-specified attribute. 

def test_func16():
    trials = JSON("trials.json")
    trials.write_csv(None, ['attackerNum', 'type', "omega"], [49], "attackerNum", None)

# Working tests #
# These tests contain queries that run and produce CSVs. No Exception errors raised.

def test_pass1():
    trials = JSON("trials.json")
    trials.write_csv("attackers", ['attackerNum', 'type', "omega"], [49, 7, 26, 33], "attackerNum", "attacker1_info.csv")

def test_pass2():
    trials = JSON("trials.json")
    trials.write_csv("attackers", ['attackerNum', 'targets', 'talent'], [], None, "attacker2_info.csv")

def test_pass3():
    trials = JSON("trials.json")
    trials.write_csv("attackers", ['attackerNum', 'talent'], [22], "attackerNum", "attacker3_info.csv")

def test_pass4():
    trials = JSON("trials.json")
    trials.write_csv("attackers", ['attackerNum', 'talent', 'type'], ["reputational"], "type", "attacker4_info.csv")

def test_pass5():
    trials = JSON("trials.json")
    trials.write_csv("attackers", [], None, None, "attacker5_info.csv")

def test_pass6():
    trials = JSON("trials.json")
    trials.write_csv("attackers", [], [49, 21, 7, 30], "attackerNum", "attacker6_info.csv")

# Test Class checks if Exception is raised for Exception-related test cases. 
# Runs all other test cases and prints if they are successful
# If command line runs all 22 tests without failure and ends with ok, you're golden.

class ATestCase(unittest.TestCase):
    def test1(self):
        self.assertRaises(Exception, test_func1)
    
    def test2(self):
        self.assertRaises(Exception, test_func2)

    def test3(self):
        self.assertRaises(Exception, test_func3)

    def test4(self):
        self.assertRaises(Exception, test_func4)
    
    def test5(self):
        self.assertRaises(Exception, test_func5)

    def test6(self):
        self.assertRaises(Exception, test_func6)

    def test7(self):
        self.assertRaises(Exception, test_func7)

    def test8(self):
        self.assertRaises(Exception, test_func8)
    
    def test9(self):
        self.assertRaises(Exception, test_func9)
    
    def test10(self):
        self.assertRaises(Exception, test_func10)

    def test11(self):
        self.assertRaises(Exception, test_func11)

    def test12(self):
        self.assertRaises(Exception, test_func12)

    def test13(self):
        self.assertRaises(Exception, test_func13)

    def test14(self):
        self.assertRaises(Exception, test_func14)

    def test15(self):
        self.assertRaises(Exception, test_func15)

    def test16(self):
        self.assertRaises(Exception, test_func16)

    def test17(self):
        test_pass1()
        print("Test Pass 1 Successful")

    def test18(self):
        test_pass2()
        print("Test Pass 2 Successful")

    def test19(self):
        test_pass3()
        print("Test Pass 3 Successful")
    
    def test20(self):
        test_pass4()
        print("Test Pass 4 Successful")

    def test21(self):
        test_pass5()
        print("Test Pass 5 Successful")

    def test22(self):
        test_pass6()
        print("Test Pass 6 Successful")

unittest.main()