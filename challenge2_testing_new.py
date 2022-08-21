# Sources: 
# https://docs.python.org/3/library/unittest.html
# https://www.stackvidhya.com/change-order-of-columns-in-pandas-dataframe/
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.equals.html

import unittest
import pandas as pd
from challenge2_json_new import *

############################################
### Function To Check If Two CSVs Are Equal
############################################

def check_csvs_equal(known_solution, output_solution):
    # Accepts known solution and output solution as strings of two csv files

    # Converting csv files to pandas dataframes
    df1 = pd.read_csv(known_solution)
    df2 = pd.read_csv(output_solution)

    # Reordering dataframes so field names are in alphabetical order left to right
    df1 = df1.reindex(sorted(df1.columns), axis=1)
    df2 = df2.reindex(sorted(df2.columns), axis=1)

    # Checking if both dataframes are equal
    return df1.equals(df2)

class DataTransportTestCaseA(unittest.TestCase):
    def setUp(self):
        self.trials = JSON("trials.json")

    ########################################
    ### Tests That Raise Exceptions
    ### See Exceptions.py For All Exceptions
    ########################################

    def test_Invalid_File_Extension(self):
        print("\n Running test_Invalid_File_Extension...")
        with self.assertRaises(Invalid_File_Extension):
            return JSON("trials.html")

    def test_Empty_JSON_File(self):
        print("\n Running test_Empty_JSON_File...")
        with self.assertRaises(Exception):
            trials = JSON("emptyfile.json")
            trials.write_csv("attackers", ['attackerNum', 'type', "omega"], [49], "attackerNum", "attacker_info.csv")

    def test_Empty_JSON_File_Dictionary(self):
        print("\n Running test_Empty_JSON_File_Dictionary...")
        with self.assertRaises(Empty_JSON_File_Dictionary):
            trials = JSON("emptydictfile.json")
            trials.write_csv("attackers", ['attackerNum', 'type', "omega"], [49], "attackerNum", "attacker_info.csv")

    def test_Values_Specific_Field_Mismatch(self):
        print("\n Running test_Values_Specific_Field_Mismatch...")
        with self.assertRaises(Values_Specific_Field_Mismatch):
            self.trials.write_csv("attackers", ['attackerNum', 'type', "omega"], None, "attackerNum", "attacker_info.csv")

    def test_Values_Specific_Field_Mismatch2(self):
        print("\n Running test_Values_Specific_Field_Mismatch2...")
        with self.assertRaises(Values_Specific_Field_Mismatch):
            self.trials.write_csv("attackers", ['attackerNum', 'type', "omega"], [49, 21, 7, 30], None, "attacker_info.csv")

    def test_Empty_Output_Filename(self):
        print("\n Running test_Empty_Output_Filename...")
        with self.assertRaises(Empty_Output_Filename):
            self.trials.write_csv("attackers", ['attackerNum', 'type', "omega"], [49], "attackerNum", None)

    def test_Empty_Attribute(self):
        print("\n Running test_Empty_Attribute...")
        with self.assertRaises(Empty_Attribute):
            self.trials.write_csv(None, ['attackerNum', 'type', "omega"], [49], "attackerNum", "attacker_info.csv")

    def test_Non_Existent_Attribute(self):
        print("\n Running test_Non_Existent_Attribute...")
        with self.assertRaises(Non_Existent_Attribute):
            self.trials.write_csv("rando", ['attackerNum', 'type', "omega"], [49, 7, 26, 33], "attackerNum", "attacker_info.csv")

    def test_Attribute_Not_Type_String(self):
        print("\n Running test_Attribute_Not_Type_String...")
        with self.assertRaises(Attribute_Not_Type_String):
            self.trials.write_csv(10, ['attackerNum', 'type', "omega"], [49, 7, 26, 33], "attackerNum", "attacker_info.csv")

    def test_Fields_List_Not_Type_List(self):
        print("\n Running test_Fields_List_Not_Type_List...")
        with self.assertRaises(Fields_List_Not_Type_List):
            self.trials.write_csv("attackers", {'attackerNum', 'talent'}, [49, 7, 26, 33], "attackerNum", "attacker_info.csv")

    def test_Fields_Not_Type_String(self):
        print("\n Running test_Fields_Not_Type_String...")
        with self.assertRaises(Fields_Not_Type_String):
            self.trials.write_csv("attackers", [{'attackerNum'}, {'talent'}], [49, 7, 26, 33], "attackerNum", "attacker_info.csv")

    def test_Fields_Not_Type_String2(self):
        print("\n Running test_Fields_Not_Type_String2...")
        with self.assertRaises(Fields_Not_Type_String):
            self.trials.write_csv("attackers", [11, 12, 45, 67], [49, 7, 26, 33], "attackerNum", "attacker_info.csv")

    def test_Values_Not_Type_List(self):
        print("\n Running test_Values_Not_Type_List...")
        with self.assertRaises(Values_Not_Type_List):
            self.trials.write_csv("attackers", ['attackerNum', 'type', "omega"], {49, 21, 7, 30}, "attackerNum", "attacker_info.csv")

    def test_Output_Filename_Not_Type_String(self):
        print("\n Running test_Output_Filename_Not_Type_String...")
        with self.assertRaises(Output_Filename_Not_Type_String):
            self.trials.write_csv("attackers", ['attackerNum', 'type', "omega"], [49], "attackerNum", 100)

    def test_No_Data_Found(self):
        print("\n Running test_No_Data_Found...")
        with self.assertRaises(No_Data_Found):
            self.trials.write_csv("attackers", ['attackerNum', 'x'], [49], "attackerNum", "attacker_info.csv")

    def test_No_Data_Found2(self):
        print("\n Running test_No_Data_Found2...")
        with self.assertRaises(No_Data_Found):
            self.trials.write_csv("attackers", ['connor'], [49], "attackerNum", "attacker_info.csv")

    def test_No_Data_Found3(self):
        print("\n Running test_No_Data_Found3... \n")
        with self.assertRaises(No_Data_Found):
            self.trials.write_csv("attackers", ['connor'], None, None, "attacker_info.csv")


    #######################
    ### Passing Tests
    #######################

    def test_Pass_AttackerNum_Values(self):
        print("\n Running test_Pass_AttackerNum_Values... \n")
        self.trials.write_csv("attackers", ['attackerNum', 'type', "omega"], [49, 7, 26, 33], "attackerNum", "output_sol_1.csv")
        assert(check_csvs_equal("known_sol_1.csv", "output_sol_1.csv"))

    def test_Pass_No_Specified_Values(self):
        print("\n Running test_Pass_No_Specified_Values... \n")
        self.trials.write_csv("attackers", ['attackerNum', 'targets', 'talent'], [], None, "output_sol_2.csv")
        assert(check_csvs_equal("known_sol_2.csv", "output_sol_2.csv"))

    def test_Pass_One_Specified_Values(self):
        print("\n Running test_Pass_One_Specified_Values... \n")
        self.trials.write_csv("attackers", ['attackerNum', 'talent'], [22], "attackerNum", "output_sol_3.csv")
        assert(check_csvs_equal("known_sol_3.csv", "output_sol_3.csv"))
    
    def test_Pass_Type_Values(self):
        print("\n Running test_Pass_Type_Values... \n")
        self.trials.write_csv("attackers", ['attackerNum', 'talent', 'type'], ["reputational"], "type", "output_sol_4.csv")
        assert(check_csvs_equal("known_sol_4.csv", "output_sol_4.csv"))

    def test_Pass_Common_Fields_No_Values(self):
        print("\n Running test_Pass_Common_Fields_No_Values... \n")
        self.trials.write_csv("attackers", [], None, None, "output_sol_5.csv")
        assert(check_csvs_equal("known_sol_5.csv", "output_sol_5.csv"))

    def test_Pass_Common_Fields_With_Values(self):
        print("\n Running test_Pass_Common_Fields_With_Values... \n")
        self.trials.write_csv("attackers", [], [49, 21, 7, 30], "attackerNum", "output_sol_6.csv")
        assert(check_csvs_equal("known_sol_6.csv", "output_sol_6.csv"))