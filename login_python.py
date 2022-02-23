import re
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
pattern=re.compile(r'')
def reg():
    name=input("Enter your Email:")
    if(re.search(regex,name)):
        print("Email-Id Valid!!!")
        passwd=input("Enter your Password:")
        cpasswd=input("Confirm your Password:")
        if passwd==cpasswd:
            if len(passwd)<6 and len(passwd)>16:
                print('Password must be 6 to 16 characters long')
            elif re.search(r'[!@#$%^&*()]',passwd) is None:
                print('Password must contain atleast one special Symbol')
            elif re.search(r'\d',passwd) is None:
                print('Password must contain atleast one digit')
            elif re.search(r'[A-Z]',passwd) is None:
                print('password must contain one capital letter')
            elif re.match(r'[a-z A-Z 0-9 !@#$%^&*()]{6,16}',passwd):
                result=pattern.match(passwd)
                print("Password is Correct")
            else:
                print("Password Invalid")
        else:
            print("Password did not match...")
    else:
        print("Email Id Invalid!")

    db=open("C:\\Users\\Asus\\Desktop\\login_python\\login.txt","a")
    db.write(name+",")
    db.write(passwd)
    db.write('\n')
    
reg()
def gainAccess(name=None, passwd=None):
    name = input("Enter your username:")
    passwd = input("Enter your Password:")
    
    if not len(name or Passwd) < 1:
        if True:
            db = open("C:\\Users\\Asus\\Desktop\\login_python\\login.txt", "r")
            d = []
            f = []
            for i in db:
                a,b = i.split(",")
                b = b.strip()
                c = a,b
                d.append(a)
                f.append(b)
                data = dict(zip(d, f))
            try:
                if name in data:
                                   
                    try:
                        if passwd==passwd:
                        
                            print("Login success!")
                            print("Hi",name,"Welcome to KT infotech...")
                            
                        else:
                            print("Wrong password")
                        
                    except:
                        print("Incorrect passwords or username")
                else:
                    print("Username doesn't exist")
            except:
                print("Password or username doesn't exist")
        else:
            print("Error logging into the system")
            print("check forget password")
            forget()
            
    else:
        print("Please attempt login again")
gainAccess()
def forget():
    if name == name:
        fp=print("Enter your last remembered Password:")
        if passwd==fp:
            print("Password is correct... Try soome other time...")
        if passwd!=fp:
            fp1=print("Enter your New password:")
            fp2=print("Confirm your new password:")
            if fp1==fp2:
                if len(passwd)<6 and len(passwd)>16:
                    print('Password must be 6 to 16 characters long')
                elif re.search(r'[!@#$%^&*()]',passwd) is None:
                    print('Password must contain atleast one special Symbol')
                elif re.search(r'\d',passwd) is None:
                    print('Password must contain atleast one digit')
                elif re.search(r'[A-Z]',passwd) is None:
                    print('password must contain one capital letter')
                elif re.match(r'[a-z A-Z 0-9 !@#$%^&*()]{6,16}',passwd):
                    result=pattern.match(passwd)
                    print("Password is Correct")
                else:
                    print("Password Invalid")
            else:
                print("Password did not match...")

        if not len(name or Passwd) < 1:
            if True:
                db = open("C:\\Users\\Asus\\Desktop\\login_python\\login.txt", "w")
                d = []
                f = []
                for i in db:
                    a,b = i.split(",")
                    b = b.strip()
                    c = a,b
                    d.append(a)
                    f.append(b)
                    data = dict(zip(d, f))
                try:
                    if name in data:
                                       
                        try:
                            if passwd==passwd:
                            
                                print("Login success!")
                                print("Hi",name,"Welcome to KT infotech...")
                                
                            else:
                                print("Wrong password")
                        except:
                            print("Wait...")
                except:
                    print("Kindly Register again...")
                    reg()
                    
