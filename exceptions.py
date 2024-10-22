# Source credits: 
# https://towardsdatascience.com/how-to-define-custom-exception-classes-in-python-bfa346629bca
# https://www.programiz.com/python-programming/user-defined-exception

# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""

    def __str__(self):
        return "".join([self.__class__.__name__, ' error has been raised'])
    pass

class Invalid_File_Extension(Error):
    """Incorrect file type passed - must be .json"""
    pass

class Empty_JSON_File(Error):
    """Empty Json file passed"""
    pass

class Empty_JSON_File_Dictionary(Error):
    """Empty dictionary passed in JSON file"""
    pass

class Values_Specific_Field_Mismatch(Error):
    """Specific field and values don't match/correspond to one another"""
    pass

class Empty_Output_Filename(Error):
    """Empty output filename argument passed"""
    pass

class Empty_Attribute(Error):
    """Empty attribute argument passed"""
    #print("Empty attribute argument passed")
    pass

class Non_Existent_Attribute(Error):
    """Attribute does not exist in Json dictionary"""
    pass

class Attribute_Not_Type_String(Error):
    """Attribute is not of type String"""
    pass

class Fields_List_Not_Type_List(Error):
    """Fields list is not of type List"""
    pass

class Fields_Not_Type_String(Error):
    """Fields in fields list are not of type String"""
    pass

class Values_Not_Type_List(Error):
    """Values list is not of type List"""
    pass

class Specific_Field_Not_Type_String(Error):
    """Specific field is not of type String"""
    pass

class Output_Filename_Not_Type_String(Error):
    """Output filename is not of type String"""
    pass

class No_Data_Found(Error):
    """No dictionaries with relevant data found as per defined specifications"""
    pass

