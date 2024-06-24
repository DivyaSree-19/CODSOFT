#contacts_details={}
import mysql.connector

db=mysql.connector.connect(host="localhost",user="root",password="",database="contact_deatils")
cursor=db.cursor()

def create():
    name=input("enter ur name:")
    contact_no=int(input("enter ur phone no.:"))
    cursor.execute("insert into contacts (name,contact_no) values(%s,%s)",(name,contact_no))
    db.commit()
    print("succesfully created.....")

def search():
    name=input("enter ur name to be Search:")
    cursor.execute("select name,contact_no from contacts where name=%s",(name,))
    result=cursor.fetchall()
    if result:
        print("Search results:")
        for name, contact_no in result:
            print(f"Name: {name},\n Phone Number: {contact_no}")
    else:
        print("Contact not found.")
    
def update():
    name = input("Enter the current name: ")
    cursor.execute("select name,contact_no from contacts where name=%s",(name,))
    result = cursor.fetchone()
    if result:
        new_name = input("\nEnter the new name: ")
        new_contact_no = input("Enter the new phone number: ")
        cursor.execute("UPDATE contacts SET name = %s, contact_no = %s where name = %s", (new_name, new_contact_no,name))
        db.commit()
        print("Contact successfully updated.")
    else:
        print("Contact not found.")

    
def delete():
    name = input("Enter your name: ")
    cursor.execute("select contact_no FROM contacts where name = %s", (name,))
    result = cursor.fetchone()
    if result:
        cursor.execute("DELETE FROM contacts where name = %s", (name,))
        db.commit()
        print("Contact successfully deleted.")
    else:
        print("Contact not found.")

def print_all_contacts():
    cursor.execute("SELECT name, contact_no FROM contacts")
    results = cursor.fetchall()
    if results:
        print("All contacts:")
        for name, contact_no in results:
            print(f"Name: {name}, Phone Number: {contact_no}")
    else:
        print("No contacts available.")
    
while True:
    print("\n\n1.Create\n2.Search\n3.Update\n4.Delete\n5.To_print_AllData\n6.exit")
    ch=int(input("\n Enter Your Choice:"))
    if ch==1:
        create()
    elif ch==2:
        search()
    elif ch==3:
        update()
    elif ch==4:
        delete()
    elif ch==5:
        print_all_contacts()
    elif ch==6:
        print("successfully Exist")
        break
    else:
        print("wrong choice...")
      
        
