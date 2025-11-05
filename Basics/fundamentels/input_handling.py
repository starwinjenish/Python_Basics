import sys

if len(sys.argv) == 2:
    print("usage:this have two parameter:'full name & last name'")
    sys.exit()
name = sys.argv[1]
last_name = sys.argv[2]
email = name.lower().replace(" ","") + "@company.com"
print("\n ---your profile---")
print("name:",name)
print("Generated Email:",email )

