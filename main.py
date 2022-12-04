if __name__ == '__main__':
    def plus_action(action):
        run = True
        final = num1 + num2
        print(final)
        x = int(input())
        while run:
            final1 = final + x
            print(final1)
            break



    def minus_action(action):
        final = num1 - num2
        print(final)


    def multi_action(action):
        final = num1 * num2
        print(final)


    def decide_action(action):
        final = num1 / num2
        print(final)


    def decide_0_action(action):
        final = "На ноль делить нельзя!"
        print(final)
    print("<<<КАЛЬКУЛЯТОР>>>")
    print("Добро пожаловать! ")
    print(" Введите нужное вам число")
    print('Нажмите "Enter" и выберите операцию из:"+","-","*","/". Нажмите "Enter"  и введите следующее число:')
    num1 = int(input())
    action = input()
    num2 = int(input())
    print(f'{num1}{action}{num2}=')
    run = True
    run1 = False

    if action == "+":
        run1 = True
        while run1:
            run2 = plus_action(action)
            break
    elif action == "-":
        run = minus_action(action)
        #run1= True:
        #while run1:
    elif action == "*":
        run = multi_action(action)
    elif action == "/" and num2 != 0:
        run = decide_action(action)
    elif action == "/" and num2 == 0:
        run= decide_0_action(action)

    # for i in range(len(x)):
    #     if x[i] in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]:
    #         pass
