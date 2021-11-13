# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 18:51:31 2021

@author: ИнтелАв
"""


#Задание 1
# Красный горит - 7 сек
# Желтый - 2 сек
# Желеный - 7 сек   
    
import time as time
class TrafficLight():
    color = ""
    def running(self):
        StartTime = time.time()
        while 1==1:
            LeftTime = int(time.time() - StartTime)
            Sec = LeftTime % 16
            if self.color != "Красный"  and Sec < 7:
                self.color = "Красный"
                print(self.color)
            elif self.color != "Желтый"  and Sec < 9 and Sec >= 7:
                self.color = "Желтый"
                print(self.color)
            elif self.color != "Зеленый"  and Sec >= 9:
                self.color = "Зеленый"
                print(self.color)
       
a1 = TrafficLight()
a1.running()
 

#Задание 2
class Road():
    def __init__(self, length, width):
        self._width = width
        self._length = length
    def massa(self, masPerSM, SM):
        return "Вес всего асфальта {0} кг".format(self._width*self._length*masPerSM*SM)
asf = Road(5000, 20)
print(asf.massa(25, 5))

#Задание 3
class Worker():
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}
class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname
    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]
ivan = Position("Иван", "Кузьмин", "Директор сервис центра", 65000, 15000)
print(ivan.get_full_name())     
print(ivan.get_total_income())     
    
andrey = Position("Андрей", "Мартемьянов", "гл. инженер", 50000, 35000)
print(andrey.get_full_name())     
print(andrey.get_total_income())       
    
#Задание 4
class Car:
    speed = 0
    name = ""
    is_police  = False
    def go(self):
        return self.name + " поехала"
    def stop(self):
        return self.name + " остановилась"
    def turn(self, direction):
        return self.name + " повернула на " + direction
    def show_speed(self):
        return self.name + " сокрость: " + str(self.speed)
    
class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return self.name + " Превышение сокрости: " + str(self.speed)
        else:
            return self.name + " сокрость: " + str(self.speed)
  

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return self.name + " Превышение сокрости: " + str(self.speed)
        else:
            return self.name + " сокрость: " + str(self.speed)
  
class PoliceCar(Car):
    pass

police = PoliceCar()
police.name = "Субару Ипреза"
print(police.go())
police.speed = 60
print(police.show_speed())
print(police.turn("лево"))
print(police.stop())


cat = WorkCar()
cat.name = "BOB CAT"
print(cat.go())
cat.speed = 90
print(cat.show_speed())
print(cat.turn("право"))
print(cat.stop())


#Задание 5
class Stationery():
    def __init__(self, title):
        self.title = title
    def draw(self):
        print("Запуск отрисовки.")
class Pen(Stationery):
    def draw(self):
        print("Рисуем ручкой.")    
class Pencil(Stationery):
    def draw(self):
        print("Рисуем карандашом.")
class Handle(Stationery):
    def draw(self):
        print("Рисуем маркером.")
    
pen5 = Pen("Ручка")
pen5.draw()

pencil5 = Pencil("Ручка")
pencil5.draw()

handle5 = Handle("Ручка")
handle5.draw()

stationery5 = Stationery("Ручка")
stationery5.draw()






















    
    
        
        
    