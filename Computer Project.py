print("==================================== COMPUTER PROJECT =======================================")
print("\n")
print("\t             CREATED BY ANJAL.P.DIJO & ADREENA.J.THEKKAN")
print("                                     CLASS - XII.B")
print("\n")
print("=============================================================================================")

def Book_Record():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="root")
    if mydb.is_connected():
        print("Connection Successful")
    else:
        print("Connection Unsuccessful")
    mycursor=mydb.cursor()
    mycursor.execute("create database if not exists library")
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="library")
    mycursor=mydb.cursor()
    mycursor.execute("create table Book(Book_code int(90)primary key,Book_name varchar(90),Author_of_book varchar(90),Price_of_book int(90),Publisher_of_book varchar(90),Date_of_purchase date,Total_quantity_of_book int(90))")
    mydb.commit()

    
    def bookinsertion():
        print("---------------------------------------------------------------------------------------------")
        import mysql.connector
        try:
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="library")
            mycursor=mydb.cursor()
            k="y"
            while k=="y":
                n=int(input("Enter the Book code:"))
                t=input("Enter the Book name:")
                q=input("Enter the Author of book:")
                e=input("Enter the Price of book:")
                r=input("Enter the Publisher of book:")
                d=input("Enter the Date of purchase:")
                z=int(input("Enter the Quantity purchased:"))
                a=(n,t,q,e,r,d,z)
                w="Insert into Book values(%s,%s,%s,%s,%s,%s,%s)"
                mycursor.execute(w,a)
                print("Insertion is Successful")
                k=input("Do you want to continue insertion of book records(y/n):")
                mydb.commit()
        except Exception as e:
            print(e)
        print("---------------------------------------------------------------------------------------------")        


    def bookdisplay():
        print("---------------------------------------------------------------------------------------------")
        import mysql.connector
        try:
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="library")
            mycursor=mydb.cursor()
            mycursor.execute("select * from Book")
            print("*******************************************BOOK**********************************************")
            for i in mycursor:
                print(i)
            print("*********************************************************************************************")
            print("Number of Book Records:",mycursor.rowcount)
        except Exception as e:
            print(e)
        print("---------------------------------------------------------------------------------------------")


    def booksearch():
        print("---------------------------------------------------------------------------------------------")
        import mysql.connector
        try:
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="library")
            mycursor=mydb.cursor()
            g="y"
            while g=="y":
                w=input("Enter the book to be searched:")
                t=(w,)
                k="select* from Book where Book_name=%s"
                mycursor.execute(k,t)
                for i in mycursor:
                    if i[1]==w:
                        print("Book is present in library")
                        print("Book Details")
                        print("Book code:",i[0])
                        print("Book name:",i[1])
                        print("Author of book:",i[2])
                        print("Price of book:",i[3])
                        print("Publisher of book:",i[4])
                        print("Date of purchase:",i[5])
                        print("Quantity purchased:",i[6])
                        break
                else:
                    print("Sorry!!!")
                    print("The book",w,"that you had asked to search is not present in  the library")
                    print("Please try again...")
                g=input("Do you want to continue the searching of book records(y/n):")
        except Exception as e:
            print(e)
        print("---------------------------------------------------------------------------------------------")                    


    def bookdelete():
        print("---------------------------------------------------------------------------------------------")
        import mysql.connector
        try:
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="library")
            mycursor=mydb.cursor()
            h="y"
            while h=="y":
                print("Deletion operations")
                print("1. To delete Book name")
                print("2. To delete Book code")
                c=int(input("Enter your choice:"))
                if c==1:
                    u=input("Enter the name of book to be deleted:")
                    m="select * from Book where Book_name=%s"
                    t=(u,)
                    mycursor.execute(m,t)
                    for i in mycursor:
                        if i[1]==u:
                            t=(u,)
                            w="delete from Book where Book_name=%s"
                            mycursor.execute(w,t)
                            print("The book",u,"is deleted")
                            print("Deletion is Successful")
                            print("Number of Book Records:",mycursor.rowcount)
                            break
                    else:
                        print("Sorry!!!")
                        print("The book",u,"that you had asked to delete is not present in the library")
                        print("Please try again...")
                elif c==2:
                    b=int(input("Enter the code of book to be deleted:"))
                    m="select * from Book where Book_code=%s"
                    y=(b,)
                    mycursor.execute(m,y)
                    for i in mycursor:
                        if i[0]==b:
                            y=(b,)
                            w="delete from Book where Book_code=%s"
                            mycursor.execute(w,y)
                            print("The book code",b,"is deleted")
                            print("Deletion is Successful")
                            print("Number of Book Records:",mycursor.rowcount)
                            break
                    else:
                        print("Sorry!!!")
                        print("The book code",b,"that you had asked to delete is not present in the library")
                        print("Please try again...")
                else:
                    print("Invalid option!")
                    print("Please try again...")
                h=input("Do you want to continue deletion of book records(y/n):") 
                mydb.commit()
        except Exception as e:
            print(e)
        print("---------------------------------------------------------------------------------------------")

        
    def bookupdate():
        print("---------------------------------------------------------------------------------------------")
        import mysql.connector
        try:
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="library")
            mycursor=mydb.cursor()
            h="y"
            while h=="y":
                print("Updation Operations")
                print("1. In terms  of book code") 
                print("2. In terms of book name")
                c=int(input("Enter your choice:"))
                if c==1:
                    l=int(input("Enter the Book code to be updated:"))
                    m=(l,) 
                    v="select * from Book where Book_code=%s"
                    mycursor.execute(v,m)
                    for i in mycursor:
                        if l==i[0]:
                            print("Book code:",i[0])
                            print("Book name:",i[1])
                            print("Author of Book:",i[2])
                            print("Price of Book:",i[3])
                            print("Publisher of Book:",i[4])
                            print("Date of purchase:",i[5])
                            print("Quantity of Book:",i[6])
                        print("Enter the new information")
                        t=input("Enter the name of book:")
                        q=input("Enter the author of book:")
                        e=int(input("Enter the price of book:"))
                        r=input("Enter the publisher of book:")
                        a=input("Enter the date of purchase:")
                        h=int(input("Enter the total quantity of book:"))
                        s=(t,q,e,r,a,h,l)
                        w="update Book set Book_name=%s,Author_of_book=%s,Price_of_book=%s,Publisher_of_book=%s,Date_of_purchase=%s,Total_quantity_of_book=%s where Book_code=%s"
                        mycursor.execute(w,s)
                        print("Updation is Successful")
                        break
                    else:
                        print("Sorry!!!")
                        print("The book code",l," that you had asked to update is not present in the library")
                        print("Please try again...")
                elif c==2:
                    l=input("Enter the Book name to be updated:")
                    m=(l,) 
                    v="select * from Book where Book_name=%s"
                    mycursor.execute(v,m)
                    for i in mycursor:
                        if l==i[1]:
                            print("Book code:",i[0])
                            print("Book name:",i[1])
                            print("Author of Book:",i[2])
                            print("Price of Book:",i[3])
                            print("Publisher of Book:",i[4])
                            print("Date of purchase:",i[5])
                            print("Quantity of Book:",i[6])
                        print("Enter the new information")
                        t=input("Enter the code of book:")
                        q=input("Enter the author of book:")
                        e=int(input("Enter the price of book:"))
                        r=input("Enter the publisher of book:")
                        a=input("Enter the date of purchase:")
                        h=int(input("Enter the total quantity of book:"))
                        s=(t,q,e,r,a,h,l)
                        w="update Book set Book_code=%s,Author_of_book=%s,Price_of_book=%s,Publisher_of_book=%s,Date_of_purchase=%s,Total_quantity_of_book=%s where Book_name=%s"
                        mycursor.execute(w,s)
                        print("Updation is Successful")
                        break
                    else:
                        print("Sorry!!!")
                        print("The book name",l," that you had asked to update is not present in the library")
                        print("Please try again...")
                else:
                    print("Invalid option!")
                    print("Please try again...")
                h=input("Do you want to continue the updation of book records(y/n):")
                mydb.commit()
        except Exception as e:
            print(e)
        print("---------------------------------------------------------------------------------------------")

    
    print("---------------------------------------------------------------------------------------------")   
    try:
        k="y"
        while k=="y":
            print("                                  BOOK RECORD MANAGEMENT")
            print("---------------------------------------------------------------------------------------------")
            print("---------------------------------------------------------------------------------------------")
            print("     Book Records")
            print("1. Add Book Records")
            print("2. Display Book Records")
            print("3. Search Book Records")
            print("4. Delete Book Records")
            print("5. Update Book Records")
            print("6. Exit")
            print("---------------------------------------------------------------------------------------------")
            print("---------------------------------------------------------------------------------------------")
            c=int(input("Enter your choice:"))
            if c==1:
                bookinsertion()
            elif c==2:
                bookdisplay()
            elif c==3:
                booksearch()
            elif c==4:
                bookdelete()
            elif c==5:
                bookupdate()
            elif c==6:
                break
            else:
                print("Invalid option!")
                print("Check once again...")
            k=input("Do you want to continue menu operations of Book Record Management(y/n):")
    except Exception as e:
        print(e)
    print("---------------------------------------------------------------------------------------------")


