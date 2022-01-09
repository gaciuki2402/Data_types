class Grading:
    def pupilDetails(self):
        self.studentList=[]
        self.number_of_students=eval(input("Enter the number of students in class:"))
        for students in range(self.number_of_students): #range(2)
            name=input("Name:")
            age=input("Age:")
            adm=input("AdmNo:")
            myDict={
                "Name":name,
                "Age":age,
                "Adm":adm
            }
            self.studentList.append(myDict)
        print(self.studentList)
    def resultslip(self):
        for student in range(len(self.studentList)):#[1,2,3,4,[5,8],]
            #[{'Name': 'grace', 'Age': '21', 'Adm': 'tu01'}, {'Name': 'Irene', 'Age': '21', 'Adm': 'tu02'}]=2
            print(f"Name:{self.studentList[student]['Name']}\nAdmNo:{self.studentList[student]['Adm']}")
            english=eval(input("English"))
            math=eval(input("Mathematics"))
            kiswahili=eval(input("Kiswahili"))
            science=eval(input("Science"))
            sst=eval(input("Social Studies"))
            total_marks=english+kiswahili+math+science+sst
            mean_marks=total_marks/5
            print(f"English:{english}\nKiswahili:{kiswahili}\nMaths:{math}\nScience:{science}\nSst:{sst}")
            print(f"Total Marks:{total_marks}\nMean Marks:{mean_marks}")
            if mean_marks>=0 and mean_marks<=100:
                if mean_marks>80:
                    print("Grade:A")
                elif mean_marks>=74 and mean_marks<=80:
                    print("Grade :A-")
                elif mean_marks>=69 and mean_marks<=73:
                    print("Grade:B+")
                elif mean_marks>=63 and mean_marks<=68:
                    print("Grade:B")
                elif mean_marks>=54 and mean_marks<=62:
                    print("Grade:B-")
                elif mean_marks>=47 and mean_marks<=53:
                    print("Grade:C+")
                elif mean_marks>=39 and mean_marks<=46:
                    print("Grade:C")
                elif mean_marks>=34 and mean_marks<=33:
                    print("Grade:C-")
                elif mean_marks>=28 and mean_marks<=33:
                    print("Grade:D+")
                elif mean_marks>=24 and mean_marks<=27:
                    print("Grade:D")
                elif mean_marks>=14 and mean_marks<23:
                    print("Grade:E")

                print("-"*10,"End","-"*10)
G1=Grading()
G1.pupilDetails()
G1.resultslip()

