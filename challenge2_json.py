import json
import csv
import copy

class JSON(object):
    def __init__(self, input_filename):
        self.filename = input_filename
        self.data = None
        
    def __loadData(self):
        with open(self.filename) as f:
            self.data = json.load(f)
        
        #makes data a dictionary instead of a one element list
        self.data = self.data[0]

    def __checkFields(self, curDict, fields):
        if(not fields): return
        for key in curDict:
            if(type(curDict[key]) == dict):
                self.__checkFields(curDict[key], fields)
            elif(key in fields):
                fields.remove(key)
               
    def getCSV(self, attribute, num, output_filename, fields):
        self.__loadData()
        
        #The specific attribute we are looking for: in this case the 
        #attackers list 
        csv_data = self.data[attribute]

        #Checking that a valid attacker is requested
        if(num > len(csv_data)):
            raise ValueError("Invalid attribute request")
        
        #Specific attacker dictionary
        attribute_data = csv_data[num-1]

        #checking validity of fields
        temp = copy.deepcopy(fields)
        self.__checkFields(attribute_data, temp)
        if(temp):
            str_fields = ", ".join(temp)
            raise Exception("These field(s) are invalid: ", str_fields)
        
        with open(output_filename, "w", newline="") as file:
            #writer object to write to csv file
            writer = csv.writer(file)
            headers = [] #headers in the csv
            info = [] #data for a specific attacker
            curName = ""
           
            #function that fills in the relevant data
            self.__getData(attribute_data, fields, headers, info, curName)
            print("fields: ",fields)
            #writing data to csv file
            writer.writerow(headers)
            writer.writerow(info)

    def __getData(self, curDict, fields, headers, info, curName):
        for key in curDict:
          
            if(type(curDict[key]) == dict):
                newCurName = curName + key + "_"
                self.__getData(curDict[key], fields, headers, info, newCurName)
            elif((fields and key in fields) or not fields):
                keyName = curName + key
                headers.append(keyName)
                info.append(curDict[key])