def Member_Record():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="root")
    if mydb.is_connected():
        print("Connection Successful")
    else:
        print("Connection Unsuccessful")
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="library")
    mycursor=mydb.cursor()
    mycursor.execute("create table Member(Member_code int(90)primary key,Member_name varchar(90),Mobile_number decimal(12,0),Date_of_membership date,Address varchar(90),Book_code int(90))")
    mydb.commit()


    def memberinsertion():
        print("---------------------------------------------------------------------------------------------")
        import mysql.connector
        try:
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="library")
            mycursor=mydb.cursor()
            k="y"
            while k=="y":
                n=int(input("Enter the Member code:"))
                t=input("Enter the Member name:")
                q=int(input("Enter the Mobile number:"))
                d=input("Enter the Date of membership:")
                z=input("Enter the Address:")
                r=int(input("Enter the Book code:"))
                a=(n,t,q,d,z,r)
                w="insert into Member values(%s,%s,%s,%s,%s,%s)"
                mycursor.execute(w,a)
                print("Insertion is Successful")
                k=input("Do you want to continue insertion of member records(y/n):")
                mydb.commit()
        except Exception as e:
            print(e)
        print("---------------------------------------------------------------------------------------------")        


    def memberdisplay():
        print("---------------------------------------------------------------------------------------------")
        import mysql.connector
        try:
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="library")
            mycursor=mydb.cursor()
            mycursor.execute("select * from Member")
            print("******************************************MEMBER*********************************************")
            for i in mycursor:
                print(i)
            print("*********************************************************************************************")
            print("Number of Member Records:",mycursor.rowcount)
        except Exception as e:
            print(e)
        print("---------------------------------------------------------------------------------------------")


    def membersearch():
        print("---------------------------------------------------------------------------------------------")
        import mysql.connector
        try:
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="library")
            mycursor=mydb.cursor()
            g="y"
            while g=="y":
                w=input("Enter the member name to be searched:")
                t=(w,)
                r="select * from Member where Member_name=%s"
                mycursor.execute(r,t)
                for i in mycursor:
                    if i[1]==w:
                        print("Member is present in library")
                        print("Member Details")
                        print("Member code:",i[0])
                        print("Member name:",i[1])
                        print("Mobile number:",i[2])
                        print("Date of membership:",i[3])
                        print("Address:",i[4])
                        print("Book code:",i[5])
                        break
                else:
                    print("Sorry!!!")
                    print("The member",w,"that you had asked to search is not present in  the library")
                    print("Please try again...")
                g=input("Do you want to continue the searching of member records(y/n):")
        except Exception as e:
            print(e)
        print("---------------------------------------------------------------------------------------------")                    


    def memberdelete():
        print("---------------------------------------------------------------------------------------------")
        import mysql.connector
        try:
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="library")
            mycursor=mydb.cursor()
            h="y"
            while h=="y":
                print("Deletion operations")
                print("1. To delete Member name")
                print("2. To delete Member code")
                c=int(input("Enter your choice:"))
                if c==1:
                    u=input("Enter the name of member to be deleted:")
                    m="select * from Member where Member_name=%s"
                    t=(u,)
                    mycursor.execute(m,t)
                    for i in mycursor:
                        if i[1]==u:
                            t=(u,)
                            w="delete from Member where Member_name=%s"
                            mycursor.execute(w,t)
                            print("The member",u,"is deleted")
                            print("Deletion is Successful")
                            print("Number of Member Records:",mycursor.rowcount)
                            break
                    else:
                        print("Sorry!!!")
                        print("The member",u,"that you had asked to delete is not present in the library")
                        print("Please try again...")
                elif c==2:
                    b=int(input("Enter the member code to be deleted:"))
                    m="select * from Member where Member_code=%s"
                    y=(b,)
                    mycursor.execute(m,y)
                    for i in mycursor:
                        if i[0]==b:
                            y=(b,)
                            w="delete from Member where Member_code=%s"
                            mycursor.execute(w,y)
                            print("The member code",b,"is deleted")
                            print("Deletion is Successful")
                            print("Number of Member Records:",mycursor.rowcount)
                            break
                    else:
                        print("Sorry!!!")
                        print("The member code",b,"that you had asked to delete is not present in the library")
                        print("Please try again...")
                else:
                    print("Invalid option!")
                    print("Please try again...")
                h=input("Do you want to continue deletion of member records(y/n):") 
                mydb.commit()
        except Exception as e:
            print(e)
        print("---------------------------------------------------------------------------------------------")    



    def memberupdate():
        print("---------------------------------------------------------------------------------------------")
        import mysql.connector
        try:
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="library")
            mycursor=mydb.cursor()
            h="y"
            while h=="y":
                print("Updation operations")
                print("1. In terms of member code")
                print("2. In terms of member name")
                c=int(input("Enter your choice:"))
                if c==1:
                    l=int(input("Enter the Member code to be updated:"))
                    m=(l,) 
                    v="select * from Member where Member_code=%s"
                    mycursor.execute(v,m)
                    for i in mycursor:
                        if l==i[0]:
                            print("Member code:",i[0])
                            print("Member name:",i[1])
                            print("Mobile number:",i[2])
                            print("Date of membership:",i[3])
                            print("Address:",i[4])
                        print("Enter the new information")
                        t=input("Enter the name of Member:")
                        q=int(input("Enter the mobile number of Member:"))
                        e=input("Enter the date of membership:")
                        r=input("Enter the address of member:")
                        u=int(input("Enter the book code:"))
                        s=(t,q,e,r,u,l)
                        w="update Member set Member_name=%s,Mobile_number=%s,Date_of_membership=%s,Address=%s,Book_code=%s where Member_code=%s"
                        mycursor.execute(w,s)
                        print("Updation is Successful")
                        break
                    else:
                        print("Sorry!!!")
                        print("The member code",l," that you had asked to update is not present in the library")
                        print("Please try again...")
                elif c==2:
                    l=input("Enter the Member name to be updated:")
                    m=(l,) 
                    v="select * from Member where Member_name=%s"
                    mycursor.execute(v,m)
                    for i in mycursor:
                        if l==i[1]:
                            print("Member code:",i[0])
                            print("Member name:",i[1])
                            print("Mobile number:",i[2])
                            print("Date of membership:",i[3])
                            print("Address:",i[4])
                            print("Book code:",i[5])
                        print("Enter the new information")
                        t=input("Enter the code of Member:")
                        q=int(input("Enter the mobile number of Member:"))
                        e=input("Enter the date of membership:")
                        r=input("Enter the address of member:")
                        u=int(input("Ente the book code:"))
                        s=(t,q,e,r,u,l)
                        w="update Member set Member_code=%s,Mobile_number=%s,Date_of_membership=%s,Address=%s,Book_code=%s where Member_name=%s"
                        mycursor.execute(w,s)
                        print("Updation is Successful")
                        break
                    else:
                        print("Sorry!!!")
                        print("The member name",l," that you had asked to update is not present in the library")
                        print("Please try again...")
                else:
                    print("Invalid option")
                    print("Please try again")
                h=input("Do you want to continue the updation of member records(y/n):")
                mydb.commit()
        except Exception as e:
            print(e)
        print("---------------------------------------------------------------------------------------------")
    

    print("---------------------------------------------------------------------------------------------")   
    try:
        k="y"
        while k=="y":
            print("                                  MEMBER RECORD MANAGEMENT")
            print("---------------------------------------------------------------------------------------------")
            print("---------------------------------------------------------------------------------------------")
            print("   Member Records")
            print("1. Add Member Records")
            print("2. Display Member Records")
            print("3. Search Member Records")
            print("4. Delete Member Records")
            print("5. Update Member Records")
            print("6. Exit")
            print("---------------------------------------------------------------------------------------------")
            print("---------------------------------------------------------------------------------------------")
            c=int(input("Enter your choice:"))
            if c==1:
                memberinsertion()
            elif c==2:
                memberdisplay()
            elif c==3:
                membersearch()
            elif c==4:
                memberdelete()
            elif c==5:
                memberupdate()
            elif c==6:
                break
            else:
                print("Invalid option!")
                print("Check once again...")
            k=input("Do you want to continue menu operations of Member Record Management(y/n):")
    except Exception as e:
        print(e)
    print("---------------------------------------------------------------------------------------------")        
          

