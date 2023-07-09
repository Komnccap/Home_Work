# Доработаем задачи 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
import random


class Animal:
    def __init__(self, class_animal, kind_animal):
        self.class_animal = class_animal
        self.kind_animal = kind_animal


class Dog(Animal):
    def __init__(self, voice, *args, **kwargs):
        self.voice = voice
        super().__init__(*args, **kwargs)

    def print_beast(self):
        return f'Порода - {self.class_animal}, характер - {self.kind_animal}, Голос - {self.voice}'


class Fish(Animal):
    def __init__(self, deep_swim, *args, **kwargs):
        self.deep_swim = deep_swim
        super().__init__(*args, **kwargs)

    def print_fish(self):
        return f'Класс - {self.class_animal}, Вид - {self.kind_animal}, Глубина погружения - {self.deep_swim}м'


class Bird(Animal):
    def __init__(self, width_fly, *args, **kwargs):
        self.width_fly = width_fly
        super().__init__(*args, **kwargs)

    def print_bird(self):
        return f'Класс - {self.class_animal}, Вид - {self.kind_animal}, Высота полёта - {self.width_fly}м'


class Fabric(Dog):
    random = random.randint
    n1 = random(0, 2)
    n2 = random(0, 2)
    n3 = random(0, 2)
    voices = ['Разумное потребление пластика!', 'Я животное', '*звуки*']
    animal_breeds = ['Немецкая овчарка', 'Доберман', 'Босерон']
    animals_character = ['Агрессивный', 'Спокойный', 'эмоционально не стаильный']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    fab = Dog(voices[n1], animal_breeds[n2], animals_character[n3])
    print(fab.print_beast())

# dog = Dog('Разумное потребление пластика!', 'Земноводное', 'Собака')
# print(dog.print_beast())
# fish = Fish(350, 'Водоплавающее', 'Барракуда')
# print(fish.print_fish())
# bird = Bird(1200, 'Птица', 'Ястреб')
# print(bird.print_bird())
