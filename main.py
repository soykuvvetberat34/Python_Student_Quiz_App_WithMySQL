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
    print("Sistemi kapatmak için için (-1) yaz")
    check_user=int(input("Which your user type(1/2/-1):"))

    if check_user==2:
        
        check_teacher_password=input("şifrenizi girin:")
        
        
        if cm.check_authorized_user(check_teacher_password)==1:
            while True:
            
                print("--------------Teacher info system--------------")    
                print("\n")
                print("What do you want to do?")
                print("1)New Question add")
                print("2)Delete a question")
                print("3)Update a question")
                print("4)See students scores")
                print("5)Tüm sorulari gör")
                print("Sistemi kapatmak için (-1) yaz")
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
                    delete_question=int(input("Silmek istediğiniz sorunun id numarası nedir:"))
                    cm.delete_Question(delete_question)
                if decision==3:
                    q_id=int(input("Güncellemek istediğiniz sorunun id numarasi nedir:"))
                    mycursor.execute("SELECT idquestions FROM questions")
                    result=mycursor.fetchall()
                    for k in result:
                        for j in k:
                            if j==q_id:
                                print("1)Soruyu güncelle")
                                print("2)Cevabı güncelle")
                                q_dec=int(input("Yapmnak istediğiniz işlem nedir?(1/2):"))
                                if q_dec==1:
                                    new_q=input("yeni soruyu girin:")
                                    cm.Update_Questions(q_dec,q_id,new_q)
                                if q_dec==2:
                                    new_q=input("Yeni cevabi girin:")
                                    cm.Update_Questions(q_dec,q_id,new_q)    
                
                if decision==4:
                    stnum=int(input("puanini öğrenmek istediğiniz öğrencinin numarasini girin:"))
                    cm.see_students_score(stnum)
                if decision==5:
                    cm.see_Questions()
                if decision==-1:
                    print("sistem kapatildi!")
                    break
                else:
                    print("\nHatali işlem")


            

    
    if check_user==1:
        decision2=int(input("öğrenci kayidiniz var mi?(Hayir(1)/Evet(2)):"))
        if decision2==1:
            name1=input("Adinizi giriniz:")
            surname1=input("Soyadinizi giriniz:")
            num1=int(input("Numaranizi giriniz:"))
            cm.insert_Student(name1,surname1,num1)
        if decision2==2:
            num3=int(input("Giriş yapmak için öğrenci numaranizi giriniz:"))
            cm.check_student(num3)
    
    if check_user==-1:
        print("Çikiş yapildi!")
        break
    else:
        print("HATA tekrar dene")
mydb.close
        
        