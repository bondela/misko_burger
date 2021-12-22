import random
import time
import os
import sys
import datetime
menu = []

def men():
    menu.append("Меню:")
    menu.append("\n1. VG Burger\n2. GoodTrip burger\n3. ElProblema burger\n4. Ded burger\n5. Aristocrat burger")
    print(*menu, sep=' ')
    vibor = int(input('Выберите цифру: '))
    os.system('cls' if os.name == 'nt' else "clear")
    return vibor

def oneburger(vse):
    print('Вы выбрали VG Burger.\nСостав: Растительная котлета, маринованные патиссоны,')
    buy = input("Что-то ещё или всё?\n1 - Да.\n2 - Нет.")
    os.system('cls' if os.name == 'nt' else "clear")
    vse += 6
    while True:
        if buy == '1':
            return 6
        elif buy == '2':
            print("Хорошо, тогда с вас", vse, "рублей.")
            oplata = input("Картой или наличными?\n1 - Картой.\n2 - Наличными.")
            os.system('cls' if os.name == 'nt' else "clear")
            break
        else:
            buy = input("Выберите 1 или 2!\n")
            os.system('cls' if os.name == 'nt' else "clear")
    while True:
        if oplata == '1':
            print("Вы выбрали оплату картой.")
            print("Вы приложили карту, прошла оплата и Ваш заказ принялись готовить.")
            wait = random.randrange(10,60)
            time.sleep(wait)
            os.system('cls' if os.name == 'nt' else "clear")
            print("Ваш закала готов.")
            eat = input("Съесть в заведении или пойти домой.\n1 - Заведение.\n2 - Дома.\n")
            os.system('cls' if os.name == 'nt' else "clear")
            break
        elif oplata == '2':
            print("Вы выбрали оплату наличными.")
            print("Вы достали кошелёк, после достали нужную сумму и отдали продавцу, Ваш заказ принялись готовить.")
            wait = random.randrange(10,60)
            time.sleep(wait)
            os.system('cls' if os.name == 'nt' else "clear")
            print("Ваш заказ готов.")
            eat = input("Съесть в заведении или пойти домой.\n1 - Заведение.\n2 - Дома.\n")
            os.system('cls' if os.name == 'nt' else "clear")
            break
        else:
            oplata = input("Картой или наличными?\n1 - Картой.\n2 - Наличными.")
            os.system('cls' if os.name == 'nt' else "clear")
    while True:
        if eat == '1':
            print("Вы остались в завездение и хорошо покушали.")
            return 1
        elif eat == '2':
            print("Вы пришли домой, бургер был холодный но всё равно вкусный, Вы хорошо покушали.")
            return 1
        else:
            eat = input("Съесть в заведении или пойти домой.\n1 - Заведение.\n2 - Дома.\n")
            os.system('cls' if os.name == 'nt' else "clear")

