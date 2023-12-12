import time
from datetime import datetime
def Writing(title):
    count=0
    with open("text.txt", "r") as file:
        content = file.read()
        controlltext = "Title:"+title

    if controlltext in content:
        print("\033[31mВыберете другое название, такой заголовок уже есть\033[0m")
        count=1
    if count==0:
        msg = input("Введите текст: ")
        with open('text.txt', 'a') as f:
            f.write('\n'+"######################################")
            current_time = time.strftime("%H:%M:%S")
            current_time2 = datetime.now()
            date_string = current_time2.strftime('%d %B %Y')
            f.write("\nCreation data: "+date_string)
            f.write("\nCreation time: "+current_time+" / "+date_string)
            f.write("\nEditing time: No")
            nameT= "\nTitle:"+title
            f.write(nameT)
            f.write('\n'+msg)
            f.write('\n'+"######################################")
        print("\033[92mЗаметка добавлена!\033[0m")

def Delete(title):
    with open('text.txt','r+') as f:
        a=1
        list=[]
        b=1
        for index, line in enumerate(f, 1):
            next=line.replace("\n","")
            if next == "######################################":
                a=1
            if next == "Title:"+title:
                inext = index-1
                a=2
            if a == 2:
                inext+=1
                list.append(inext)
            if a==2 and b == 1:
                number = list[0]-1
                list.append(number)
                number-=1
                list.append(number)
                number-=1
                list.append(number)
                number-=1
                list.append(number)
                b=0
        number = list[len(list)-1]+1
        list.append(number)
        i=1
        newtext=""
    with open('text.txt','r+') as f:
        for index, line in enumerate(f, 1):
            if index not in list:
                newtext+=line
    with open('text.txt','w') as f:
        f.write(newtext)
    print("\033[92mУдаляем заметку\033[0m")

def Redactor(title,text):
    try:
        with open('text.txt','r+') as f:
            a=1
            list=[]
            b=1
            for index, line in enumerate(f, 1):
                next=line.replace("\n","")
                if next == "######################################":
                    a=1
                    index2 = index-1
                if next == "Title:"+title:
                    inext = index
                    a=2
                if a == 2:
                    inext+=1
                    list.append(inext)
            list.pop(-1)
            i=1
            newtext=""
        print("\033[92mРедактируем заметку\033[0m")
        newtext=""
        with open('text.txt','r+') as f:
            for index, line in enumerate(f, 1):
                if index == list[0]-2:
                    current_time = time.strftime("%H:%M:%S")
                    current_time2 = datetime.now()
                    date_string = current_time2.strftime('%d %B %Y')
                    newtext+="Editing time: "+str(current_time)+" / "+date_string+"\n"
                if index == list[0]:
                    newtext+=text+"\n"
                if index not in list and index!=list[0]-2:
                    newtext+=line
        with open('text.txt','w') as f:
            f.write(newtext)
    except:
        print("\033[31mТакого заголовка нет\033[0m")
def ReadList():
    with open('text.txt', 'r') as f:
        text = f.read()
        print(text)
def Read(title):
    try:
        with open('text.txt','r+') as f:
            a=1
            list=[]
            b=1
            for index, line in enumerate(f, 1):
                next=line.replace("\n","")
                if next == "######################################":
                    a=1
                if next == "Title:"+title:
                    inext = index-1
                    a=2
                if a == 2:
                    inext+=1
                    list.append(inext)
                if a==2 and b == 1:
                    number = list[0]-1
                    list.append(number)
                    number-=1
                    list.append(number)
                    number-=1
                    list.append(number)
                    b=0
            number = list[len(list)-1]+1
            list.append(number)
            i=1
            newtext=""
        with open('text.txt','r+') as f:
            for index, line in enumerate(f, 1):
                if index in list:
                    newtext+=line
        print(newtext)
    except:
        print("\033[31mТакого заголовка нет\033[0m")
def ReadData(data):
    try:
        with open('text.txt','r+') as f:

            list=[]
            c=1
            a=0
            y=1
            for index, line in enumerate(f, 1):
                next=line.replace("\n","")
                if next == "######################################":
                    a=0
                if next == "Creation data: "+data:
                    number = index
                    number2=index
                    list.append(number)
                    c=0
                    a=1
                    y=0
                if c==0:
                    list.append(number-1)
                    c=1
                if a==1:
                    number2+=1
                    list.append(number2)
            if y==1:
                print("\033[31mЗаметки созданной в эту дату нет\033[0m")
            i=1
            newtext=""
        with open('text.txt','r+') as f:
            for index, line in enumerate(f, 1):
                if index in list:
                    newtext+=line
        print(newtext)
    except:
         print("\033[31mЗаметки созданной в эту дату нет\033[0m")