def Issue_Record():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="root")
    if mydb.is_connected():
         print("Connection Successful")
    else:
        print("Connection Unsuccessful")
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="library")
    mycursor=mydb.cursor()
    mycursor.execute("create table Issue(Issue_code int(90)primary key,Book_code int(90),Book_name varchar(90),Date_of_issue date,Date_of_return date,Member_name varchar(90),Member_code int(90))")
    mydb.commit()

    
    def issueinsertion():
        print("--------------------------------------------------------------------------------------------")
        import mysql.connector
        try:
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="library")
            mycursor=mydb.cursor()
            k="y"
            while k=="y":
                n=int(input("Enter the Issue code:"))
                t=input("Enter the Book code:")
                q=input("Enter the Book name:")
                e=input("Enter the Date of issue:")
                d=input("Enter the Date of return:")
                r=input("Enter the Member name:")               
                z=int(input("Enter the Member code:"))
                a=(n,t,q,e,d,r,z)
                w="insert into Issue values(%s,%s,%s,%s,%s,%s,%s)"
                mycursor.execute(w,a)
                print("Insertion is Successful")
                k=input("Do you want to continue insertion of issue records(y/n):")
                mydb.commit()
        except Exception as e:
            print(e)
        print("---------------------------------------------------------------------------------------------")        


    def issuedisplay():
        print("---------------------------------------------------------------------------------------------")
        import mysql.connector
        try:
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="library")
            mycursor=mydb.cursor()
            mycursor.execute("select * from Issue")
            print("******************************************ISSUE**********************************************")
            for i in mycursor:
                print(i)
            print("*********************************************************************************************")
            print("Number of Issue Records:",mycursor.rowcount)
        except Exception as e:
            print(e)
        print("---------------------------------------------------------------------------------------------")


    def issuesearch():
        print("---------------------------------------------------------------------------------------------")
        import mysql.connector
        try:
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="library")
            mycursor=mydb.cursor()
            g="y"
            while g=="y":
                print("Search Operations")
                print("1. To search book name")
                print("2. To search member name")
                c=int(input("Enter your choice:"))
                if c==1:
                    w=input("Enter the book to be searched:")
                    l="select * from Issue where Book_name=%s"
                    t=(w,)
                    mycursor.execute(l,t) 
                    for i in mycursor:
                        if i[2]==w:
                            print("Book is present in library")
                            print("Book Details")
                            print("Issue code:",i[0])
                            print("Book code:",i[1])
                            print("Book name:",i[2])
                            print("Date of issue:",i[3])
                            print("Date of return:",i[4])
                            print("Member name:",i[5])
                            print("Member code:",i[6])
                            break
                    else:
                            print("Sorry!!!")
                            print("The book",w,"that you had asked to search is not present in  the library records")
                            print("Please try again...")
                elif c==2:
                    w=input("Enter the member to be searched:")
                    l="select * from Issue where Member_name=%s"
                    t=(w,)
                    mycursor.execute(l,t)
                    for i in mycursor:
                        if i[5]==w:
                            print("Member is present in library")
                            print("Member Details")
                            print("Issue code:",i[0])
                            print("Book code:",i[1])
                            print("Book name:",i[2])
                            print("Date of issue:",i[3])
                            print("Date of return:",i[4])
                            print("Member name:",i[5])
                            print("Member code:",i[6])
                            break
                    else:
                        print("Sorry!!!")
                        print("The member",w,"that you had asked to search is not present in  the library records")
                        print("Please try again...")
                else:
                    print("Invalid option!")
                    print("Please try again...")
                g=input("Do you want to continue the searching of issue records(y/n):")
                mydb.commit()
        except Exception as e:
            print(e)
        print("---------------------------------------------------------------------------------------------")                    


    def issuedelete():
        print("---------------------------------------------------------------------------------------------")
        import mysql.connector
        try:
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="library")
            mycursor=mydb.cursor()
            h="y"
            while h=="y":
                print("Deletion operations")
                print("1. To delete Book code")
                print("2. To delete Member code")
                print("3. To delete Issue code")
                c=int(input("Enter your choice:"))
                if c==1:
                    u=input("Enter the code of book to be deleted:")
                    m="select * from Issue where Book_code=%s"
                    t=(u,)
                    mycursor.execute(m,t)
                    for i in mycursor:
                        if i[1]==u:
                            t=(u,)
                            w="delete from Issue where Book_code=%s"
                            mycursor.execute(w,t)
                            print("The book code",u,"is deleted")
                            print("Deletion is Successful")
                            print("Number of Issue Records:",mycursor.rowcount)
                            break
                    else:
                        print("Sorry!!!")
                        print("The book code",u,"that you had asked to delete is not present in the library records")
                        print("Please try again...")

                elif c==2:
                    u=int(input("Enter the code of member to be deleted:"))
                    m="select * from Issue where Member_code=%s"
                    t=(u,)
                    mycursor.execute(m,t)
                    for i in mycursor:
                        if i[6]==u:
                            t=(u,)
                            w="delete from Issue where Member_code=%s"
                            mycursor.execute(w,t)
                            print("The member code",u,"is deleted")
                            print("Deletion is Successful")
                            print("Number of Issue Records:",mycursor.rowcount)
                            break
                    else:
                        print("Sorry!!!")
                        print("The member code",u,"that you had asked to delete is not present in the library records")
                        print("Please try again...")
                elif c==3:
                    b=int(input("Enter the code of issue to be deleted:"))
                    m="select * from Issue where Issue_code=%s"
                    y=(b,)
                    mycursor.execute(m,y)
                    for i in mycursor:
                        if i[0]==b:
                            y=(b,)
                            w="delete from Issue where Issue_code=%s"
                            mycursor.execute(w,y)
                            print("The issue code",b,"is deleted")
                            print("Deletion is Successful")
                            print("Number of Issue Records:",mycursor.rowcount)
                            break
                    else:
                        print("Sorry!!!")
                        print("The issue code",b,"that you had asked to delete is not present in the library records")
                        print("Please try again...")
                else:
                    print("Invalid option!")
                    print("Please try again...")
                h=input("Do you want to continue deletion of issue records(y/n):") 
                mydb.commit()
        except Exception as e:
            print(e)
        print("---------------------------------------------------------------------------------------------")    



    def issueupdate():
        print("---------------------------------------------------------------------------------------------")
        import mysql.connector
        try:
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="library")
            mycursor=mydb.cursor()
            h="y"
            while h=="y":
                print("Updation operations")
                print("1. In terms of issue code")
                print("2. In terms of book code")
                print("3. In terms of member code")
                c=int(input("Enter your choice:"))
                if c==1:
                    l=int(input("Enter the Issue code to be updated:"))
                    m=(l,) 
                    v="select * from Issue where Issue_code=%s"
                    mycursor.execute(v,m)
                    for i in mycursor:
                        if l==i[0]:
                            print("Issue code:",i[0])
                            print("Book code :",i[1])
                            print("Book name:",i[2])
                            print("Date of issue:",i[3])
                            print("Date of return:",i[4])
                            print("Member name:",i[5])
                            print("Member code:",i[6])
                        print("Enter the new information")
                        t=int(input("Enter the book code:"))
                        q=input("Enter the book name:")
                        e=input("Enter the date of issue:")
                        f=input("Enter the date of return:") 
                        r=input("Enter the name of member:")
                        u=int(input("Enter the member code:"))
                        s=(t,q,e,f,r,u,l)
                        w="update Issue set Book_code=%s,Book_name=%s,Date_of_issue=%s,Date_of_return=%s,Member_name=%s,Member_code=%s where Issue_code=%s"
                        mycursor.execute(w,s)
                        print("Updation is Successful")
                        break
                    else:
                        print("Sorry!!!")
                        print("The issue code",l," that you had asked to update is not present in the library records")
                        print("Please try again...")
                elif c==2:
                    l=int(input("Enter the Book code to be updated:"))
                    m=(l,) 
                    v="select * from Issue where Book_code=%s"
                    mycursor.execute(v,m)
                    for i in mycursor:
                        if l==i[1]:
                            print("Issue code:",i[0])
                            print("Book code :",i[1])
                            print("Book name:",i[2])
                            print("Date of issue:",i[3])
                            print("Date of return:",i[4])
                            print("Member name:",i[5])
                            print("Member code:",i[6])
                        print("Enter the new information")
                        t=int(input("Enter the issue code:"))
                        q=input("Enter the book name:")
                        e=input("Enter the date of issue:")
                        f=input("Enter the date of return:") 
                        r=input("Enter the name of member:")
                        u=int(input("Enter the member code:"))
                        s=(t,q,e,f,r,u,l)
                        w="update Issue set Issue_code=%s,Book_name=%s,Date_of_issue=%s,Date_of_return=%s,Member_name=%s,Member_code=%s where Book_code=%s"
                        mycursor.execute(w,s)
                        print("Updation is Successful")
                        break
                    else:
                        print("Sorry!!!")
                        print("The book code",l," that you had asked to update is not present in the library records")
                        print("Please try again...")
                elif c==3:
                    l=int(input("Enter the Member code to be updated:"))
                    m=(l,) 
                    v="select * from Issue where Member_code=%s"
                    mycursor.execute(v,m)
                    for i in mycursor:
                        if l==i[6]:
                            print("Issue code:",i[0])
                            print("Book code :",i[1])
                            print("Book name:",i[2])
                            print("Date of issue:",i[3])
                            print("Date of return:",i[4])
                            print("Member name:",i[5])
                            print("Member code:",i[6])
                        print("Enter the new information")
                        u=int(input("Enter the issue code:"))
                        t=int(input("Enter the book code:"))
                        q=input("Enter the book name:")
                        e=input("Enter the date of issue:")
                        f=input("Enter the date of return:") 
                        r=input("Enter the name of member:")
                        s=(t,q,e,f,r,u,l)
                        w="update Issue set Issue_code=%s,Book_code=%s,Book_name=%s,Date_of_issue=%s,Date_of_return=%s,Member_name=%s where Member_code=%s" 
                        mycursor.execute(w,s)
                        print("Updation is Successful")
                        break
                    else:
                        print("Sorry!!!")
                        print("The member code",l," that you had asked to update is not present in the library records")
                        print("Please try again...")
                else:
                    print("Invalid option!")
                    print("Please try again...")
                h=input("Do you want to continue the updation of issue records:")
                mydb.commit()
        except Exception as e:
            print(e)
        print("---------------------------------------------------------------------------------------------")


    print("---------------------------------------------------------------------------------------------")   
    try:
        k="y"
        while k=="y":
            print("                                  ISSUE/RETURN INFORMATION")
            print("---------------------------------------------------------------------------------------------")
            print("---------------------------------------------------------------------------------------------")
            print(" Issue/Return Records")
            print("1. Add Issue Records")
            print("2. Display Issue Records")
            print("3. Search Issue Records")
            print("4. Delete Issue Records")
            print("5. Update Issue Records")
            print("6. Exit")
            print("---------------------------------------------------------------------------------------------")
            print("---------------------------------------------------------------------------------------------")
            c=int(input("Enter your choice:"))
            if c==1:
                issueinsertion()
            elif c==2:
                issuedisplay()
            elif c==3:
                issuesearch()
            elif c==4:
                issuedelete()
            elif c==5:
                issueupdate()
            elif c==6:
                break
            else:
                print("Invalid option!")
                print("Check once again...")
            k=input("Do you want to continue menu operations of Issue/Return Information(y/n):")
    except Exception as e:
        print(e)
    print("---------------------------------------------------------------------------------------------")        

          
try:
    k="y"
    while k=="y":
        print("                                    LIBRARY MANAGEMENT")
        print("---------------------------------------------------------------------------------------------")
        print("---------------------------------------------------------------------------------------------")
        print("    LIBRARY RECORDS")
        print("1. BOOK RECORD MANAGEMENT")
        print("2. MEMBER RECORD MANAGEMENT")
        print("3. ISSUE/RETURN INFORMATION")
        print("4. EXIT")
        print("---------------------------------------------------------------------------------------------")
        print("---------------------------------------------------------------------------------------------")
        c=int(input("Enter your choice:"))
        if c==1:
            Book_Record()
        elif c==2:
            Member_Record()
        elif c==3:
            Issue_Record()
        elif c==4:
            print("##GOOD BYE##")
            print("SEE YOU NEXT TIME...")
            break
        else:
            print("Invalid option!")
            print("Check once again...")
        k=input("Do you want to continue menu operations of Library Management(y/n):")
        print("---------------------------------------------------------------------------------------------")   
except Exception as e:
    print(e)


  
        
          
        
        
          
