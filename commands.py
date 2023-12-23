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
        print(f"işlem başarili soru:{Question} ve cevap:{Answer} eklendi!")
    except pymysql.connect.Error as err:
        print("HATA KODU:",err)
    except pymysql.err.InterfaceError as err2:
        print("Hata:",err2)
    finally:
        
        print("Veritabani kapatildi")
        
def check_authorized_user(check_teacher_password):
    kontrol=0
    mycursor.execute("SELECT AuthorizedUserPassword FROM authorizedusers")
    
    result=mycursor.fetchall()
    for i in result:
        for k in i:
            if k==check_teacher_password:
                print("\nGiriş başarili Hoşgeldiniz!")
                print("Yönetici olarak giriş yaptiniz.\n")
                kontrol=1
            else:
                print("\n")
    
    print("HATALİ İŞLEM")
    if(kontrol==1):
        return 1
    try:
        mydb.commit()
    except:
        print("Hatali işlem")
    finally:
        print("işlem bitirildi.")
        

def delete_Question(questionid):
    sql2="DELETE FROM questions where idquestions=%s"
    value2=questionid
    mycursor.execute(sql2,value2)
    try:
        print("soru silindi")
        mydb.commit()
    except:
        print("\n")
    finally:
        
        print("Veritabani kapatildi")

def see_Questions():
    mycursor.execute("SELECT * FROM questions")
    result2=mycursor.fetchall()
    
    for y in result2:
        print(f"soru id:{y[0]} soru:{y[1]} doğru cevap:{y[2]}")
    try:
        print("işlem başarili")
        mydb.commit()
    except:
        print("HATALİ İŞLEM")
    finally:
        
        print("Veritabani kapatildi")

def Update_Questions(q_dec,q_id,new_q):
    if q_dec==1:
        sql3="UPDATE questions SET questions=%s WHERE idquestions=%s"
        values3=(new_q,q_id)
        mycursor.execute(sql3,values3)
        try:
            print("işlem başarili")
            mydb.commit()
        except:
            print("HATALİ İŞLEM")
        finally:
            print("Veritabani kapatildi")
            
    if q_dec==2:
        sql4="UPDATE questions SET answer=%s WHERE idquestions=%s"
        values4=(new_q,q_id)
        mycursor.execute(sql4,values4)  
        try:
            print("işlem başarili")
            mydb.commit()
        except:
            print("HATALİ İŞLEM")
        finally:
            print("Veritabani kapatildi")
              
    else:
        print("Bir hata oluştu") 
        
def insert_Student(name1,surname1,num1):
    sql5="INSERT INTO students(studentsnumber,studentsName,studentsSurname,studentsPoint) VALUE(%s,%s,%s,%s)"
    values5=(num1,name1,surname1,0)
    mycursor.execute(sql5,values5)
    try:
        print(f" {num1} numarali öğrenci {name1} {surname1} eklendi")
        mydb.commit()
    except:
        print("Süreçte hata oluştu")
    finally:
        
        print("Veritabani kapatildi")
    
def check_student(num3):
    mycursor.execute("SELECT studentsnumber FROM students")
    result4=mycursor.fetchall()
    for r in result4:
        for g in r:
            if g==num3:
                print("\n")
                while True:
                    print("------------HOŞGELDİN------------")
                    print("Yapacağiniz işlemi seçin")
                    print("1)Sorulari çöz")
                    print("2)Puanini gör")
                    print("Çikiş yap (-1)")
                    decision4=int(input("Karariniz nedir?(1/2/-1):"))
                    if decision4==1:
                        choices=[]
                        point=0
                        mycursor.execute("SELECT questions FROM questions")
                        result5=mycursor.fetchall()
                        for d in result5:
                            for f in d:
                                print(f"Soru:{f}")
                                answ=input("Cevabin nedir:")
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
                                print(f"PUANIN:{s}")
                    if decision4==-1:
                        break
                    
            else:
                print("HATALİ GİRİŞ")
    
    try:
        mydb.commit()
        
    except:
        print("HATALİ İŞLEM") 
    
        
def see_students_score(stnum):
    sql8="SELECT studentsPoint FROM students WHERE studentsnumber=%s"
    values8=stnum
    mycursor.execute(sql8,values8)
    result8=mycursor.fetchall()
    for x in result8:
        for c in x:
            print(f"{stnum} numarali öğrencinin puani:{c}")    
    try:
        mydb.commit()
        print("işlem başari ile bitirildi")
    except:
        print("Hatali işlem")
        
   
    

    