def twoburger(vse):
    print('Вы выбрали goodtrip burger.\nСостав: Говяжья котлета, белые грибы, шампиньоны, трюфель')
    buy = input("Что-то ещё или всё?\n1 - Да.\n2 - Нет.")
    os.system('cls' if os.name == 'nt' else "clear")
    vse += 15
    while True:
        if buy == '1':
            return 15
        elif buy == '2':
            print("Хорошо, тогда с вас", vse, "рублей.")
            oplata = input("Картой или наличными?\n1 - Картой.\n2 - Наличными.")
            os.system('cls' if os.name == 'nt' else "clear")
            break
        else:
            buy = input("Выберите 1 или 2!\n")
            os.system('cls' if os.name == 'nt' else "clear")
    while True:
        if oplata == '1':
            print("Вы выбрали оплату картой.")
            print("Вы приложили карту, прошла оплата и Ваш заказ принялись готовить.")
            wait = random.randrange(10,60)
            time.sleep(wait)
            os.system('cls' if os.name == 'nt' else "clear")
            print("Ваш закала готов.")
            eat = input("Съесть в заведении или пойти домой.\n1 - Заведение.\n2 - Дома.\n")
            os.system('cls' if os.name == 'nt' else "clear")
            break
        elif oplata == '2':
            print("Вы выбрали оплату наличными.")
            print("Вы достали кошелёк, после достали нужную сумму и отдали продавцу, Ваш заказ принялись готовить.")
            wait = random.randrange(10,60)
            time.sleep(wait)
            os.system('cls' if os.name == 'nt' else "clear")
            print("Ваш заказ готов.")
            eat = input("Съесть в заведении или пойти домой.\n1 - Заведение.\n2 - Дома.\n")
            os.system('cls' if os.name == 'nt' else "clear")
            break
        else:
            oplata = input("Картой или наличными?\n1 - Картой.\n2 - Наличными.")
            os.system('cls' if os.name == 'nt' else "clear")
    while True:
        if eat == '1':
            print("Вы остались в завездение и хорошо покушали.")
            return 1
        elif eat == '2':
            print("Вы пришли домой, бургер был холодный но всё равно вкусный, Вы хорошо покушали.")
            return 1
        else:
            eat = input("Съесть в заведении или пойти домой.\n1 - Заведение.\n2 - Дома.\n")
            os.system('cls' if os.name == 'nt' else "clear")

def threeburger(vse):
    print('Вы выбрали EL Problema.\nСостав: Говяжья котлета, аджика, фирменная картофельная булка')
    buy = input("Что-то ещё или всё?\n1 - Да.\n2 - Нет.")
    os.system('cls' if os.name == 'nt' else "clear")
    vse += 20
    while True:
        if buy == '1':
            return 20
        elif buy == '2':
            print("Хорошо, тогда с вас", vse, "рублей.")
            oplata = input("Картой или наличными?\n1 - Картой.\n2 - Наличными.")
            os.system('cls' if os.name == 'nt' else "clear")
            break
        else:
            buy = input("Выберите 1 или 2!\n")
            os.system('cls' if os.name == 'nt' else "clear")
    while True:
        if oplata == '1':
            print("Вы выбрали оплату картой.")
            print("Вы приложили карту, прошла оплата и Ваш заказ принялись готовить.")
            wait = random.randrange(10,60)
            time.sleep(wait)
            os.system('cls' if os.name == 'nt' else "clear")
            print("Ваш закала готов.")
            eat = input("Съесть в заведении или пойти домой.\n1 - Заведение.\n2 - Дома.\n")
            os.system('cls' if os.name == 'nt' else "clear")
            break
        elif oplata == '2':
            print("Вы выбрали оплату наличными.")
            print("Вы достали кошелёк, после достали нужную сумму и отдали продавцу, Ваш заказ принялись готовить.")
            wait = random.randrange(10,60)
            time.sleep(wait)
            os.system('cls' if os.name == 'nt' else "clear")
            print("Ваш заказ готов.")
            eat = input("Съесть в заведении или пойти домой.\n1 - Заведение.\n2 - Дома.\n")
            os.system('cls' if os.name == 'nt' else "clear")
            break
        else:
            oplata = input("Картой или наличными?\n1 - Картой.\n2 - Наличными.")
            os.system('cls' if os.name == 'nt' else "clear")
    while True:
        if eat == '1':
            print("Вы остались в завездение и хорошо покушали.")
            return 1
        elif eat == '2':
            print("Вы пришли домой, бургер был холодный но всё равно вкусный, Вы хорошо покушали.")
            return 1
        else:
            eat = input("Съесть в заведении или пойти домой.\n1 - Заведение.\n2 - Дома.\n")
            os.system('cls' if os.name == 'nt' else "clear")

