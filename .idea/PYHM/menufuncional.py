import funcional
def Menu():
    commands = input("Введите команду: ")
    if commands == "add":
        funcional.Add()
        Menu()
    elif commands == "delete":
        funcional.Delete()
        Menu()
    elif commands == "redactor":
        funcional.Redactor()
        Menu()
    elif commands == "readlist":
        funcional.ReadList()
        Menu()
    elif commands == "read":
        funcional.Read()
        Menu()
    elif commands == "help":
        print("\033[92mСписок команд:\nadd - добавить заметку\ndelete - удалить заметку\nredactor - редактировать заметку\nreadlist - вывести все заметки\nread - вывести заметку по названию\nend - завершить работу\ndataread - показать заметки сделанные в эту дату\ndatahelp - список/перевод месяцев\033[0m")
        Menu()
    elif commands == "datahelp":
        print("\033[92mПеревод месяцев:\nJanuary – Январь\nFebruary – Февраль\nMarch – Март\nApril – Апрель\nMay – Май\nJune – Июнь\nJuly – Июль\nAugust – Август\nAugust – Август\nOctober – Октябрь\nNovember – Ноябрь\nDecember – Декабрь\033[0m")
        Menu()
    elif commands == "dataread":
        funcional.ReadData();
        Menu()
    elif commands == "end":
        print("До свидания!")
    else:
        print("\033[31mНеизвестная команда!\033[0m\nДля списка команд введите: help")
        Menu()