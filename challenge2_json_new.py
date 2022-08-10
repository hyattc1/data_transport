import json
import csv

# Helpful notes to self:

#Json object contains key value pairs, acting like a dictionary
#One of the values within the json object is a list called attackers. 
#Within this list are dictionaries - each dictionary specifying an attacker. 
#Within the dictionary could be more dictionaries. 

class JSON(object):
    def __init__(self, input_filename):
        self.filename = input_filename
        self.data = None
        
    def __loadData(self):
        with open(self.filename) as f:
            self.data = json.load(f)
        
        #makes data a dictionary instead of a one element list
        self.data = self.data[0]
    
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

        attribute_data = self.data[attribute]

        relevant_data = []

        for d in attribute_data:
            if (self.__check_fields(fields, d) == False): continue
            else:
                if (not(values == [] or values == ["all"])):
                    for val in values:
                        if (self.__check_val_field(val, spec_field, d)): 
                            relevant_data.append(d)
                            break
                else:
                    relevant_data.append(d)
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
    
    def write_csv(self, attribute, fields, values, spec_field, output_filename):
        # Only method public to user and can be accessed
        # Creates a csv of data pertaining to user specifications

        self.__loadData()

        relevant_data = self.__get_data(attribute, fields, values, spec_field)
        
        if (len(relevant_data) == 0):
            raise Exception("Data as per specifications not found")

        fields_list = []
        for field in fields:
            fields_list.append(field)

        with open(output_filename, "w", newline="") as file:
            writer = csv.writer(file)
            headers = fields_list
            info = []
            
            for d in relevant_data:
                info.append(self.__get_dict_info(fields_list, d))

            writer.writerow(headers)
            writer.writerows(info)
