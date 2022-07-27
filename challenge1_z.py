#Challenge 1:  Moving JSON data from an API endpoint into a csv file

import json
import csv

#opening the json file
with open("testdata.json") as f:
    data = json.load(f)

#the list of github repos
gitData = data["items"]

#field names for the json file
fields = ["repo_id", "repo_name", "stargazers", "project_url", "owner_name", "owner_id"]

#adding the data to the csv file
with open("converted_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    
    writer.writerow(fields) #headers
    for item in gitData:
        temp_owner = item["owner"]
        temp_row = []
        temp_row.append(item["id"])
        temp_row.append(item["name"])
        temp_row.append(item["stargazers_count"])
        temp_row.append(item["html_url"])
        temp_row.append(temp_owner["login"])
        temp_row.append(temp_owner["id"])
        writer.writerow(temp_row)



