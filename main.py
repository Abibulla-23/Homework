def main(input: str):
    s = input('Введите запрос в формате: целое число от 1 до 10 включительно, затем через пробел знак действия(+,-,*,/), затем через пробел второе целое число от 1 до 10 включительно:')
    se = s.split()
    try:
        a = int(se[0])
        b = int(se[2])
    except:
        print("Введите целое число!")
        exit()
    c = se[1]
    try:
        c == '+' or '-' or '*' or '/'
    except:
        print('Введите один из знаков действия(+,-,*,/)')
        exit()
    if 0<=a<=10 and 0<=b<=10:
        if c == '+':
            print(a+b)
        elif c == '-':
            print(a-b)
        elif c == '*':
            print(a*b)
        elif c == '/':
            print(a//b)
    else:
        print("Введите целые числа от 1 до 10 включительно!")
main(input)
main(input)