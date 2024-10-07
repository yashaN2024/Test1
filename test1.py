from datetime import datetime

print ("Hello АКАДЕМИЯ ТОП")
date_birth = input() #"11.10.2007"
print(datetime.date(datetime.strptime(date_birth,"%Y-%m-%d")))
date_birth_data = datetime.date(datetime.strptime(date_birth,"%Y-%m-%d"))
year = date_birth_data.year
print(year)
now_year = datetime.now().year
#print(now_year)
#age = now_year - year
#print(age)
a =  "Второй Урок"
b = 10
print(a * b)
#
print(a)
хороший урок
