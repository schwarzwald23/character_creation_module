# Объявите класс Quest с методами и свойствами.
class Quest:
    def __init__(self, name, description, goal):
        self.name = name
        self.description = description
        self.goal = goal
        print(f'Новый квест {name} получен')
# В этих переменных содержатся значения, которые нужно передать
# в качестве аргументов в экземпляр класса Quest.\
    
    def __str__(self):
        return (
            f'Квест — «{self.name}». '
            f'Цель: {self.goal} '
            f'История: {self.description} '
           )


quest_name = 'Сбор пиксельники'
quest_goal = 'Соберите 12 ягод пиксельники.'
quest_description = '''
        В древнем лесу Кодоборье растёт ягода "пиксельника".
        Она нужна для приготовления целебных снадобий.
        Соберите 12 ягод пиксельники.'''


new_quest = Quest(quest_name, quest_description, quest_goal)
print(new_quest)