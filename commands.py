import pymysql.cursors

mydb=pymysql.connect(
    host="localhost",
    user="root",
    password="34.bjkberat",
    database="quiz"
)
mycursor=mydb.cursor()

def insert_Question(Question,Answer):
    sql="INSERT INTO questions(questions,answer) VALUE(%s,%s)"
    values=(Question,Answer)
    mycursor.execute(sql,values)
    
    try:
        mydb.commit()
        print(f"Process went with succes Question:{Question} and answer:{Answer} added!")
    except pymysql.connect.Error as err:
        print("ERROR CODE:",err)
    except pymysql.err.InterfaceError as err2:
        print("ERROR:",err2)
    
        
def check_authorized_user(check_teacher_password):
    kontrol=0
    mycursor.execute("SELECT AuthorizedUserPassword FROM authorizedusers")
    
    result=mycursor.fetchall()
    for i in result:
        for k in i:
            if k==check_teacher_password:
                print("\nLogin process went with succes!")
                print("You are logged in as teacher!\n")
                kontrol=1
            else:
                print("\n")
    
    if(kontrol==1):
        return 1
    try:
        mydb.commit()
    except:
        print("process went wrong")
        

def delete_Question(questionid):
    sql2="DELETE FROM questions where idquestions=%s"
    value2=questionid
    mycursor.execute(sql2,value2)
    try:
        print("Question is deleted")
        mydb.commit()
    except:
        print("\n")


def see_Questions():
    mycursor.execute("SELECT * FROM questions")
    result2=mycursor.fetchall()
    
    for y in result2:
        print(f"Question id:{y[0]} Question:{y[1]} True answer:{y[2]}")
    try:
        print("Process successed")
        mydb.commit()
    except:
        print("Process went wrong")

def Update_Questions(q_dec,q_id,new_q):
    if q_dec==1:
        sql3="UPDATE questions SET questions=%s WHERE idquestions=%s"
        values3=(new_q,q_id)
        mycursor.execute(sql3,values3)
        try:
            print("Process successed")
            mydb.commit()
        except:
            print("Process went wrong")
            
    if q_dec==2:
        sql4="UPDATE questions SET answer=%s WHERE idquestions=%s"
        values4=(new_q,q_id)
        mycursor.execute(sql4,values4)  
        try:
            print("Process successed")
            mydb.commit()
        except:
            print("Process went wrong")

              
    else:
        print("Something went wrong") 
        
def insert_Student(name1,surname1,num1):
    sql5="INSERT INTO students(studentsnumber,studentsName,studentsSurname,studentsPoint) VALUE(%s,%s,%s,%s)"
    values5=(num1,name1,surname1,0)
    mycursor.execute(sql5,values5)
    try:
        print(f" {num1}-{name1} {surname1} student added")
        mydb.commit()
    except:
        print("Something went wrong")
    
def check_student(num3):
    mycursor.execute("SELECT studentsnumber FROM students")
    result4=mycursor.fetchall()
    for r in result4:
        for g in r:
            if g==num3:
                print("\n")
                while True:
                    print("------------Welcome-----------")
                    print("Which action do you want to take?")
                    print("1)Solve the questions")
                    print("2)See your score")
                    print("exit(-1)")
                    decision4=int(input("What's your choice?(1/2/-1):"))
                    if decision4==1:
                        choices=[]
                        point=0
                        mycursor.execute("SELECT questions FROM questions")
                        result5=mycursor.fetchall()
                        for d in result5:
                            for f in d:
                                print(f"Question:{f}")
                                answ=input("What's your answer?:")
                                choices.append(answ)
                        mycursor.execute("SELECT answer FROM questions")
                        result6=mycursor.fetchall()
                        for q in result6:
                            for p in q:
                                for t in choices:
                                    if p==t:
                                        point+=1
                                    else:
                                        continue
                        last_point=point
                        sql6="UPDATE students SET studentsPoint=%s"
                        if last_point<0:
                            values6=last_point*-1
                        else:
                            values6=last_point
                        mycursor.execute(sql6,values6)
                        print(f"puaniniz:{values6}")

                            

                            
                    if decision4==2:
                        sql7="SELECT studentsPoint FROM students WHERE studentsnumber=%s"
                        value7=(num3)
                        mycursor.execute(sql7,value7)
                        result7=mycursor.fetchall()
                        for j in result7:
                            for s in j:
                                print(f"Your score:{s}")
                    if decision4==-1:
                        break
                    
    
    try:
        mydb.commit()
        
    except:
        print("Something went wrong") 
    
        
def see_students_score(stnum):
    sql8="SELECT studentsPoint FROM students WHERE studentsnumber=%s"
    values8=stnum
    mycursor.execute(sql8,values8)
    result8=mycursor.fetchall()
    for x in result8:
        for c in x:
            print(f"Student with this id:{stnum}, student's score:{c}")    
    try:
        mydb.commit()
        print("Process went succes")
    except:
        print("Something wnet wrong")
        
   
    

    
