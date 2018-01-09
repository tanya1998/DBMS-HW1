import re
class Student(object):
    def __init__(self,rollno,name,marks):
        self.rollno = rollno
        self.name   = name
        self.marks  = marks
    def filewrite(self,filename):
        file = open(filename,"w")
        file.write(self.rollno+"\t"+str(self.name)+"\t"+str(self.marks))
    def findsum(self,fieldname,filename):
        file = open(filename,"r")
        sum =0;
        for line in file:
            l = line
            values = re.split(r'\t+', l.rstrip('\n'))
            if(fieldname == "Roll Number"):
                sum+=int(values[0])
            elif(fieldname == "Name"):
                print("Invalid Fieldname:- Can't Add Strings")
                break
            elif(fieldname == "Marks"):
                sum+=int(values[2])
            else:
                print("Invalid Fieldname :- Fieldname Not present")
        print("The sum is :- "+str(sum))
    def fileread(self,filename):
        file = open(filename,"r")
        for line in file:
            print(line)


if __name__=='__main__':
	s = Student(0,"",0)
	while(True):
		print("\n\n\nWelcome to the Student Database");
		print("\nMENU: ")
		print("Enter P for printing the Student data")
		print("Enter S for finding sum of the all values in a field")
		print("Press Q to exit")
		
		ch = input("\n\nPress a Key: ")
		
		if(ch=="P"):
			print("\nHere is the data of all files:")
			s.fileread("Student.txt")
			
		elif(ch=="S"):
			print("The possible field names are: Roll Number, Name, Marks")
			field = input("Enter Field Name: ")
			s.findsum(field,"Student.txt")
		elif(ch=='Q'):
			break
		else:
			print("\nPlease enter a valid option")
            
    
