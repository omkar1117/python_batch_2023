print("Program for biodata information")

name = input("Enter your First Name:")
lname = input("Enter your Last Name:")
email = input("Enter your email address:")
phone = input("Enter your phone number:")
address = input("Enter your address:")

fp = open("stu_info.txt", "w")
fp.write("First Name of the Student :%s \n" %name)
fp.write("Last Name of the Student :%s \n" %lname)
fp.close()
