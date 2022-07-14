from datetime import datetime
def counter(year , mounth , day):
    global datenow 
    datenow = datetime.now()
    global brithday
    brithday = datetime(year,mounth,day)
    return f" ur next brithday after  {datenow - brithday}"


my = counter(2000 , 4 , 22)
print(my)
