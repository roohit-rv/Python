states_of_Amercia=["AK - Alaska",  "AL - Alabama",  "AR - Arkansas", "AS - American Samoa", "AZ - Arizona", "CA - California",  "CO - Colorado", 
                "CT - Connecticut",  "DC - District of Columbia",  "DE - Delaware",  "FL - Florida",  "GA - Georgia",  "GU - Guam",  "HI - Hawaii", 
                "IA - Iowa",  "ID - Idaho",  "IL - Illinois",  "IN - Indiana",  "KS - Kansas",  "KY - Kentucky",  "LA - Louisiana",  "MA - Massachusetts",  "MD - Maryland",  "ME - Maine",  "MI - Michigan", 
                "MN - Minnesota",  "MO - Missouri",  "MS - Mississippi",  "MT - Montana",  "NC - North Carolina",  "ND - North Dakota",  "NE - Nebraska",  "NH - New Hampshire",  "NJ - New Jersey",  "NM - New Mexico",  "NV - Nevada", 
                "NY - New York",  "OH - Ohio",  "OK - Oklahoma",  "OR - Oregon",  "PA - Pennsylvania",  "PR - Puerto Rico",  "RI - Rhode Island", 
                "SC - South Carolina",  "SD - South Dakota",  "TN - Tennessee",  "TX - Texas", 
                "UT - Utah",  "VA - Virginia", "VI - Virgin Islands",  "VT - Vermont",  "WA - Washington",  "WI - Wisconsin", "WV - West Virginia", "WY - Wyoming"]
#list is used to store many different strings in just one varirable.
print(states_of_Amercia[0])
#if we want to add any string at last we can use append function
states_of_Amercia.append("RohitOwnsLAnd")
#-1 can be used in the list to display the last string
#if we eant to add more than one string then we can used extend function
states_of_Amercia.extend(["JackReacher", "ArkhamsKnigh"])
print(states_of_Amercia[-1])
#we can specifcally change any position string by using it's postion
states_of_Amercia[2]=("ganginOHIO")
print(states_of_Amercia)