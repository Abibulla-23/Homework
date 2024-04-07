
def main(s):
    se = s.split()
    try:
        a = int(se[0])
        b = int(se[2])
        c = se[1]
        if c == '+' or '-' or '*' or '/':
            if c == '+' and 0 <= a <= 10 and 0 <= b <= 10:
                f = str(a + b)
            elif c == '-' and 0 <= a <= 10 and 0 <= b <= 10:
                f = str(a - b)
            elif c == '*' and 0 <= a <= 10 and 0 <= b <= 10:
                f = str(a * b)
            elif c == '/' and 0 <= a <= 10 and 0 <= b <= 10:
                f = str(a // b)
            return f

    except:
        print("Введите корректный запрос!")