def fourburger(vse):
    print('Вы выбрали дед Burger.\nСостав: Куриная котлета, овощи,сливочный соус')
    buy = input("Что-то ещё или всё?\n1 - Да.\n2 - Нет.")
    os.system('cls' if os.name == 'nt' else "clear")
    vse += 18
    while True:
        if buy == '1':
            return 18
        elif buy == '2':
            print("Хорошо, тогда с вас", vse, "рублей.")
            oplata = input("Картой или наличными?\n1 - Картой.\n2 - Наличными.")
            os.system('cls' if os.name == 'nt' else "clear")
            break
        else:
            buy = input("Выберите 1 или 2!\n")
            os.system('cls' if os.name == 'nt' else "clear")
    while True:
        if oplata == '1':
            print("Вы выбрали оплату картой.")
            print("Вы приложили карту, прошла оплата и Ваш заказ принялись готовить.")
            wait = random.randrange(10,60)
            time.sleep(wait)
            os.system('cls' if os.name == 'nt' else "clear")
            print("Ваш закала готов.")
            eat = input("Съесть в заведении или пойти домой.\n1 - Заведение.\n2 - Дома.\n")
            os.system('cls' if os.name == 'nt' else "clear")
            break
        elif oplata == '2':
            print("Вы выбрали оплату наличными.")
            print("Вы достали кошелёк, после достали нужную сумму и отдали продавцу, Ваш заказ принялись готовить.")
            wait = random.randrange(10,60)
            time.sleep(wait)
            os.system('cls' if os.name == 'nt' else "clear")
            print("Ваш заказ готов.")
            eat = input("Съесть в заведении или пойти домой.\n1 - Заведение.\n2 - Дома.\n")
            os.system('cls' if os.name == 'nt' else "clear")
            break
        else:
            oplata = input("Картой или наличными?\n1 - Картой.\n2 - Наличными.")
            os.system('cls' if os.name == 'nt' else "clear")
    while True:
        if eat == '1':
            print("Вы остались в завездение и хорошо покушали.")
            return 1
        elif eat == '2':
            print("Вы пришли домой, бургер был холодный но всё равно вкусный, Вы хорошо покушали.")
            return 1
        else:
            eat = input("Съесть в заведении или пойти домой.\n1 - Заведение.\n2 - Дома.\n")
            os.system('cls' if os.name == 'nt' else "clear")

def fiveburger(vse):
    print('Вы выбрали аристократ бургер.\nСостав: Стейк «Шатобриан», овощи, салат, помидоры.')
    buy = input("Что-то ещё или всё?\n1 - Да.\n2 - Нет.")
    os.system('cls' if os.name == 'nt' else "clear")
    vse += 30
    while True:
        if buy == '1':
            return 30
        elif buy == '2':
            print("Хорошо, тогда с вас", vse, "рублей.")
            oplata = input("Картой или наличными?\n1 - Картой.\n2 - Наличными.")
            os.system('cls' if os.name == 'nt' else "clear")
            break
        else:
            buy = input("Выберите 1 или 2!\n")
            os.system('cls' if os.name == 'nt' else "clear")
    while True:
        if oplata == '1':
            print("Вы выбрали оплату картой.")
            print("Вы приложили карту, прошла оплата и Ваш заказ принялись готовить.")
            wait = random.randrange(10,60)
            time.sleep(wait)
            os.system('cls' if os.name == 'nt' else "clear")
            print("Ваш закала готов.")
            eat = input("Съесть в заведении или пойти домой.\n1 - Заведение.\n2 - Дома.\n")
            os.system('cls' if os.name == 'nt' else "clear")
            break
        elif oplata == '2':
            print("Вы выбрали оплату наличными.")
            print("Вы достали кошелёк, после достали нужную сумму и отдали продавцу, Ваш заказ принялись готовить.")
            wait = random.randrange(10,60)
            time.sleep(wait)
            os.system('cls' if os.name == 'nt' else "clear")
            print("Ваш заказ готов.")
            eat = input("Съесть в заведении или пойти домой.\n1 - Заведение.\n2 - Дома.\n")
            os.system('cls' if os.name == 'nt' else "clear")
            break
        else:
            oplata = input("Картой или наличными?\n1 - Картой.\n2 - Наличными.")
            os.system('cls' if os.name == 'nt' else "clear")
    while True:
        if eat == '1':
            print("Вы остались в завездение и хорошо покушали.")
            return 1
        elif eat == '2':
            print("Вы пришли домой, бургер был холодный но всё равно вкусный, Вы хорошо покушали.")
            return 1
        else:
            eat = input("Съесть в заведении или пойти домой.\n1 - Заведение.\n2 - Дома.\n")
            os.system('cls' if os.name == 'nt' else "clear")
            

