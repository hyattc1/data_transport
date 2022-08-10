from challenge2_json import *

fields1 = {'attackerNum', 'type', "omega"}
fields2 = {'attackerNum', 'targets', 'talent'}
fields3 = {'attackerNum', 'talent'}
values1 = [49, 7, 26, 33]
values2 = []
values3 = [22]

trials = JSON("trials.json")

trials.write_csv("attackers", fields1, values1, "attackerNum", "attacker1_info.csv")
trials.write_csv("attackers", fields2, values2, "attackerNum", "attacker2_info.csv")
trials.write_csv("attackers", fields3, values3, "attackerNum", "attacker3_info.csv")

