from challenge2_testing_new import *

def suite():
    # Exception Related Tests

    suite = unittest.TestSuite()
    suite.addTest(DataTransportTestCaseA('test_Invalid_File_Extension'))
    suite.addTest(DataTransportTestCaseA('test_Empty_JSON_File'))
    suite.addTest(DataTransportTestCaseA('test_Empty_JSON_File_Dictionary'))

    suite.addTest(DataTransportTestCaseA('test_Values_Specific_Field_Mismatch'))
    suite.addTest(DataTransportTestCaseA('test_Values_Specific_Field_Mismatch2'))

    suite.addTest(DataTransportTestCaseA('test_Empty_Output_Filename'))
    suite.addTest(DataTransportTestCaseA('test_Empty_Attribute'))
    suite.addTest(DataTransportTestCaseA('test_Non_Existent_Attribute'))
    suite.addTest(DataTransportTestCaseA('test_Attribute_Not_Type_String'))
    suite.addTest(DataTransportTestCaseA('test_Fields_List_Not_Type_List'))
    suite.addTest(DataTransportTestCaseA('test_Fields_Not_Type_String'))
    suite.addTest(DataTransportTestCaseA('test_Fields_Not_Type_String2'))

    suite.addTest(DataTransportTestCaseA('test_Values_Not_Type_List'))
    suite.addTest(DataTransportTestCaseA('test_Output_Filename_Not_Type_String'))
    suite.addTest(DataTransportTestCaseA('test_No_Data_Found'))
    suite.addTest(DataTransportTestCaseA('test_No_Data_Found2'))
    suite.addTest(DataTransportTestCaseA('test_No_Data_Found3'))

    # Passing Tests

    suite.addTest(DataTransportTestCaseA('test_Pass_AttackerNum_Values'))
    suite.addTest(DataTransportTestCaseA('test_Pass_No_Specified_Values'))
    suite.addTest(DataTransportTestCaseA('test_Pass_One_Specified_Values'))
    suite.addTest(DataTransportTestCaseA('test_Pass_Type_Values'))
    suite.addTest(DataTransportTestCaseA('test_Pass_Common_Fields_No_Values'))
    suite.addTest(DataTransportTestCaseA('test_Pass_Common_Fields_With_Values'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())