def povar():
    zakaz = random.randrange(0,1000)
    print("Вам поступил заказ #", zakaz)
    zakaz1 = random.randrange(0,6)
    if zakaz1 == 1:
        print("Вам поступил заказ на VG Burger")
        vg = input("Вы взяли булки, после положили туда лист салата, налили соуса, теперь Вам надо положить катлет.\n1 - Положить катлету.\n2 - Не ложить(Вас уволят)")
        os.system('cls' if os.name == 'nt' else "clear")
        while True:
            if vg == '1':
                vg1 = input("Вы положили катлету, после добавили остальные нужные ингридиенты, теперь нужно положить всё в упаковку.\n1 - Положить\n2 - Не ложить.")
                q = random.randrange(0,2)
                os.system('cls' if os.name == 'nt' else "clear")
                while True:
                    if vg == '1':
                        print("Вы положили бургер в коробку после отдали заказ покупателю.")
                        if q == 1:
                            print("Вы очень долго делали заказ и вам не дали чаевых.")
                            print("Но заказ Вы сделали.")
                            return 1
                        elif q == 2:
                            chai = random.randrange(10,101)
                            print("Вы сделали всё быстро и Вам дали", chai, "чаявых.")
                            return 1
                        elif q == 0:
                            print("Вы не очень быстро и не очень медлено делали заказ, но чаявых Вам не дали.")
                            return 1
                    else:
                        vg1 = input("Вы положили катлету, после добавили остальные нужные ингридиенты, теперь нужно положить всё в упаковку.\n1 - Положить\n2 - Не ложить.")
            elif vg == '2':
                print("Вы не положили катлету в бургер, это увидели и сообщили страшим, после Вас уволили.")
                os.system('cls' if os.name == 'nt' else "clear")
                return
            else:
                vg = input("Вы взяли булки, после положили туда лист салата, налили соуса, теперь Вам надо положить катлету.\n1 - Положить катлету.\n2 - Не ложить(Вас уволят)")
                os.system('cls' if os.name == 'nt' else "clear")
    elif zakaz1 == 2:
        print("Вам поступил заказ на GoodTrip burger.")
        vg = input("Вы взяли булки, после положили туда лист салата, налили соуса, теперь Вам надо положить катлет.\n1 - Положить катлету.\n2 - Не ложить(Вас уволят)")
        os.system('cls' if os.name == 'nt' else "clear")
        while True:
            if vg == '1':
                vg1 = input("Вы положили катлету, после добавили остальные нужные ингридиенты, теперь нужно положить всё в упаковку.\n1 - Положить\n2 - Не ложить.")
                os.system('cls' if os.name == 'nt' else "clear")
                q = random.randrange(0,2)
                while True:
                    if vg == '1':
                        print("Вы положили бургер в коробку после отдали заказ покупателю.")
                        if q == 1:
                            print("Вы очень долго делали заказ и вам не дали чаевых.")
                            print("Но заказ Вы сделали.")
                            return 1
                        elif q == 2:
                            chai = random.randrange(10,101)
                            print("Вы сделали всё быстро и Вам дали", chai, "чаявых.")
                            return 1
                        elif q == 0:
                            print("Вы не очень быстро и не очень медлено делали заказ, но чаявых Вам не дали.")
                            return 1
                    else:
                        vg1 = input("Вы положили катлету, после добавили остальные нужные ингридиенты, теперь нужно положить всё в упаковку.\n1 - Положить\n2 - Не ложить.")
                        os.system('cls' if os.name == 'nt' else "clear")
            elif vg == '2':
                print("Вы не положили катлету в бургер, это увидели и сообщили страшим, после Вас уволили.")
                return
            else:
                vg = input("Вы взяли булки, после положили туда лист салата, налили соуса, теперь Вам надо положить катлету.\n1 - Положить катлету.\n2 - Не ложить(Вас уволят)")
                os.system('cls' if os.name == 'nt' else "clear")
    elif zakaz1 == 3:
        print("Вам поступил заказ на ElBroblema burger.")
        vg = input("Вы взяли булки, после положили туда лист салата, налили соуса, теперь Вам надо положить катлет.\n1 - Положить катлету.\n2 - Не ложить(Вас уволят)")
        os.system('cls' if os.name == 'nt' else "clear")
        while True:
            if vg == '1':
                vg1 = input("Вы положили катлету, после добавили остальные нужные ингридиенты, теперь нужно положить всё в упаковку.\n1 - Положить\n2 - Не ложить.")
                os.system('cls' if os.name == 'nt' else "clear")
                q = random.randrange(0,2)
                while True:
                    if vg == '1':
                        print("Вы положили бургер в коробку после отдали заказ покупателю.")
                        if q == 1:
                            print("Вы очень долго делали заказ и вам не дали чаевых.")
                            print("Но заказ Вы сделали.")
                            return 1
                        elif q == 2:
                            chai = random.randrange(10,101)
                            print("Вы сделали всё быстро и Вам дали", chai, "чаявых.")
                            return 1
                        elif q == 0:
                            print("Вы не очень быстро и не очень медлено делали заказ, но чаявых Вам не дали.")
                            return 1
                    else:
                        vg1 = input("Вы положили катлету, после добавили остальные нужные ингридиенты, теперь нужно положить всё в упаковку.\n1 - Положить\n2 - Не ложить.")
                        os.system('cls' if os.name == 'nt' else "clear")
            elif vg == '2':
                print("Вы не положили катлету в бургер, это увидели и сообщили страшим, после Вас уволили.")
                return
            else:
                vg = input("Вы взяли булки, после положили туда лист салата, налили соуса, теперь Вам надо положить катлету.\n1 - Положить катлету.\n2 - Не ложить(Вас уволят)")
    elif zakaz1 == 4:
        print("Вам поступил заказ на Ded burger")
        vg = input("Вы взяли булки, после положили туда лист салата, налили соуса, теперь Вам надо положить катлет.\n1 - Положить катлету.\n2 - Не ложить(Вас уволят)")
        os.system('cls' if os.name == 'nt' else "clear")
        while True:
            if vg == '1':
                vg1 = input("Вы положили катлету, после добавили остальные нужные ингридиенты, теперь нужно положить всё в упаковку.\n1 - Положить\n2 - Не ложить.")
                os.system('cls' if os.name == 'nt' else "clear")
                q = random.randrange(0,2)
                while True:
                    if vg == '1':
                        print("Вы положили бургер в коробку после отдали заказ покупателю.")
                        if q == 1:
                            print("Вы очень долго делали заказ и вам не дали чаевых.")
                            print("Но заказ Вы сделали.")
                            return 1
                        elif q == 2:
                            chai = random.randrange(10,101)
                            print("Вы сделали всё быстро и Вам дали", chai, "чаявых.")
                            return 1
                        elif q == 0:
                            print("Вы не очень быстро и не очень медлено делали заказ, но чаявых Вам не дали.")
                            return 1
                    else:
                        vg1 = input("Вы положили катлету, после добавили остальные нужные ингридиенты, теперь нужно положить всё в упаковку.\n1 - Положить\n2 - Не ложить.")
            elif vg == '2':
                print("Вы не положили катлету в бургер, это увидели и сообщили страшим, после Вас уволили.")
                return
            else:
                vg = input("Вы взяли булки, после положили туда лист салата, налили соуса, теперь Вам надо положить катлету.\n1 - Положить катлету.\n2 - Не ложить(Вас уволят)")
                os.system('cls' if os.name == 'nt' else "clear")
    elif zakaz1 == 5:
        print("Вам поступил заказ на Aristocrat burger")
        vg = input("Вы взяли булки, после положили туда лист салата, налили соуса, теперь Вам надо положить катлет.\n1 - Положить катлету.\n2 - Не ложить(Вас уволят)")
        os.system('cls' if os.name == 'nt' else "clear")
        while True:
            if vg == '1':
                vg1 = input("Вы положили катлету, после добавили остальные нужные ингридиенты, теперь нужно положить всё в упаковку.\n1 - Положить\n2 - Не ложить.")
                os.system('cls' if os.name == 'nt' else "clear")
                q = random.randrange(0,2)
                while True:
                    if vg == '1':
                        print("Вы положили бургер в коробку после отдали заказ покупателю.")
                        if q == 1:
                            print("Вы очень долго делали заказ и вам не дали чаевых.")
                            print("Но заказ Вы сделали.")
                            return 1
                        elif q == 2:
                            chai = random.randrange(10,101)
                            print("Вы сделали всё быстро и Вам дали", chai, "чаявых.")
                            return 1
                        elif q == 0:
                            print("Вы не очень быстро и не очень медлено делали заказ, но чаявых Вам не дали.")
                            return 1
                    else:
                        vg1 = input("Вы положили катлету, после добавили остальные нужные ингридиенты, теперь нужно положить всё в упаковку.\n1 - Положить\n2 - Не ложить.")
            elif vg == '2':
                print("Вы не положили катлету в бургер, это увидели и сообщили страшим, после Вас уволили.")
                return
            else:
                vg = input("Вы взяли булки, после положили туда лист салата, налили соуса, теперь Вам надо положить катлету.\n1 - Положить катлету.\n2 - Не ложить(Вас уволят)")
                os.system('cls' if os.name == 'nt' else "clear")

