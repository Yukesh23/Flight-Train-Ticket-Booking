import mysql.connector
yukidb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Yuki$0623@",
    database="yourtravel"
)
print(yukidb)
mycursor=yukidb.cursor()
def register(name,password,mobile_num):
    a="insert into reg(name,password,mobile_num) values(%s,%s,%s)"
    b=(name,password,mobile_num)
    mycursor.execute(a,b)
    yukidb.commit()
    show = mycursor.fetchall()
    print(show)
    
def flight(starting,landing,how,name):
    a="insert into flight(starting_point,landing_point,how_many,name) values(%s,%s,%s,%s)"
    b=(starting,landing,how,name)
    mycursor.execute(a,b)
    yukidb.commit()
    flight_ticket(starting,landing,how,name)
    
def flight_ticket(start,land,how,name):
    mycursor.execute(f"select starting_point,landing_point from flight where name='{name}'")
    show=mycursor.fetchall()
    result=show[0]
  
    if start=="chennai" and land=="delhi":#1000
        total=how*1000
        print(f"Starting-point ='{start}'")
        print(f"ending-point ='{land}'")
        print(f" how many ticket ='{how}'")
        print(f"Total amount ='{total}'")
    elif start == "chennai" and land=="malayisa":#2000
        total=how*2000
        print(f"Starting-point ='{start}'")
        print(f"ending-point ='{land}'")
        print(f" how many ticket ='{how}'")
        print(f"Total amount Ticket ='{total}'")
    elif start== "chennai" and land=="hyderbad":#500
        total=how*500
        print(f"Starting-point ='{start}'")
        print(f"ending-point ='{land}'")
        print(f" how many ticket ='{how}'")
        print(f"Total amount ='{total}'")
        

    else:
        print("flight not available")
        

    
def train(starting,ending,how,name):
    a="insert into train(starting_point,ending_point,how_many,name) values(%s,%s,%s,%s)"
    b=(starting,ending,how,name)
    mycursor.execute(a,b)
    yukidb.commit()
    train_ticket(starting,ending,how,name)
        
def train_ticket(start,end,how,name):
    mycursor.execute(f"select starting_point,ending_point from train where name='{name}'")
    show=mycursor.fetchall()
    result=show[0]
    
    if start=="vellore" and end=="coimbatore":#150
        total=how*150
        mycursor.execute(f"update train set total_cost='{total}' where name='{name}'")
        yukidb.commit()
        print(f"Startivng-point ='{start}'")
        print(f"ending-point ='{end}'")
        print(f" how many ticket ='{how}'")
        print(f"Total amount  ='{total}'")
    elif start == "chennai" and end=="mumbai":#400
        total=how*400
        print(f"Starting-point ='{start}'")
        print(f"ending-point ='{end}'")
        print(f" how many ticket ='{how}'")
        print(f"Total amount ='{total}'")
        print("enjoy your travel")
    
    else:
        print("Sorry train not available") 

def login(name,password):
    mycursor.execute(f"select name,password from reg where name='{name}'")
    show = mycursor.fetchall()
    if show !=[]:
        print("Enter Correct Password")
        if name==show[0][0] and password==show[0][1]:
            print("Login Successful\n  Book your tickets")
            print("1.Flight Ticket")
            print("2.Train Ticket")
            user=int(input("Enter Your Tickets: "))
            if user == 1:
             print("1.chennai to delhi =1000(perticket)")
             print("2.chennai to malaysia =2000(perticket)")
             print("3.chennai to hyderbad=500(perticket)")
             starting_point=input("Enter Your start point: ")
             landing_point=input("Enter Your land point: ")
             how=int(input("How Many Ticket do You Want: "))
             flight(starting_point,landing_point,how,name)
             print("enjoy your travel")


            elif user == 2:
             print("1.vellore to coimbatore =150(perticket)")
             print("2.chennai to mumbai =400(perticket)")
             start=input("Enter Your Start-point: ")
             end=input("Enter Your end-point: ")
             how=int(input("How Many Ticket You Want: "))
             train(start,end,how,name)
             print("enjoy your travel")



            else:
                 print("Enter Valid option")
    else:
        print("Login Failed")

user=int(input("1) Register \n   2) login \n"))
if user == 1:
    name=input("Enter Your Name: ")
    password=input("Enter Your password: ")
    mobile_num=input("Enter Your Mobile: ")
    register(name,password,mobile_num)
elif user == 2:
    name=input("Enter Your Name: ")
    password=input("Enter Your Password: ")

    login(name,password)
