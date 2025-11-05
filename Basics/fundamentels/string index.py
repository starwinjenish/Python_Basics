#string index
'''example(hello)
str[o] = 'h',   str[:] = 'hello'
str[1] = 'e',   str[0:] = 'hello'
str[2] = 'l',   str[:5] = 'hello'
str[3] = 'l',   str[:3] = 'hel'
str[4] = 'o',   str[0:2] = 'he'
                str[1:4] = 'eel'

'''#Example
# User_Name = "STARWIN"
# print(User_Name[0:-1])
# print(User_Name[3:5])

#string handling

# e_sport_team = "staRwin"

# print(e_sport_team.upper())
# print(e_sport_team.lower())
# print(e_sport_team.capitalize())

#String Usecases
mobile_number = "7639249726"
masked = mobile_number[:2]+"********"+mobile_number[-2:]
print(masked)
print("\n")
#title method
Game_name = "call OF Duty"
company = " ACtivision"
formated_version = f"{Game_name.title()} - {company.title()}"
print(formated_version)
print("\n")
#replace method
location = "tirunelveli"
fixed_location =location.replace("tirunelveli","Vadakkankulam")
print(fixed_location)
#strip method
print('\n')
message = "your booking id is,123456.please keep it safe"
id = message.split(',')[1].split('.')[0].strip()
print(id)
#find posistion
print("\n")
txt = "elcome to the Ultimate 12-Hour Python Masterclass in Tamil – designed for freshers, data engineers, data analysts, and aspiring data scientists! This all-in-one course covers Python from the very basics to advanced real-world applications"
posistion = txt.find("Ultimate")
print(posistion)
print("\n")
name = "Starwin jenish s"
initial ="".join([word[0].upper()for word in name.split()])
print(initial)