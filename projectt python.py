import random
def x(q):
n=""
for j in q:
if ord(j)<=122 and ord(j)>=97:
n+=j
else:
n+=chr(ord(j)+32)
return n
print("::: Welcome to the quiz 
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::")
print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::")
print("::: There will be 5 rounds and in each round random quiz questions 
will be displayed to the participant. :::")
print("::: Participant have to answer whether the given question/statement 
is True or False. ::::::::::::::::::::::")
print("::: press 1 to continue ::: or ::: press any other digit to exit 
:::::::::::::::::::::::::::::::::::::::::::")
print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::")
f=int(input())
print()
print()
a={"Microsoft Word is an example of utility software.":"false",
"Programs that make your computer run better are considered to be 
operating system programs.":"false",
"Application software consist of programs that perform specific tasks 
for users. Examples include Microsoft Word, Internet Explorer, and 
Microtype 5.":"true",
"Software is available to help you with all kinds of tasks.":"true",
"Software is a series of instructions that tells the computer hardware 
what to do and how to do it.":"true",
"The operating system is a set programs that coordinate all the 
activities among all hardware devices.":"true",
"Utility software is system software designed to help analyze, 
configure, optimize or maintain a computer.":"true",
"Application software focuses on how the computer operates.":"false",
"Utility software is generally used by people with an advanced level of 
computer knowledge.":"true",
"Is Microsoft Windows an application software?":"false"}
c=""
d=0
s=y=0
if f==1:
while d!=-1:
k=random.choice(list(a.keys()))
if k not in c:
c+=k
s+=1
print("Q"+str(s)+")",k+" (True/False)")
e=input()
if x(e)==a[k]:
y+=5
print("Correct! Well done")
else:
print("Incorrect! You got it wrong")
print()
print()
if s==5:
break
print("congratulations! your score is:",y)
else:
print("Thank you for coming")
