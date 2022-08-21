import json
import csv
from exceptions import *

# Helpful notes to self:

#Json object contains key value pairs, acting like a dictionary
#One of the values within the json object is a list called attackers. 
#Within this list are dictionaries - each dictionary specifying an attacker. 
#Within the dictionary could be more dictionaries. 

class JSON(object):
    def __init__(self, input_filename):

        # Check if valid file has been passed - must be .json
        if (not (input_filename[-5:] == '.json')): 
            #raise Exception("Incorrect file type passed - must be .json")
            raise Invalid_File_Extension

        self.filename = input_filename
        self.data = None
        
    def __loadData(self):
        with open(self.filename) as f:
            self.data = json.load(f)
        
        # Checking if json file is empty array
        if (self.data == []):
            #raise Exception("Empty json file passed")
            raise Empty_JSON_File

        #makes data a dictionary instead of a one element list
        self.data = self.data[0]

        # Checking if dictionary is empty
        if (len(self.data) == 0):
            #raise Exception("No data found in Json file dictionary")
            raise Empty_JSON_File_Dictionary        
    
    def __check_fields_helper(self, field, curr_dict):
        for key in curr_dict:
            if (key == field and type(curr_dict[key]) != dict): return True
            elif (type(curr_dict[key]) == dict):
                if (self.__check_fields_helper(field, curr_dict[key])): return True
        return False

    def __check_fields(self, fields, curr_dict):
        # Accepts fields as a set
        if (len(fields) == 0 or "all" in fields): return True
        else:
            for field in fields:
                if (not self.__check_fields_helper(field, curr_dict)): return False
            return True
    

    def __check_val_field(self, val, field, curr_dict):
        # Checks whether a value exists in a field
        # Ex. checking whether a certain attackerNum val exists in its field

        for key in curr_dict:
            if (key == field and type(curr_dict[key]) != dict): 
                if (type(curr_dict[key]) == type(val) and curr_dict[key] == val): 
                    return True
            elif (type(curr_dict[key]) == dict):
                if (self.__check_val_field(val, field, curr_dict[key])): 
                    return True
        return False

    def __get_data(self, attribute, fields, values, spec_field):
        # Specific attribute data is being compiled for, ex: "attackers"
        # Specific fields data is compiled for
        # Specify a list of values for a particular field

        # Checking that attribute exists in Json dictionary
        if (attribute not in self.data):
            raise Non_Existent_Attribute

        attribute_data = self.data[attribute]

        relevant_data = []
        values_found = set()

        if ((not(values) and spec_field) or (not(spec_field) and values)):
            #raise Exception("Specifications for specific field and values must match")
            raise Values_Specific_Field_Mismatch

        for d in attribute_data:
            if (not(fields)): 
                if (not(values) and not(spec_field)):
                    relevant_data.append(d)
    
            else:
                if (self.__check_fields(fields, d) == False): continue
                else:
                    if (not(values) and not(spec_field)):
                        relevant_data.append(d)
                    else:
                        for val in values:
                            if (self.__check_val_field(val, spec_field, d)): 
                                relevant_data.append(d)
                                values_found.add(val)
                                break

        # Detail which values if any were missing from data
        if (values):
            for val in values:
                if (val not in values_found):
                    print("\n The value", val, "for field ", spec_field, " was not found given all specified fields \n")

        return relevant_data

    def __dict_info_helper(self, field, curr_dict, dict_info):
        for key in curr_dict:
            if (key == field and type(curr_dict[key]) != dict):
                dict_info.append(curr_dict[key])
                return dict_info
            elif (type(curr_dict[key]) == dict):
                dict_info = self.__dict_info_helper(field, curr_dict[key], dict_info)
        return dict_info

    def __get_dict_info(self, fields_list, curr_dict):
        # Gets row info from dict to be pasted in csv

        dict_info = []
        for field in fields_list:
            dict_info = self.__dict_info_helper(field, curr_dict, dict_info)
        return dict_info
    
    def __find_fields_dict(self, curr_dict, fields):
        # Accepts an empty set of fields at the start
        for key in curr_dict:
            if (type(curr_dict[key]) != dict):
                fields.add(key)
            else:
                fields = self.__find_fields_dict(curr_dict[key], fields)
        return fields

    def __gather_common_fields(self, attribute, values, spec_field):
        
        field_sets = []
        fields_list = []
        fields_intersection = set()
        attribute_data = self.data[attribute]

        if ((not(values) and spec_field) or (not(spec_field) and values)):
            #raise Exception("Specifications for specific field and values must match")
            raise Values_Specific_Field_Mismatch

        if (not(values) and not(spec_field)):
            for d in attribute_data:
                field_sets.append(self.__find_fields_dict(d, set()))
            fields_intersection = set.intersection(*field_sets)
        else:
            for d in attribute_data:
                for val in values:
                    if (self.__check_val_field(val, spec_field, d)):
                        field_sets.append(self.__find_fields_dict(d, set()))
            fields_intersection = set.intersection(*field_sets)

        for f in fields_intersection:
            fields_list.append(f)
        return fields_list

    def write_csv(self, attribute, fields_list, values, spec_field, output_filename):
        # Only method public to user and can be accessed
        # Creates a csv of data pertaining to user specifications

        self.__loadData()

        # Checking that output file is not None
        if (not(output_filename)):
            #raise Exception("Please provide output file")
            raise Empty_Output_Filename

        # Checking that attribute is not None
        if (not(attribute)):
            #raise Exception("Please provide attribute")
            raise Empty_Attribute

        # Checking for proper types: 
        if (not (type(attribute) == str)):
            #raise Exception("Incorrect type for parameter")
            raise Attribute_Not_Type_String

        if (not (type(fields_list) == list)):
            #raise Exception("Incorrect type for parameter")
            raise Fields_List_Not_Type_List

        for field in fields_list:
            if (not (type(field) == str) and field != None):
                #raise Exception("Incorrect type for parameter")
                raise Fields_Not_Type_String

        if (not (type(values) == list) and values != None):
            #raise Exception("Incorrect type for parameter")
            raise Values_Not_Type_List

        if (not (type(spec_field) == str) and spec_field != None):
            #raise Exception("Incorrect type for parameter")
            raise Specific_Field_Not_Type_String

        if (not (type(output_filename) == str)):
            #raise Exception("Incorrect type for parameter")
            raise Output_Filename_Not_Type_String

        # If no fields are specified, data for all fields must be extracted
        if (not(fields_list)):
            fields_list = self.__gather_common_fields(attribute, values, spec_field)

        fields = set()
        for f in fields_list:
            fields.add(f)

        relevant_data = self.__get_data(attribute, fields, values, spec_field)
        
        if (len(relevant_data) == 0):
            #raise Exception("No data as per specifications found")
            raise No_Data_Found

        with open(output_filename, "w", newline="") as file:
            writer = csv.writer(file)
            headers = fields_list
            info = []
            
            for d in relevant_data:
                info.append(self.__get_dict_info(headers, d))

            writer.writerow(headers)
            writer.writerows(info)