def main():
    print("Добро пожалуловать в бургерную.\nДля начала давайте дадим ей название: ")
    vse = 0
    nazv = str(input())
    os.system('cls' if os.name == 'nt' else "clear")
    print('Бургерная называется', nazv)
    player = input('Выберите за кого будете играть.\n1 - Гость.\n2 - Повар\n')
    os.system('cls' if os.name == 'nt' else "clear")
    while True:
        if player == '1':
            burger = men()
            if burger == 1:
                vg = oneburger(vse)
                if vg == 1:
                    print("Game over!")
                    break
                elif vg == 6:
                    vse += 6
                    print("Выберите что-то ещё: ")
            elif burger == 2:
                gt = twoburger(vse)
                if gt == 1:
                    print("Game over!")
                    break
                elif gt == 15:
                    vse += 15
                    print("Выберите что-то ещё: ")
            elif burger == 3:
                gt = threeburger(vse)
                if gt == 1:
                    print("Game over!")
                    break
                elif gt == 20:
                    vse += 20
                    print("Выберите что-то ещё: ")
            elif burger == 4:
                gt = threeburger(vse)
                if gt == 1:
                    print("Game over!")
                    break
                elif gt == 18:
                    vse += 18
                    print("Выберите что-то ещё: ")
            elif burger == 5:
                gt = threeburger(vse)
                if gt == 1:
                    print("Game over!")
                    break
                elif gt == 30:
                    vse += 30
                    print("Выберите что-то ещё: ")
        elif  player == '2':
            q = povar()
            if q == 1:
                print("The end.")
                break
        else:
            player = input('Выберите цифру: ')


if __name__ == "__main__":
    main()
