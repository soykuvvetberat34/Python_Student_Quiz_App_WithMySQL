import pymysql.cursors
import commands as cm

mydb=pymysql.connect(
    host="localhost",
    user="root",
    password="34.bjkberat",
    database="quiz"
)
mycursor=mydb.cursor()
while True:
    print("\n-----------------------QuizApp-----------------------\n")
    print("User types:student(1) teacher(2)")
    print("If you want to exit press (-1)")
    check_user=int(input("Which your user type(1/2/-1):"))

    if check_user==2:
        
        check_teacher_password=input("Please enter your password:")
        
        
        if cm.check_authorized_user(check_teacher_password)==1:
            while True:
            
                print("--------------Teacher info system--------------")    
                print("\n")
                print("What do you want to do?")
                print("1)New Question add")
                print("2)Delete a question")
                print("3)Update a question")
                print("4)See students scores")
                print("5)Look at the all questions")
                print("If you want to exit press (-1)")
                decision=int(input("Which operating you want to make(1/2/3/4/5):"))
                if decision==1:
                    Question=input("Please enter the Question:")
                    Answer=input("please enter the question's answer:")
                    Choices=[]
                    for i in range(1,6):
                        add=input(f"please enter the choise {i}:")
                        Choices.append(add)
                    cm.insert_Question(Question,Answer)
                
                if decision==2:
                    delete_question=int(input("What is the id of question you want to delete?:"))
                    cm.delete_Question(delete_question)
                if decision==3:
                    q_id=int(input("What is the id of question you want to update?:"))
                    mycursor.execute("SELECT idquestions FROM questions")
                    result=mycursor.fetchall()
                    for k in result:
                        for j in k:
                            if j==q_id:
                                print("1)Update the question")
                                print("2)Update the answer")
                                q_dec=int(input("Which action do you want to take?(1/2):"))
                                if q_dec==1:
                                    new_q=input("Enter the new question:")
                                    cm.Update_Questions(q_dec,q_id,new_q)
                                if q_dec==2:
                                    new_q=input("Enter the new question:")
                                    cm.Update_Questions(q_dec,q_id,new_q)    
                
                if decision==4:
                    stnum=int(input("Enter the ID of the student whose score you want to know:"))
                    cm.see_students_score(stnum)
                if decision==5:
                    cm.see_Questions()
                if decision==-1:
                    print("system shut down!")
                    break


            

    
    if check_user==1:
        decision2=int(input("Do you have student number?(No(1)/Yes(2)):"))
        if decision2==1:
            print("sign in")
            name1=input("Please enter your name:")
            surname1=input("Please enter your surname:")
            num1=int(input("please enter your student number:"))
            cm.insert_Student(name1,surname1,num1)
        if decision2==2:
            print("Log in")
            print("\n")
            num3=int(input("Please enter your student number:"))
            cm.check_student(num3)
    
    if check_user==-1:
        print("exited!")
        break
    else:
        print("error, try again!")
mydb.close
        
        
