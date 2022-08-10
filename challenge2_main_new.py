from challenge2_json_new import *

fields1 = ['attackerNum', 'type', "omega"]
fields2 = ['attackerNum', 'targets', 'talent']
fields3 = ['attackerNum', 'talent']
fields4 = ['attackerNum', 'talent', 'type']
fields5 = []
fields6 = []

values1 = [49, 7, 26, 33]
values2 = []
values3 = [22]
values4 = ["reputational", "random"]
values5 = None
values6 = [49, 21, 7, 30]

trials = JSON("trials.json")

trials.write_csv("attackers", fields1, values1, "attackerNum", "attacker1_info.csv")
trials.write_csv("attackers", fields2, values2, None, "attacker2_info.csv")
trials.write_csv("attackers", fields3, values3, "attackerNum", "attacker3_info.csv")
trials.write_csv("attackers", fields4, values4, "type", "attacker4_info.csv")
trials.write_csv("attackers", fields5, values5, None, "attacker5_info.csv")
trials.write_csv("attackers", fields6, values6, "attackerNum", "attacker6_info.csv")
