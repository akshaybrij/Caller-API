from faker import Faker
import json
from random import randint
from ProfileUser.models import User,Contact
from ProfileUser.serializers import ContactSerializer

data = []

class DataGen:
    def generator(self):
        from faker import Faker
        num = '912%s' % (self.random_with_N_digits(7))
        name = Faker().name()
        return name,num

        
    def random_with_N_digits(self,n):
        range_start = 10**(n-1)
        range_end = (10**n)-1
        from random import randint 
        return randint(range_start, range_end)

dt = DataGen()
for k in range(99):
    name,num = dt.generator()
    data.append({'full_name':name,'num':num})

data = json.dumps(data)
with open('data.txt','w') as dt:
    dt.write(data)
fl = open('data.txt','rb').read()
fl = json.loads(fl)
for k in fl:
    con = ContactSerializer(data=k)
    if con.is_valid():
        con.save()



