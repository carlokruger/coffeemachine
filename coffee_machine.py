class CoffeeMachine:
    money = 550
    water = 400
    milk = 540
    beans = 120
    cups = 9

    def print_state(self):
        print("The coffee machine has:")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.beans, "of coffee beans")
        print(self.cups, "of disposable cups")
        print(self.money, "of money")

    def take(self):
        print("I gave you {}".format(self.money))
        self.money = 0

    def fill(self):
        self.water += int(input("Write how many ml of water do you want to add:"))
        self.milk += int(input("Write how many ml of milk do you want to add:"))
        self.beans += int(input("Write how many grams of coffee beans do you want to add:"))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add:"))
        # print_state()

    def espresso(self):
        if self.water >= 250 and self.beans >= 16 and self.cups >= 1:
            self.water -= 250
            self.beans -= 16
            self.cups -= 1
            self.money += 4
            print("I have enough resources, making you a coffee!")
        else:
            if self.water < 250:
                print("Sorry, not enough water!")
            elif self.beans < 16:
                print("Sorry, not enough coffee beans!")
            elif self.cups < 1:
                print("Sorry, not enough cups!")
        # print_state()

    def latte(self):
        if self.water >= 350 and self.milk >= 75 and self.beans >= 20 and self.cups >= 1:
            self.water -= 350
            self.milk -= 75
            self.beans -= 20
            self.cups -= 1
            self.money += 7
            print("I have enough resources, making you a coffee!")
        else:
            if self.water < 350:
                print("Sorry, not enough water!")
            elif self.milk < 75:
                print("Sorry, not enough milk!")
            elif self.beans < 20:
                print("Sorry, not enough coffee beans!")
            elif self.cups < 1:
                print("Sorry, not enough cups!")
        # print_state()

    def cappuccino(self):
        if self.water >= 200 and self.milk >= 100 and self.beans >= 12 and self.cups >= 1:
            print("I have enough resources, making you a coffee!")
            self.water -= 200
            self.milk -= 100
            self.beans -= 12
            self.cups -= 1
            self.money += 6
        else:
            if self.water < 200:
                print("Sorry, not enough water!")
            elif self.milk < 100:
                print("Sorry, not enough milk!")
            elif self.beans < 12:
                print("Sorry, not enough coffee beans!")
            elif self.cups < 1:
                print("Sorry, not enough cups!")
        # print_state()

this_machine = CoffeeMachine
action = "remaining"

while action != "exit":
    action = input("Write action (buy, fill, take, remaining, exit)")
    if action == "remaining":
        CoffeeMachine.print_state(this_machine)
    elif action == "take":
        CoffeeMachine.take(this_machine)
    elif action == "fill":
        CoffeeMachine.fill(this_machine)
    elif action == "buy":
        coffee = "1"
        while coffee != "back":
            coffee = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu")
            if coffee == "1":
                CoffeeMachine.espresso(this_machine)
                coffee = "back"
            elif coffee == "2":
                CoffeeMachine.latte(this_machine)
                coffee = "back"
            elif coffee == "3":
                CoffeeMachine.cappuccino(this_machine)
                coffee = "back"

