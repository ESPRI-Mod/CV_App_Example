from cv_app_example.api_client import get



DD_names = get("api/universe/datadescriptor")
print(DD_names)



for dd in DD_names:
    print(get("api/universe/datadescriptor/"+dd))


for dd in DD_names:
    terms = get("api/universe/datadescriptor/"+dd+"/term")
    print(terms)

for dd in DD_names:
    print("")
    terms = get("api/universe/datadescriptor/"+dd+"/term")
    for term in terms:
        t = get("api/universe/datadescriptor/"+dd+"/term/"+term['id'])
        print(dd,"    ",t)
    


# # Exploring known projects 


known_projects = get("api/project/")
print(known_projects)

for proj in known_projects:
    print(get("api/project/"+proj))

col_names = get("api/project/CMIP6Plus_CVs/collection")
print(col_names)

for col in col_names:
    print(get("api/project/CMIP6Plus_CVs/collection/"+col))


for col in col_names:
    print(col,"   ",get("api/project/CMIP6Plus_CVs/collection/"+col+"/term"))

for col in col_names:
    term_ids = get("api/project/CMIP6Plus_CVs/collection/"+col+"/term")
    for term in term_ids:
        t = get("api/project/CMIP6Plus_CVs/collection/"+col+"/term/"+term)
        print(col,"  ",t)
    


# Some shortcuts 

print(get("api/universe/datadescriptor/institution/term/ipsl"))
print(get("api/universe/term/ipsl"))


print(get("api/project/CMIP6Plus_CVs/collection/"+"institution_id"+"/term/"+"ipsl"))
print("")
print(get("api/project/term/ipsl")[0]["term"]) # WHY [0]["term"] ???? 


# Explore all (Universe and projects) in one call  

ipsl_insts = get("api/term/"+"ipsl")
for inst in ipsl_insts:
    print(inst["path"])
    print( "  ", inst)


print(get("api/collection/institution_id"))

