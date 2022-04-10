#import module
import smtplib
import getpass
import os

from email.mime.multipart import MIMEMultipart

print("Selamat Datang di Program Pengirim Email Otomatis")
print("-----Silahkan Login-----")
email = str(input("Silahkan masukan email : "))
email_password = getpass.getpass("Silahkan masukan password email : ")
os.system('cls')
print("-----Login Berhasil-----")

#fungsi add email
def add_email():
    email = str(input("Silahkan Masukkan Email Penerima : "))
    with open ('receiver_list.txt', 'a') as filex:
        filex.write("\n{}" .format(email))
    print("Email Berhasil ditambahkan.")

#fungsi list email 
def list_email():
    with open ('receiver_list.txt', 'r') as filex:
        list = filex.read()
        print(list)

#fungsi receiver email
def recipient_email():
    with open('receiver_list.txt','r') as filex:
       recipient = filex.readlines()

#fungsi send email
def send_email():
    mails = MIMEMultipart()
    mails ['From'] = email
    mails ['Subject'] = "Email Otomatis"
    
    text = str(input("Silahkan Masukkan Pesan : "))

    with open ('receiver_list.txt', 'r') as filex:
        reciepients = filex.readlines()
        mails ['To'] = reciepients  
    
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(email, email_password)
        server.sendmail(email, reciepients, text)
        server.close()
        print("Email Berhasil Dikirim")
        
    except Exception:
        print("Error : " %Exception)
        
        
while True:
    print("\n1. Tambah Email\n2. List Email Penerima\n3. Kirim Email Otomatis\n4. Keluar")
    menu = int(input("\nSilahkan pilih menu layanan :"))
    os.system('cls')
    
    if menu == 1:
        while True:
            if add_email() == False:
                continue
            else:
                break
        continue
    
    elif menu == 2:
        while True:
            if list_email() == False:
                continue
            else:
                break
        continue
    elif menu == 3:
        while True:
            if send_email() == False:
                continue
            else:
                break
    elif menu == 4:
        print("Program Selesai, Stay Safe")
        break
    else:
        print("Mohon maaf, menu tidak tersedia")
