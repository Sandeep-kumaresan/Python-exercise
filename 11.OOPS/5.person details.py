from datetime import date
class person:
    def __init__(self,name,country,dob):
        self.name=name
        self.country=country
        self.dob=dob
    
    def age_cal(self):
        today=date.today()
        age=today.year-self.dob.year
        if today < date(today.year,self.dob.month,self.dob.day):
            age-=1
        return age

person1=person("Sandeep","India",date(2002,8,13))
person2=person("Justin Bieber","America",date(1979,6,20))
person3=person("Marshal Mathers","UK",date(1985,12,7))

print("name of person1:",person1.name," ","Age of person1:",person1.age_cal())
print("name of person2:",person2.name," ","Age of person2:",person2.age_cal())
print("name of person3:",person3.name," ","Age of person3:",person3.age_cal())