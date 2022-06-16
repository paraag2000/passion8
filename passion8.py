from tkinter import *
from tkinter import messagebox
import numpy as np
import pandas as pd

l1=['Active Listening','Adaptability','Administration','Analysis','Assertiveness','Attentive',
    'Cleanliness','Collaboration','Communication','Computer Ability','Confidence','Coordination',
    'Creativity','Critical Thinking','Customer Service','Data Management','Decision Making','Dedication',
    'Empathetic','Enthusiastic','Entrepreneurial','Ethical','Expressive','Flexible','Helping','History',
    'Independant','Innovative','Leadership','Logical Thinking','Management','Math','Motivational','Patriotic',
    'Observation','Organizational','Patience','Problem Solving','Physical','Planning','Presentation',
    'Public Speaking','Relationship Building','Spatial Awareness','Situational Awareness',
    'Strategical','Sense of Humour','Time Management','Tutoring','Work Ethics','Writing']

Passions=['Accounting','Actor','Archaelogist','Architect','Army','Artist',
          'Athelete','Bartender','Business Manager','Cabin Crew','Chef',
          'Commercial Pilot','Counsellor','Detective','Digital Media','Doctor',
          'Enterpreneur','Ethical Hacker','Fashion Designer','Fire Fighter',
          'Human Resources','Interior Designer','Journalist','Lawyer','Marketing',
          'Mechanic','Modelling','Photographer','Politician','Professional Trainer',
          'Programmer','Psychologist','Real Estate Agent','Stand Up Comedian','Stock Broker',
          'Teacher','Wedding Planner','Writer']

l2=[]
for x in range(0,len(l1)):
    l2.append(0)

# TESTING DATA
tr=pd.read_csv("PassionTesting.csv")
tr.replace({'Passions':{'Accounting':0,'Actor':1,'Archaelogist':2,'Architect':3,'Army':4,
                        'Artist':5,'Athelete':6,'Bartender':7,'Business Manager':8,'Cabin Crew':9,
                        'Chef':10,'Commercial Pilot':11,'Counsellor':12,'Detective':13,
                        'Digital Media':14,'Doctor':15,'Enterpreneur':16,'Ethical Hacker':17,
                        'Fashion Designer':18,'Fire Fighter':19,'Human Resources':20,'Interior Designer':21,
                        'Journalist':22,'Lawyer':23,'Marketing':25,'Mechanic':26,'Modelling':27,'Photographer':28,
                        'Politician':29,'Professional Trainer':30,'Programmer':31,'Psychologist':32,'Real Estate Agent':33,
                        'Stand Up Comedian':34,'Stock Broker':35,'Teacher':36,'Wedding Planner':38,'Writer':39}},inplace=True)

X_test= tr[l1]
y_test = tr[["Passions"]]
np.ravel(y_test)

# TRAINING DATA
df=pd.read_csv("PassionTraining.csv")

df.replace({'Passions':{'Accounting':0,'Actor':1,'Archaelogist':2,'Architect':3,'Army':4,
                        'Artist':5,'Athelete':6,'Bartender':7,'Business Manager':8,'Cabin Crew':9,
                        'Chef':10,'Commercial Pilot':11,'Counsellor':12,'Detective':13,
                        'Digital Media':14,'Doctor':15,'Enterpreneur':16,'Ethical Hacker':17,
                        'Fashion Designer':18,'Fire Fighter':19,'Human Resources':20,'Interior Designer':21,
                        'Journalist':22,'Lawyer':23,'Marketing':25,'Mechanic':26,'Modelling':27,'Photographer':28,
                        'Politician':29,'Professional Trainer':30,'Programmer':31,'Psychologist':32,'Real Estate Agent':33,
                        'Stand Up Comedian':34,'Stock Broker':35,'Teacher':36,'Wedding Planner':38,'Writer':39}},inplace=True)

X= df[l1]

y = df[["Passions"]]
np.ravel(y)

def message():
    if (Symptom1.get() == "None" and  Symptom2.get() == "None" and Symptom3.get() == "None" and Symptom4.get() == "None" and Symptom5.get() == "None"):
        messagebox.showinfo("OOPS!!", "Please select your qualities!")
    else :
        NaiveBayes()

def NaiveBayes():
    from sklearn.naive_bayes import MultinomialNB
    gnb = MultinomialNB()
    gnb=gnb.fit(X,np.ravel(y))
    from sklearn.metrics import accuracy_score
    y_pred = gnb.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred, normalize=False))

    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = gnb.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(Passions)):
        if(Passions[predicted] == Passions[a]):
            h='yes'
            break

    if (h=='yes'):
        t3.delete("1.0", END)
        t3.insert(END, Passions[a])
    else:
        t3.delete("1.0", END)
        t3.insert(END, "Your Passion is yet to be updated!")

root = Tk()
root.title("Passion8")
root.configure()

Symptom1 = StringVar()
Symptom1.set(None)
Symptom2 = StringVar()
Symptom2.set(None)
Symptom3 = StringVar()
Symptom3.set(None)
Symptom4 = StringVar()
Symptom4.set(None)
Symptom5 = StringVar()
Symptom5.set(None)

w2 = Label(root, justify=LEFT, text=" Passion8: A Passion prediction algorithm ")
w2.config(font=("Elephant", 30))
w2.grid(row=1, column=0, columnspan=2, padx=100)

NameLb1 = Label(root, text="")
NameLb1.config(font=("Elephant", 20))
NameLb1.grid(row=5, column=1, pady=10,  sticky=W)

S1Lb = Label(root,  text="Quality 1")
S1Lb.config(font=("Elephant", 15))
S1Lb.grid(row=7, column=1, pady=10 , sticky=W)

S2Lb = Label(root,  text="Quality 2")
S2Lb.config(font=("Elephant", 15))
S2Lb.grid(row=8, column=1, pady=10, sticky=W)

S3Lb = Label(root,  text="Quality 3")
S3Lb.config(font=("Elephant", 15))
S3Lb.grid(row=9, column=1, pady=10, sticky=W)

S4Lb = Label(root,  text="Quality 4")
S4Lb.config(font=("Elephant", 15))
S4Lb.grid(row=10, column=1, pady=10, sticky=W)

S5Lb = Label(root,  text="Quality 5")
S5Lb.config(font=("Elephant", 15))
S5Lb.grid(row=11, column=1, pady=10, sticky=W)

lr = Button(root, text="Predict your Passion",height=2, width=20, command=message)
lr.config(font=("Elephant", 15))
lr.grid(row=15, column=1,pady=20)

OPTIONS = sorted(l1)

S1En = OptionMenu(root, Symptom1,*OPTIONS)
S1En.grid(row=7, column=2)

S2En = OptionMenu(root, Symptom2,*OPTIONS)
S2En.grid(row=8, column=2)

S3En = OptionMenu(root, Symptom3,*OPTIONS)
S3En.grid(row=9, column=2)

S4En = OptionMenu(root, Symptom4,*OPTIONS)
S4En.grid(row=10, column=2)

S5En = OptionMenu(root, Symptom5,*OPTIONS)
S5En.grid(row=11, column=2)

NameLb = Label(root, text="")
NameLb.config(font=("Elephant", 20))
NameLb.grid(row=13, column=1, pady=10,  sticky=W)

NameLb = Label(root, text="")
NameLb.config(font=("Elephant", 15))
NameLb.grid(row=18, column=1, pady=10,  sticky=W)

t3 = Text(root, height=2, width=30)
t3.config(font=("Elephant", 20))
t3.grid(row=20, column=1 , padx=10)

root.mainloop()