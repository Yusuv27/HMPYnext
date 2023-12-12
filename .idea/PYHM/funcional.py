import funcional2
def Add():
    titile = input("Введите заголовок заметки: ")
    funcional2.Writing(title=titile)
def Delete():
    title = input("Введите заголовок который хотите удалить: ")
    funcional2.Delete(title=title)
def Redactor():
    title = input("Введите заголовок заметки текст которого хотите отредактировать: ")
    text = input("Введите текст: ")
    funcional2.Redactor(title=title,text=text)
def ReadList():
    funcional2.ReadList()
def Read():
    title = input("Введите заголовок: ")
    funcional2.Read(title=title)
def ReadData():
    data= input("Пример: 12 December 2023\nВведите дату строго по примеру(месяц с большой буквы): ")
    funcional2.ReadData(data=data)