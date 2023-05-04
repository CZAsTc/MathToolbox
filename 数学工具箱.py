import decimal
import math
import time
from fractions import Fraction
from decimal import getcontext, Decimal
import sys
import numpy as np
import sympy
from nzmath import *
from mpmath import *
import gmpy2
import itertools
import functools
from sympy.ntheory import totient
from math import comb, factorial
from sympy import divisor_sigma as sigma

sys.set_int_max_str_digits(0)
print("欢迎进入数学帝国")
while True:
    text = """计算斐波那契数请输入1
计算阶乘请输入2
计算(1+2+……+n)请输入3
判断一个数是否为质数请输入4
计算圆周率请输入5
列出a~b之间的质数请输入6
计算自然常数请输入7
分数约分请输入8
计算两个数的最大公因数和最小公倍数请输入9
分数计算请输入10
循环小数转分数请输入11
开根号请输入12
开n次方根请输入13
计算一个数的n次方请输入14
计算一个数的自然对数请输入15
计算一个数以任意数为底的对数请输入16
计算(1!+2!+……+n!)请输入17
计算1~n的任意数次方和请输入18
计算a~b的任意数次方和请输入19
计算a~b的整数和请输入20
分数转循环小数并查看循环节请输入21
计算1~n里有几个质数请输入请输入22
分解质因数请输入请输入23
判断是否为超级质数请输入24
列出一个数的所有因数并求和请输入25
判断一个数是否为完全数请输入26
计算第n个质数请输入27
计算第n个任意边形数请输入28
判断一个数是否为n边形数请输入29
判断一个数是可恶数还是邪恶数请输入30
判断一个数是否为亚当数请输入31
判断一个数是否为节俭数请输入32
计算第n个蛋糕数请输入33
判断一个数是否为蛋糕数请输入34
列出第1~n个卡特兰数请输入35
判断一个数是否为卡特兰数请输入36
计算第n个帕多瓦数请输入37
列出第1~n个帕多瓦数请输入38
计算组合数公式请输入39
计算第n个伯努利数请输入40
计算第n个欧拉数请输入41
计算第n个贝尔数请输入42
判断一个数是否为贝尔数请输入43
判断一个数是过剩数还是不足数请输入44
使用普洛尼克数合集请输入45
使用各种比例合集请输入46
计算高斯常数请输入47
计算阿培里常数请输入48
计算欧拉常数请输入49
计算加泰罗尼亚常数请输入50
计算辛钦常数请输入51
计算葛莱佘-金可林常数请输入52
计算默滕斯常数请输入53
计算孪生素数常数请输入54
使用三角函数大合集请输入55
使用小数版三角函数大合集请输入56
列出第0~n个雅各布斯塔尔数请输入57
判断一个数是否为雅各布斯塔尔数请输入58
请输入："""
    mode = int(input(text))
    mode_1 = str(mode)
    if mode_1 == "q":
        break
    if mode == 1:
        mode_1 = int(input("""计算第n个斐波那契数请输入1
列出1~n个斐波那契数请输入2
判断一个数是否为斐波那契数请输入3
请输入："""))
        if mode_1 == 1:
            print("计算第几个斐波那契数？")
            number = int(input("请输入："))


            def fibonacci_sequence(n_0):
                if n_0 < 2:
                    return n_0
                a_1, b_1 = 0, 1
                for i_1 in range(1, n_0):
                    a_1, b_1 = b_1, a_1 + b_1
                return b_1


            print(fibonacci_sequence(number))
        elif mode_1 == 2:
            print("列出1到第几个斐波那契数？")
            number = int(input("请输入："))
            results = []


            def fibonacci_sequence(n_0):
                if n_0 < 2:
                    return n_0
                a_1, b_1 = 0, 1
                for i_1 in range(1, n_0):
                    a_1, b_1 = b_1, a_1 + b_1
                return b_1


            for i in range(1, number + 1):
                results.append(fibonacci_sequence(i))
            text = "\n".join(str(i_7) for i_7 in results)
            total = sum(results)
            print(f"第1~{number}个斐波那契数分别是{text}\n它们的和为{total}")
        elif mode_1 == 3:
            num = int(input("请输入要判断的数："))
            val = 0
            cnt = 0
            n = 1


            def fibonacci_sequence(n_0):
                if n_0 < 2:
                    return n_0
                a_1, b_1 = 0, 1
                for i_1 in range(1, n_0):
                    a_1, b_1 = b_1, a_1 + b_1
                return b_1


            while num > val:
                val = fibonacci_sequence(n)
                cnt += 1
                n += 1
            if val == num:
                print(f"{num}是第{cnt}个斐波那契数")
            else:
                print(f"{num}不是斐波那契数")
    elif mode == 2:
        print("要计算哪个数的阶乘？")
        number = int(input("请输入："))
        factorial = combinatorial.factorial(number)

    elif mode == 3:
        number = int(input("请输入n的值："))
        sum_result = 0
        for i in range(1, number + 1):
            sum_result += i
        print(sum_result)

    elif mode == 4:
        number = int(input("请输入要判断的数："))
        start = time.time()
        rest = prime.millerRabin(number)
        if rest:
            rest = f"{number}是质数"
        else:
            rest = f"{number}不是质数"
        print(rest)
        print(f"\n运行时间：{(time.time() - start)}秒")

    elif mode == 5:
        mp.dps = int(input("请输入结果的精度：")) + 1
        start = time.time()
        result = mp.pi
        Result = str(result)
        p = Result.split(".", 1)[1]
        b = Result.split(".", 1)[0]
        cnt = 0
        print(f"{b}.")
        for i in p:
            cnt += 1
            print(i, end="")
            if cnt % 10 == 0:
                print(" ", end="")
            if cnt % 50 == 0:
                print(f"     :{cnt}位")
        print(f"\n运行时间：{time.time() - start}秒")

    elif mode == 6:
        a_0 = int(input("请输入第一个数："))
        b_0 = int(input("请输入第二个数：")) + 1
        list_2 = []
        for i_c in sympy.primerange(a_0, b_0):
            list_2.append(i_c)
        he = sum(list_2)
        length = len(list_2)
        text = "、".join(str(i_7) for i_7 in list_2)
        print(f"{a_0}到{b_0}一共有{length}个质数\n它们分别是{text}\n它们的和为{he}")

    elif mode == 7:
        print("请输入计算自然常数的精度")
        mp.dps = int(input("请输入：")) + 1
        start = time.time()
        result = mp.e
        Result = str(result)
        p = Result.split(".", 1)[1]
        b = Result.split(".", 1)[0]
        cnt = 0
        print(f"{b}.")
        for i in p:
            cnt += 1
            print(i, end="")
            if cnt % 10 == 0:
                print(" ", end="")
            if cnt % 50 == 0:
                print(f"     :{cnt}位")
        print(f"\n运行时间：{time.time() - start}秒")

    elif mode == 8:
        print("请输入要约分的分数（例如：6/12）")
        numerator, denominator = map(int, input("").split("/"))
        x, y_f = numerator, denominator
        while denominator > 0:
            numerator, denominator = denominator, numerator % denominator
        x = int(x / numerator)
        y_f = int(y_f / numerator)
        fractional = str(x) + "/" + str(y_f)
        print("约分后的分数为：", fractional)

    elif mode == 9:
        num1 = int(input("请输入一个整数："))
        num2 = int(input("请输入另一个整数："))
        num_1 = num1
        num_2 = num2
        result = num_1 % num_2
        while result != 0:
            num_1 = num_2
            num_2 = result
            result = num_1 % num_2
        print("%d与%d的最大公因数是：%d" % (num1, num2, num_2))
        print("%d与%d的最小公倍数是：%d" % (num1, num2, num1 * num2 / num_2))

    elif mode == 10:
        while True:
            b = int(input("请输入第一个数的分母："))
            a = int(input("请输入第一个数的分子："))
            d = int(input("请输入第二个数的分母："))
            c = int(input("请输入第二个数的分母："))
            e = Fraction(a, b)
            f_1 = Fraction(c, d)
            print("运算方法：加请输入1、减请输入2、乘请输入3、除请输入4")
            g = int(input("请输入计算方法："))
            if g == 1:
                print(e + f_1)
                break
            elif g == 2:
                print(e - f_1)
                break
            elif g == 3:
                print(e * f_1)
                break
            elif g == 4:
                print(e / f_1)
                break
            else:
                print("输入错误！")
                break

    elif mode == 11:
        str_1 = input("请输入循环小数的循环节：")
        num_1 = int(str_1)
        num_2 = int(len(str_1) * str(9))
        fractional = (Fraction(num_1, num_2))
        print(f"循环小数转分数的结果为：{fractional}")

    elif mode == 12:
        number = int(input("请输入要开根号的数字："))
        getcontext().prec = 100
        result_2 = int(Decimal(number) ** Decimal(0.5))
        result_1 = str(result_2)
        p_1 = len(result_1.split(".", 1)[0])
        getcontext().prec = int(input("请输入结果的精度：")) + p_1
        start = time.time()
        result = Decimal(number) ** Decimal(0.5)
        Result = str(result)
        p = Result.split(".", 1)[1]
        b = Result.split(".", 1)[0]
        cnt = 0
        print(f"{b}.")
        for i in p:
            cnt += 1
            print(i, end="")
            if cnt % 10 == 0:
                print(" ", end="")
            if cnt % 50 == 0:
                print(f"     :{cnt}位")
        print(f"\n运行时间：{time.time() - start}秒")

    elif mode == 13:
        number = int(input("请输入要开根号的数字："))
        root = int(input("请输入开几次方根："))
        getcontext().prec = 100
        result_2 = int(Decimal(number) ** Decimal(1 / root))
        result_1 = str(result_2)
        p_1 = len(result_1.split(".", 1)[0])
        getcontext().prec = int(input("请输入结果的精度：")) + p_1
        start = time.time()
        result = Decimal(number) ** Decimal(1 / root)
        Result = str(result)
        p = Result.split(".", 1)[1]
        b = Result.split(".", 1)[0]
        cnt = 0
        print(f"{b}.")
        for i in p:
            cnt += 1
            print(i, end="")
            if cnt % 10 == 0:
                print(" ", end="")
            if cnt % 50 == 0:
                print(f"     :{cnt}位")
        print(f"\n运行时间：{time.time() - start}秒")

    elif mode == 14:
        power = int(input("要开几次方："))
        number = int(input(f"要计算哪个数的{power}次方："))
        result_1 = int(mp.power(number, power))
        result = str(result_1)
        print(f"{number}的{power}次方是{result}")

    elif mode == 15:
        number = float(input("请输入要计算哪个数的自然对数："))
        number_1 = str(number)
        mp.dps = int(input("请输入精度："))
        natural_logarithm = mp.ln(number)
        print(f"{number_1}的自然对数是{natural_logarithm}")

    elif mode == 16:
        number = float(input("请输入要计算哪个数的任意数对数："))
        number_1 = str(number)
        base = float(input("请输入底数："))
        mp.dps = int(input("请输入精度："))
        logarithm = mp.log(number, base)
        print(f"以{base}为底，{number_1}的对数是{logarithm}")

    elif mode == 17:
        def factorial_summation(n_5):
            factorial_1 = 1
            for i_1 in range(1, n_5 + 1):
                factorial_1 *= i_1
            return factorial_1


        number = int(input("请输入n的值："))
        print("和为 %d" % sum(map(factorial_summation, range(1, number + 1))))

    elif mode == 18:
        x = int(input("请输入n的值："))
        power = int(input(f"请输入1到{x}的几次方和："))
        power_summation = 0
        for i in range(1, x + 1):
            power_summation += int(mp.power(i, power))
        print(f"1到{x}的{power}次方和为{power_summation}")

    elif mode == 19:
        a = int(input("请输入第一个数："))
        b = int(input("请输入第二个数："))
        power = int(input(f"请输入{a}到{b}的几次方和："))
        power_summation = 0
        for i in range(a, b + 1):
            power_summation += int(mp.power(i, power))
        print(f"{a}到{b}的{power}次方和为{power_summation}")

    elif mode == 20:
        a = int(input("请输入第一个数："))
        b = int(input("请输入第二个数："))
        summation = 0
        result = []
        for i in range(a, b + 1):
            result.append(i)
        summation = np.sum(result)
        print(f"{a}到{b}所有整数的和为：{summation}")

    elif mode == 21:
        numerator = int(input("请输入分子："))
        denominator = int(input("请输入分母："))


        def repetend(numerator_1, denominator_1):
            integer = str(numerator_1 // denominator_1)
            fractional_1 = ""
            remainder = [numerator_1 % denominator_1]
            while True:
                x_1, y_1 = divmod(remainder[-1] * 10, denominator_1)
                fractional_1 += str(x_1)
                remainder.append(y_1)
                i_2 = remainder.index(remainder[-1])
                if i_2 != len(remainder) - 1:
                    remainder_1 = fractional_1[i_2:]
                    fractional_1 = fractional_1[:i_2] + "[" + fractional_1[i_2:] + "]"
                    break
            r = integer + "." + fractional_1
            if r.endswith("[0]"):
                r = r[:-3]
            if r.endswith("."):
                r = r[:-1]
            return r, remainder_1


        result, repetend_1 = repetend(numerator, denominator)
        length = len(repetend_1)
        print(f"""{numerator}/{denominator}转化为小数为：{result}，循环节是：{repetend_1}，循环节长度为：{length}""")

    elif mode == 22:
        class Solution:
            @staticmethod
            def countprimes(n_3: int):
                if n_3 < 3:
                    return 0
                else:
                    output = [1] * n_3
                    output[0], output[1] = 0, 0
                    for i_4 in range(2, int(n_3 ** 0.5) + 1):
                        if output[i_4] == 1:
                            output[i_4 * i_4: n_3: i_4] = [0] * len(output[i_4 * i_4: n_3: i_4])
                return sum(output)


        number = int(input("请输入一个数："))
        s_1 = Solution()
        a = s_1.countprimes(number)
        print(f"1~{number}里有{a}个质数")

    elif mode == 23:
        number = int(input("请输入要分解质因数的数："))
        a = sympy.factorint(number)
        b = []
        for key, value in a.items():
            if value == 1:
                b.append(str(key))
            else:
                b.append(f"{key}^{value}")
        text = " * ".join(str(i_7) for i_7 in b)
        print(f"{number} = {text}")

    elif mode == 24:
        def isprime(n_3):
            if n_3 < 2:
                return False
            for i_7 in range(2, int(math.sqrt(n_3)) + 1):
                if n_3 % i_7 == 0:
                    return False
            return True


        def issuperprime(n_8):
            n_str = str(n_8)
            for i_6 in range(len(n_str)):
                cur_n = n_str[:len(n_str) - i_6]
                if not isprime(int(cur_n)):
                    return False
            return True


        n = input("请输入一个整数:")
        n = int(n)
        if issuperprime(n):
            print("{} 是一个超级质数".format(n))
        else:
            print("{} 不是超级质数".format(n))

    elif mode == 25:
        x = int(input("请输入一个整数："))
        x_8 = str(x)
        text = sympy.divisors(x)
        count = len(text)
        list4 = []
        for c in text:
            list4.append(int(c))
        text = "、".join(str(i_7) for i_7 in list4)
        total = np.sum(list4)
        print(f"{x_8}的因数有{text}\n一共有{count}个\n因数和为{total}")

    elif mode == 26:
        x = input("请输入一个整数：")
        list1 = [i for i in range(1, int(x) + 1)]
        list2 = list1[:: - 1]
        list3 = []
        count = 0
        for a in list1:
            for b in list2:
                if a * b == int(x):
                    list3.append(int(a))
                    count += 1
        list4 = []
        for c in list3:
            list4.append(int(c))
        total = np.sum(list4)
        total_1 = total - int(x)
        if int(x) == total_1:
            print(f"{x}是完全数")
        else:
            print(f"{x}不是完全数")
    elif mode == 27:
        number = int(input("请输入要计算第几个质数："))
        prime_1 = sympy.prime(number)
        print("第" + str(number) + "个质数是" + str(prime_1))
    elif mode == 28:
        s_1 = int(input("请输入要计算几边形数："))
        if s_1 <= 2:
            print("输入错误！")
        else:
            n = int(input(f"请输入要计算第几个{s_1}边形数："))
            val = int(((s_1 - 2) * n * n - (s_1 - 4) * n) / 2)
            print(f"第{n}个{s_1}边形数是{val}")
    elif mode == 29:
        def polygon_number(number_3, side):
            n_5 = 1
            val_1 = 1
            count_1 = 0
            while val_1 < number_3:
                val_1 = int(((side - 2) * n_5 * n_5 - (side - 4) * n_5) / 2)
                n_5 += 1
                count_1 += 1
            if val_1 == number_3:
                print(f"{number_3}是第{count_1}个{side}边形数")
            if val_1 > number_3:
                print(f"{number_3}不是{side}边形数")


        s_1 = int(input("请输入判断是否为几边形数："))
        if s_1 <= 2:
            print("输入错误！")
            continue
        else:
            n = int(input(f"请输入要判断是否为{s_1}边形数的数："))
            polygon_number(n, s_1)
    elif mode == 30:
        x = int(input("请输入要判断的数："))
        y_f = str(x)
        binary = bin(x)[2:]
        summation = 0
        n = eval(binary)
        while n != 0:
            summation += n % 10
            n //= 10
        if summation % 2 == 1:
            print(f"{y_f}是可恶数")
        elif summation % 2 == 0:
            print(f"{y_f}是邪恶数")
        else:
            print("错误！")
            continue
    elif mode == 31:
        def reverse_digits(num_0):
            rev = 0
            while num_0 > 0:
                rev = rev * 10 + num_0 % 10
                num_0 //= 10
            return rev


        def square(num_3):
            return num_3 * num_3


        def check_adam_number(num_4):
            a_2 = square(num_4)
            b_2 = square(reverse_digits(num_4))
            if a_2 == reverse_digits(b_2):
                return True
            else:
                return False


        num = int(input("请输入要判断的数："))
        if check_adam_number(num):
            print(f"{num}是亚当数")
        else:
            print(f"{num}不是亚当数")
    elif mode == 32:
        def primes(n_a):
            prime_b = [True] * (n_a + 1)
            i_11 = 2
            while i_11 * i_11 <= n_a:
                if prime_b[i_11]:
                    j_2 = i_11 * 2
                    while j_2 <= n_a:
                        prime_b[j_2] = False
                        j_2 += i_11
                i_11 += 1
            arr = []
            for i_11 in range(2, n_a):
                if prime_b[i_11]:
                    arr.append(i_11)
            return arr


        def count_digits(n_c):
            temp = n_c
            c_1 = 0
            while temp != 0:
                temp = int(temp / 10)
                c_1 += 1
            return c_1


        def frugal(n_b):
            r = primes(n_b)
            t = n_b
            s_5 = 0
            for i_12 in range(len(r)):
                if t % r[i_12] == 0:
                    k = 0
                    while t % r[i_12] == 0:
                        t = int(t / r[i_12])
                        k += 1
                    if k == 1:
                        s_5 += count_digits(r[i_12])
                    elif k != 1:
                        s_5 = (s_5 + count_digits(r[i_12]) +
                               count_digits(k))
            return count_digits(n_b) > s_5 != 0


        n = int(input("请输入要判断的数："))
        if frugal(n):
            print(f"{n}是节俭数")
        else:
            print(f"{n}不是节俭数")
    if mode == 33:
        def number_cake(n_d):
            return (n_d * n_d * n_d + 5 * n_d + 6) // 6


        n = int(input("要计算第几个蛋糕数："))
        print(f"第{n}个蛋糕数是", number_cake(n))
    if mode == 34:
        def check_cake_number(numb):
            n_d = 1
            val_1 = 1
            count_1 = 0
            while val_1 < numb:
                val_1 = int((n_d * n_d * n_d + 5 * n_d + 6) // 6)
                n_d += 1
                count_1 += 1
            if val_1 == numb:
                print(f"{numb}是第{count_1}个蛋糕数")
            if val_1 > numb:
                print(f"{numb}不是蛋糕数")


        n = int(input(f"请输入要判断是否为蛋糕数的数："))
        check_cake_number(n)
    if mode == 35:
        ans, n = 1, int(input("请输入要计算到第几个卡特兰数："))
        result = [1]
        for i in range(2, n + 1):
            ans = int(ans * (4 * i - 2) // (i + 1))
            result.append(ans)
        results = []
        for c in result:
            results.append(int(c))
        text = "、".join(str(i_7) for i_7 in results)
        total = np.sum(results)
        print(f"第1~{n}个卡特兰数分别是{text}\n它们的和为{total}")
    if mode == 36:
        number = int(input("请输入要判断是否为卡特兰数的数："))
        i = 1
        ans = 1
        cnt = 1
        while ans < number:
            ans = int(ans * (4 * i - 2) // (i + 1))
            i += 1
            cnt += 1
        if ans > number:
            print(f"{number}不是卡特兰数")
        elif ans == number:
            print(f"{number}是第{cnt}个卡特兰数")
    elif mode == 37:
        print("要计算第几个帕多瓦数？")
        n = int(input("请输入："))
        m = str(n)
        li = [1, 1, 1]
        while len(li) < n:
            li.append(li[-2] + li[-3])
        result = str(li[-1])
        print(f"第{m}个帕多瓦数是" + result)
    elif mode == 38:
        print("列出1到第几个帕多瓦数？")
        n = int(input("请输入："))
        li = [1, 1, 1]
        while len(li) < n:
            li.append(li[-2] + li[-3])
        text = "、".join(str(i_7) for i_7 in li)
        total = np.sum(li)
        print(f"第1~{n}个帕多瓦数分别是{text}\n它们的和为{total}")
    elif mode == 39:
        print("提示：上标应大于或等于下标")
        m = int(input("请输入上标："))
        n = int(input("请输入下标："))
        if n < m:
            print("上标应大于或等于下标！")
            continue
        else:
            result = combinatorial.binomial(n, m)
            print(result)
    elif mode == 40:
        number = int(input("请输入要计算第几个伯努利数："))
        print(f"第{str(number)}个伯努利数是" + str(combinatorial.bernoulli(number)))
    elif mode == 41:
        number = int(input("请输入要计算第几个欧拉数："))
        print(f"第{str(number)}个欧拉数是" + str(combinatorial.euler(number)))
    elif mode == 42:
        number = int(input("请输入要计算第几个贝尔数："))
        print(f"第{str(number)}个贝尔数是" + str(combinatorial.bell(number)))
    elif mode == 43:
        print("列出1到第几个贝尔数？")
        n = int(input("请输入："))
        li = []
        for i in range(1, n + 1):
            li.append(combinatorial.bell(i))
        text = "、".join(str(i_7) for i_7 in li)
        total = np.sum(li)
        print(f"第1~{n}个贝尔数分别是{text}\n它们的和为{total}")
    elif mode == 44:
        x = input("请输入一个整数：")
        list1 = [i for i in range(1, int(x) + 1)]
        list2 = list1[:: - 1]
        list3 = []
        count = 0
        for a in list1:
            for b in list2:
                if a * b == int(x):
                    list3.append(int(a))
                    count += 1
        list4 = []
        for c in list3:
            list4.append(int(c))
        total = 0
        for num in list4:
            total += num
        total_1 = total - int(x)
        if int(x) < total_1:
            print(f"{x}是过剩数")
        elif int(x) > total_1:
            print(f"{x}是不足数")
        else:
            print(f"{x}是完全数")
    elif mode == 45:
        mode_1 = int(input("""计算第n个普洛尼克数请输入1
列出0到n个普洛尼克数请输入2
判断是否为普洛尼克数请输入3
请输入："""))
        if mode_1 == 1:
            number = int(input("请输入要计算第几个普洛尼克数："))
            if number < 0:
                print("错误！")
                continue
            else:
                pronic_number = number * (number + 1)
                print(f"第{number}个普洛尼克数是{pronic_number}")
        elif mode_1 == 2:
            number = int(input("请输入n的值："))
            result = [0]
            for i in range(1, number + 1):
                result.append(i * (i + 1))
            text = "、".join(str(i_7) for i_7 in result)
            total = np.sum(result)
            print(f"第0~{number}个普洛尼克数分别是{text}\n它们的和为{total}")
        elif mode_1 == 3:
            number = int(input("请输入要判断的数："))
            val = 0
            cnt = 0
            n = 0
            if number == 0:
                print("0是第0个普洛尼克数")
            else:
                while number > val:
                    val = n * (n + 1)
                    cnt += 1
                    n += 1
                if val == number:
                    print(f"{number}是第{cnt - 1}个普洛尼克数")
                else:
                    print(f"{number}不是普洛尼克数")
        else:
            print("错误！")
            continue
    elif mode == 46:
        print("""计算黄金比例请输入1
计算白银比例请输入2
计算青铜比例请输入3
计算第n贵金属比例请输入4
计算超黄金比例请输入5
计算塑胶数请输入6""")
        mode_1 = int(input("请输入："))
        if mode_1 == 1:
            mp.dps = int(input("请输入结果的精度：")) + 1
            start = time.time()
            result = mp.phi
            Result = str(result)
            p = Result.split(".", 1)[1]
            b = Result.split(".", 1)[0]
            cnt = 0
            print(f"{b}.")
            for i in p:
                cnt += 1
                print(i, end="")
                if cnt % 10 == 0:
                    print(" ", end="")
                if cnt % 50 == 0:
                    print(f"     :{cnt}位")
            print(f"\n运行时间：{time.time() - start}秒")
        elif mode_1 == 2:
            getcontext().prec = int(input("请输入结果的精度：")) + 1
            start = time.time()
            result = Decimal(2) ** Decimal(0.5) + 1
            Result = str(result)
            p = Result.split(".", 1)[1]
            b = Result.split(".", 1)[0]
            cnt = 0
            print(f"{b}.")
            for i in p:
                cnt += 1
                print(i, end="")
                if cnt % 10 == 0:
                    print(" ", end="")
                if cnt % 50 == 0:
                    print(f"     :{cnt}位")
            print(f"\n运行时间：{time.time() - start}秒")
        elif mode_1 == 3:
            getcontext().prec = int(input("请输入结果的精度：")) + 1
            start = time.time()
            result = (Decimal(13) ** Decimal(0.5) + 3) / 2
            Result = str(result)
            p = Result.split(".", 1)[1]
            b = Result.split(".", 1)[0]
            cnt = 0
            print(f"{b}.")
            for i in p:
                cnt += 1
                print(i, end="")
                if cnt % 10 == 0:
                    print(" ", end="")
                if cnt % 50 == 0:
                    print(f"     :{cnt}位")
            print(f"\n运行时间：{time.time() - start}秒")
        elif mode_1 == 4:
            number = int(input("请输入要第几个贵金属比例："))
            n = str(number)
            length = len(n)
            precision = int(input("请输入结果的精度："))
            getcontext().prec = precision + length + 10
            start = time.time()
            result = (Decimal(n) + ((Decimal(n) ** Decimal(2) + Decimal(4)) ** Decimal(0.5))) / Decimal(2)
            result_1 = result.quantize(decimal.Decimal(f"1E-{precision}"))
            Result = str(result_1)
            p = Result.split(".", 1)[1]
            b = Result.split(".", 1)[0]
            cnt = 0
            print(f"{b}.")
            for i in p:
                cnt += 1
                print(i, end="")
                if cnt % 10 == 0:
                    print(" ", end="")
                if cnt % 50 == 0:
                    print(f"     :{cnt}位")
            print(f"\n运行时间：{time.time() - start}秒")
        if mode_1 == 5:
            getcontext().prec = int(input("请输入结果的精度：")) + 1
            start = time.time()
            result_1 = ((Decimal(29) + Decimal(3) * Decimal(93) ** Decimal(0.5)) / Decimal(2)) ** Decimal(1 / 3)
            result_2 = ((Decimal(29) - Decimal(3) * Decimal(93) ** Decimal(0.5)) / Decimal(2)) ** Decimal(1 / 3)
            result = (1 + result_1 + result_2) / 3
            Result = str(result)
            p = Result.split(".", 1)[1]
            b = Result.split(".", 1)[0]
            cnt = 0
            print(f"1.")
            for i in p:
                cnt += 1
                print(i, end="")
                if cnt % 10 == 0:
                    print(" ", end="")
                if cnt % 50 == 0:
                    print(f"     :{cnt}位")
            print(f"\n运行时间：{time.time() - start}秒")
        elif mode_1 == 6:
            getcontext().prec = int(input("请输入结果的精度：")) + 1
            start = time.time()
            result_1 = (Decimal(1 / 2) + Decimal(1 / 6) * (Decimal(23 / 3) ** Decimal(0.5))) ** Decimal(1 / 3)
            result_2 = (Decimal(1 / 2) - Decimal(1 / 6) * (Decimal(23 / 3) ** Decimal(0.5))) ** Decimal(1 / 3)
            result = result_1 + result_2
            Result = str(result)
            p = Result.split(".", 1)[1]
            b = Result.split(".", 1)[0]
            cnt = 0
            print(f"1.")
            for i in p:
                cnt += 1
                print(i, end="")
                if cnt % 10 == 0:
                    print(" ", end="")
                if cnt % 50 == 0:
                    print(f"     :{cnt}位")
            print(f"\n运行时间：{time.time() - start}秒")
    elif mode == 47:
        mp.dps = int(input("请输入结果的精度："))
        start = time.time()
        result = 1 / agm(sqrt(2), 1)
        Result = str(result)
        p = Result.split(".", 1)[1]
        b = Result.split(".", 1)[0]
        cnt = 0
        print(f"{b}.")
        for i in p:
            cnt += 1
            print(i, end="")
            if cnt % 10 == 0:
                print(" ", end="")
            if cnt % 50 == 0:
                print(f"     :{cnt}位")
        print(f"\n运行时间：{time.time() - start}秒")
    elif mode == 48:
        mp.dps = int(input("请输入结果的精度：")) + 1
        start = time.time()
        result = mp.apery
        Result = str(result)
        p = Result.split(".", 1)[1]
        b = Result.split(".", 1)[0]
        cnt = 0
        print(f"{b}.")
        for i in p:
            cnt += 1
            print(i, end="")
            if cnt % 10 == 0:
                print(" ", end="")
            if cnt % 50 == 0:
                print(f"     :{cnt}位")
        print(f"\n运行时间：{time.time() - start}秒")
    elif mode == 49:
        mp.dps = int(input("请输入结果的精度："))
        start = time.time()
        result = mp.euler
        Result = str(result)
        p = Result.split(".", 1)[1]
        b = Result.split(".", 1)[0]
        cnt = 0
        print(f"{b}.")
        for i in p:
            cnt += 1
            print(i, end="")
            if cnt % 10 == 0:
                print(" ", end="")
            if cnt % 50 == 0:
                print(f"     :{cnt}位")
        print(f"\n运行时间：{time.time() - start}秒")
    elif mode == 50:
        mp.dps = int(input("请输入结果的精度："))
        start = time.time()
        result = mp.catalan
        Result = str(result)
        p = Result.split(".", 1)[1]
        b = Result.split(".", 1)[0]
        cnt = 0
        print(f"{b}.")
        for i in p:
            cnt += 1
            print(i, end="")
            if cnt % 10 == 0:
                print(" ", end="")
            if cnt % 50 == 0:
                print(f"     :{cnt}位")
        print(f"\n运行时间：{time.time() - start}秒")
    elif mode == 51:
        mp.dps = int(input("请输入结果的精度：")) + 1
        start = time.time()
        result = mp.khinchin
        Result = str(result)
        p = Result.split(".", 1)[1]
        b = Result.split(".", 1)[0]
        cnt = 0
        print(f"{b}.")
        for i in p:
            cnt += 1
            print(i, end="")
            if cnt % 10 == 0:
                print(" ", end="")
            if cnt % 50 == 0:
                print(f"     :{cnt}位")
        print(f"\n运行时间：{time.time() - start}秒")
    elif mode == 52:
        mp.dps = int(input("请输入结果的精度：")) + 1
        start = time.time()
        result = mp.glaisher
        Result = str(result)
        p = Result.split(".", 1)[1]
        b = Result.split(".", 1)[0]
        cnt = 0
        print(f"{b}.")
        for i in p:
            cnt += 1
            print(i, end="")
            if cnt % 10 == 0:
                print(" ", end="")
            if cnt % 50 == 0:
                print(f"     :{cnt}位")
        print(f"\n运行时间：{time.time() - start}秒")
    elif mode == 53:
        mp.dps = int(input("请输入结果的精度："))
        start = time.time()
        result = mp.mertens
        Result = str(result)
        p = Result.split(".", 1)[1]
        b = Result.split(".", 1)[0]
        cnt = 0
        print(f"{b}.")
        for i in p:
            cnt += 1
            print(i, end="")
            if cnt % 10 == 0:
                print(" ", end="")
            if cnt % 50 == 0:
                print(f"     :{cnt}位")
        print(f"\n运行时间：{time.time() - start}秒")
    elif mode == 54:
        mp.dps = int(input("请输入结果的精度："))
        start = time.time()
        result = mp.twinprime
        Result = str(result)
        p = Result.split(".", 1)[1]
        b = Result.split(".", 1)[0]
        cnt = 0
        print(f"{b}.")
        for i in p:
            cnt += 1
            print(i, end="")
            if cnt % 10 == 0:
                print(" ", end="")
            if cnt % 50 == 0:
                print(f"     :{cnt}位")
        print(f"\n运行时间：{time.time() - start}秒")
    if mode == 55:
        def decompose(a_a, start_1):
            result_5 = str(a_a)
            if "j" in result_5:
                print("错误！")
                exit()
            p_a = result_5.split(".", 1)[1]
            b_3 = result_5.split(".", 1)[0]
            cnt_1 = 0
            print(f"{b_3}.")
            for i_a in p_a:
                cnt_1 += 1
                print(i_a, end="")
                if cnt_1 % 10 == 0:
                    print(" ", end="")
                if cnt_1 % 50 == 0:
                    print(f"     :{cnt_1}位")
            print(f"\n运行时间：{time.time() - start_1}秒")


        text = """使用三角函数合集请输入1
使用双曲函数合集请输入2
请输入："""
        mode_1 = int(input(text))
        if mode_1 == 1:
            text = """使用三角函数小合集请输入1
使用反三角函数小合集请输入2
请输入："""
            mode_2 = int(input(text))
            if mode_2 == 1:
                text = """使用正弦函数(sin)请输入1
使用余弦函数(cos)请输入2
使用正切函数(tan)请输入3
使用余切函数(cot)请输入4
使用正割函数(sec)请输入5
使用余割函数(csc)请输入6
请输入："""
                mode_3 = int(input(text))
                if mode_3 == 1:
                    number = int(input("请输入要计算的数："))
                    mp.dps = int(input("请输入精度："))
                    start = time.time()
                    print(f"sin({number}) =\n")
                    decompose(mp.sin(number), start)
                if mode_3 == 2:
                    number = int(input("请输入要计算的数："))
                    mp.dps = int(input("请输入精度："))
                    start = time.time()
                    print(f"cos({number}) =\n")
                    decompose(mp.cos(number), start)
                if mode_3 == 3:
                    number = int(input("请输入要计算的数："))
                    mp.dps = int(input("请输入精度："))
                    start = time.time()
                    print(f"tan({number}) =\n")
                    decompose(mp.tan(number), start)
                if mode_3 == 4:
                    number = int(input("请输入要计算的数："))
                    mp.dps = int(input("请输入精度：")) + 1
                    start = time.time()
                    print(f"cot({number}) =\n")
                    decompose(mp.cot(number), start)
                if mode_3 == 5:
                    number = int(input("请输入要计算的数："))
                    mp.dps = int(input("请输入精度：")) + 1
                    start = time.time()
                    print(f"sec({number}) =\n")
                    decompose(mp.sec(number), start)
                if mode_3 == 6:
                    number = int(input("请输入要计算的数："))
                    mp.dps = int(input("请输入精度：")) + 1
                    start = time.time()
                    print(f"csc({number}) =\n")
                    decompose(mp.csc(number), start)
            if mode_2 == 2:
                text = """使用反正弦函数(arcsin)请输入1
使用反余弦函数(arccos)请输入2
使用反正切函数(arctan)请输入3
使用反余切函数(arccot)请输入4
使用反正割函数(arcsec)请输入5
使用反余割函数(arccsc)请输入6
请输入："""
                mode_3 = int(input(text))
                if mode_3 == 1:
                    number = int(input("请输入要计算的数："))
                    mp.dps = int(input("请输入精度："))
                    start = time.time()
                    print(f"arcsin({number}) =\n")
                    decompose(mp.asin(number), start)
                if mode_3 == 2:
                    number = int(input("请输入要计算的数："))
                    mp.dps = int(input("请输入精度："))
                    start = time.time()
                    print(f"arccos({number}) =\n")
                    decompose(mp.acos(number), start)
                if mode_3 == 3:
                    number = int(input("请输入要计算的数："))
                    mp.dps = int(input("请输入精度："))
                    start = time.time()
                    print(f"arctan({number}) =\n")
                    decompose(mp.atan(number), start)
                if mode_3 == 4:
                    number = int(input("请输入要计算的数："))
                    mp.dps = int(input("请输入精度：")) + 1
                    start = time.time()
                    print(f"arccot({number}) =\n")
                    decompose(mp.acot(number), start)
                if mode_3 == 5:
                    number = int(input("请输入要计算的数："))
                    mp.dps = int(input("请输入精度：")) + 1
                    start = time.time()
                    print(f"arcsec({number}) =\n")
                    decompose(mp.asec(number), start)
                if mode_3 == 6:
                    number = int(input("请输入要计算的数：")) + 1
                    mp.dps = int(input("请输入精度："))
                    start = time.time()
                    print(f"arccsc({number}) =\n")
                    decompose(mp.acsc(number), start)
        if mode_1 == 2:
            text = """使用三角函数小合集请输入1
        使用反三角函数小合集请输入2
        请输入："""
            mode_2 = int(input(text))
            if mode_2 == 1:
                text = """使用双曲正弦函数(sinh)请输入1
使用双曲余弦函数(cosh)请输入2
使用双曲正切函数(tanh)请输入3
使用双曲余切函数(coth)请输入4
使用双曲正割函数(sech)请输入5
使用双曲余割函数(csch)请输入6
请输入："""
                mode_3 = int(input(text))
                if mode_3 == 1:
                    number = int(input("请输入要计算的数："))
                    mp.dps = int(input("请输入精度："))
                    start = time.time()
                    print(f"sinh({number}) =\n")
                    decompose(mp.sinh(number), start)
                if mode_3 == 2:
                    number = int(input("请输入要计算的数："))
                    mp.dps = int(input("请输入精度："))
                    start = time.time()
                    print(f"cosh({number}) =\n")
                    decompose(mp.cosh(number), start)
                if mode_3 == 3:
                    number = int(input("请输入要计算的数："))
                    mp.dps = int(input("请输入精度："))
                    start = time.time()
                    print(f"tanh({number}) =\n")
                    decompose(mp.tanh(number), start)
                if mode_3 == 4:
                    number = int(input("请输入要计算的数："))
                    mp.dps = int(input("请输入精度：")) + 1
                    start = time.time()
                    print(f"coth({number}) =\n")
                    decompose(mp.coth(number), start)
                if mode_3 == 5:
                    number = int(input("请输入要计算的数："))
                    mp.dps = int(input("请输入精度：")) + 1
                    start = time.time()
                    print(f"sech({number}) =\n")
                    decompose(mp.sech(number), start)
                if mode_3 == 6:
                    number = int(input("请输入要计算的数："))
                    mp.dps = int(input("请输入精度：")) + 1
                    start = time.time()
                    print(f"csch({number}) =\n")
                    decompose(mp.csch(number), start)
            if mode_2 == 2:
                text = """使用反双曲正弦函数(arsinh)请输入1
使用反双曲余弦函数(arcosh)请输入2
使用反双曲正切函数(artanh)请输入3
使用反双曲余切函数(arcoth)请输入4
使用反双曲正割函数(arsech)请输入5
使用反双曲余割函数(arcsch)请输入6
请输入："""
                mode_3 = int(input(text))
                if mode_3 == 1:
                    number = int(input("请输入要计算的数："))
                    mp.dps = int(input("请输入精度："))
                    start = time.time()
                    print(f"arsinh({number}) =\n")
                    decompose(mp.asinh(number), start)
                if mode_3 == 2:
                    number = int(input("请输入要计算的数："))
                    mp.dps = int(input("请输入精度："))
                    start = time.time()
                    print(f"arcosh({number}) =\n")
                    decompose(mp.acosh(number), start)
                if mode_3 == 3:
                    number = int(input("请输入要计算的数："))
                    mp.dps = int(input("请输入精度："))
                    start = time.time()
                    print(f"artanh({number}) =\n")
                    decompose(mp.tanh(number), start)
                if mode_3 == 4:
                    number = int(input("请输入要计算的数："))
                    mp.dps = int(input("请输入精度：")) + 1
                    start = time.time()
                    print(f"arcoth({number}) =\n")
                    decompose(mp.acoth(number), start)
                if mode_3 == 5:
                    number = int(input("请输入要计算的数："))
                    mp.dps = int(input("请输入精度：")) + 1
                    start = time.time()
                    print(f"arsech({number}) =\n")
                    decompose(mp.asech(number), start)
                if mode_3 == 6:
                    number = int(input("请输入要计算的数："))
                    mp.dps = int(input("请输入精度：")) + 1
                    start = time.time()
                    print(f"arcsch({number}) =\n")
                    decompose(mp.acsch(number), start)
    elif mode == 56:
        def decompose(a_a, start_1):
            result_5 = str(a_a)
            if "j" in result_5:
                print("错误！")
                exit()
            p_a = result_5.split(".", 1)[1]
            b_3 = result_5.split(".", 1)[0]
            cnt_1 = 0
            print(f"{b_3}.")
            for i_a in p_a:
                cnt_1 += 1
                print(i_a, end="")
                if cnt_1 % 10 == 0:
                    print(" ", end="")
                if cnt_1 % 50 == 0:
                    print(f"     :{cnt_1}位")
            print(f"\n运行时间：{time.time() - start_1}秒")


        text = """使用三角函数合集请输入1
使用双曲函数合集请输入2
请输入："""
        mode_1 = int(input(text))
        if mode_1 == 1:
            text = """使用三角函数小合集请输入1
使用反三角函数小合集请输入2
请输入："""
            mode_2 = int(input(text))
            if mode_2 == 1:
                text = """使用正弦函数(sin)请输入1
使用余弦函数(cos)请输入2
使用正切函数(tan)请输入3
使用余切函数(cot)请输入4
使用正割函数(sec)请输入5
使用余割函数(csc)请输入6
请输入："""
                mode_3 = int(input(text))
                if mode_3 == 1:
                    number = Decimal(input("请输入要计算的数："))
                    mp.dps = int(input("请输入精度："))
                    start = time.time()
                    print(f"sin({number}) =\n")
                    decompose(mp.sin(number), start)
                if mode_3 == 2:
                    number = Decimal(input("请输入要计算的数："))
                    mp.dps = int(input("请输入精度："))
                    start = time.time()
                    print(f"cos({number}) =\n")
                    decompose(mp.cos(number), start)
                if mode_3 == 3:
                    number = Decimal(input("请输入要计算的数："))
                    mp.dps = int(input("请输入精度："))
                    start = time.time()
                    print(f"tan({number}) =\n")
                    decompose(mp.tan(number), start)
                if mode_3 == 4:
                    number = Decimal(input("请输入要计算的数："))
                    mp.dps = int(input("请输入精度：")) + 1
                    start = time.time()
                    print(f"cot({number}) =\n")
                    decompose(mp.cot(number), start)
                if mode_3 == 5:
                    number = Decimal(input("请输入要计算的数："))
                    mp.dps = int(input("请输入精度：")) + 1
                    start = time.time()
                    print(f"sec({number}) =\n")
                    decompose(mp.sec(number), start)
                if mode_3 == 6:
                    number = Decimal(input("请输入要计算的数："))
                    mp.dps = int(input("请输入精度：")) + 1
                    start = time.time()
                    print(f"csc({number}) =\n")
                    decompose(mp.csc(number), start)
            if mode_2 == 2:
                text = """使用反正弦函数(arcsin)请输入1
使用反余弦函数(arccos)请输入2
使用反正切函数(arctan)请输入3
使用反余切函数(arccot)请输入4
使用反正割函数(arcsec)请输入5
使用反余割函数(arccsc)请输入6
请输入："""
                mode_3 = int(input(text))
                if mode_3 == 1:
                    number = Decimal(input("请输入要计算的数："))
                    mp.dps = int(input("请输入精度："))
                    start = time.time()
                    print(f"arcsin({number}) =\n")
                    decompose(mp.asin(number), start)
                if mode_3 == 2:
                    number = Decimal(input("请输入要计算的数："))
                    mp.dps = int(input("请输入精度："))
                    start = time.time()
                    print(f"arccos({number}) =\n")
                    decompose(mp.acos(number), start)
                if mode_3 == 3:
                    number = Decimal(input("请输入要计算的数："))
                    mp.dps = int(input("请输入精度："))
                    start = time.time()
                    print(f"arctan({number}) =\n")
                    decompose(mp.atan(number), start)
                if mode_3 == 4:
                    number = Decimal(input("请输入要计算的数："))
                    mp.dps = int(input("请输入精度：")) + 1
                    start = time.time()
                    print(f"arccot({number}) =\n")
                    decompose(mp.acot(number), start)
                if mode_3 == 5:
                    number = Decimal(input("请输入要计算的数："))
                    mp.dps = int(input("请输入精度：")) + 1
                    start = time.time()
                    print(f"arcsec({number}) =\n")
                    decompose(mp.asec(number), start)
                if mode_3 == 6:
                    number = Decimal(input("请输入要计算的数：")) + 1
                    mp.dps = int(input("请输入精度："))
                    start = time.time()
                    print(f"arccsc({number}) =\n")
                    decompose(mp.acsc(number), start)
        if mode_1 == 2:
            text = """使用三角函数小合集请输入1
使用反三角函数小合集请输入2
请输入："""
            mode_2 = int(input(text))
            if mode_2 == 1:
                text = """使用双曲正弦函数(sinh)请输入1
使用双曲余弦函数(cosh)请输入2
使用双曲正切函数(tanh)请输入3
使用双曲余切函数(coth)请输入4
使用双曲正割函数(sech)请输入5
使用双曲余割函数(csch)请输入6
请输入："""
                mode_3 = int(input(text))
                if mode_3 == 1:
                    number = Decimal(input("请输入要计算的数："))
                    mp.dps = int(input("请输入精度："))
                    start = time.time()
                    print(f"sinh({number}) =\n")
                    decompose(mp.sinh(number), start)
                if mode_3 == 2:
                    number = Decimal(input("请输入要计算的数："))
                    mp.dps = int(input("请输入精度："))
                    start = time.time()
                    print(f"cosh({number}) =\n")
                    decompose(mp.cosh(number), start)
                if mode_3 == 3:
                    number = Decimal(input("请输入要计算的数："))
                    mp.dps = int(input("请输入精度："))
                    start = time.time()
                    print(f"tanh({number}) =\n")
                    decompose(mp.tanh(number), start)
                if mode_3 == 4:
                    number = Decimal(input("请输入要计算的数："))
                    mp.dps = int(input("请输入精度：")) + 1
                    start = time.time()
                    print(f"coth({number}) =\n")
                    decompose(mp.coth(number), start)
                if mode_3 == 5:
                    number = Decimal(input("请输入要计算的数："))
                    mp.dps = int(input("请输入精度：")) + 1
                    start = time.time()
                    print(f"sech({number}) =\n")
                    decompose(mp.sech(number), start)
                if mode_3 == 6:
                    number = Decimal(input("请输入要计算的数："))
                    mp.dps = int(input("请输入精度：")) + 1
                    start = time.time()
                    print(f"csch({number}) =\n")
                    decompose(mp.csch(number), start)
            if mode_2 == 2:
                text = """使用反双曲正弦函数(arsinh)请输入1
使用反双曲余弦函数(arcosh)请输入2
使用反双曲正切函数(artanh)请输入3
使用反双曲余切函数(arcoth)请输入4
使用反双曲正割函数(arsech)请输入5
使用反双曲余割函数(arcsch)请输入6
请输入："""
                mode_3 = int(input(text))
                if mode_3 == 1:
                    number = Decimal(input("请输入要计算的数："))
                    mp.dps = int(input("请输入精度："))
                    start = time.time()
                    print(f"arsinh({number}) =\n")
                    decompose(mp.asinh(number), start)
                if mode_3 == 2:
                    number = Decimal(input("请输入要计算的数："))
                    mp.dps = int(input("请输入精度："))
                    start = time.time()
                    print(f"arcosh({number}) =\n")
                    decompose(mp.acosh(number), start)
                if mode_3 == 3:
                    number = Decimal(input("请输入要计算的数："))
                    mp.dps = int(input("请输入精度："))
                    start = time.time()
                    print(f"artanh({number}) =\n")
                    decompose(mp.tanh(number), start)
                if mode_3 == 4:
                    number = Decimal(input("请输入要计算的数："))
                    mp.dps = int(input("请输入精度：")) + 1
                    start = time.time()
                    print(f"arcoth({number}) =\n")
                    decompose(mp.acoth(number), start)
                if mode_3 == 5:
                    number = Decimal(input("请输入要计算的数："))
                    mp.dps = int(input("请输入精度：")) + 1
                    start = time.time()
                    print(f"arsech({number}) =\n")
                    decompose(mp.asech(number), start)
                if mode_3 == 6:
                    number = Decimal(input("请输入要计算的数："))
                    mp.dps = int(input("请输入精度：")) + 1
                    start = time.time()
                    print(f"arcsch({number}) =\n")
                    decompose(mp.acsch(number), start)
    elif mode == 57:
        def jacobsthal_number():
            a_f, b_f = 0, 1
            while True:
                yield a_f
                a_f, b_f = b_f, b_f + 2 * a_f


        number = int(input("请输入要列出到0到第几个雅各布斯塔尔数："))
        sequence = jacobsthal_number()
        result = [next(sequence) for i in range(number + 1)]
        text = "、".join(str(i_7) for i_7 in result)
        total = np.sum(result)
        print(f"第0~{number}个雅各布斯塔尔数分别是{text}\n它们的和为{total}")
    elif mode == 58:
        def jacobsthal_number():
            a_f, b_f = 0, 1
            while True:
                yield a_f
                a_f, b_f = b_f, b_f + 2 * a_f


        number = int(input("请输入要判断是否为雅各布斯塔尔数的数："))
        sequence = jacobsthal_number()
        result = [next(sequence) for i in range(number)]
        if number in result:
            print(f"{number}是第{result.index(number)}个雅各布斯塔尔数")
        else:
            print(f"{number}不是雅各布斯塔尔数")
    elif mode == 59:
        perrin_number_list, a, b, c = [3, 0, 2], 3, 0, 2
        number = int(input("请输入要列出到0到第几个佩兰数："))
        for _ in range(number - 2):
            a, b, c = b, c, a + b
            perrin_number_list.append(c)
        text = "、".join(str(i_7) for i_7 in perrin_number_list)
        total = np.sum(perrin_number_list)
        print(f"第0~{number}个佩兰数分别是{text}\n它们的和为{total}")
    elif mode == 60:
        perrin_number_list, a, b, c = [3, 0, 2], 3, 0, 2
        number = int(input("请输入判断是否为佩兰数的数："))
        for _ in range(number - 2):
            a, b, c = b, c, a + b
            perrin_number_list.append(c)
        if number in perrin_number_list:
            print(f"{number}是第{perrin_number_list.index(number)}个佩兰数")
        else:
            print(f"{number}不是佩兰数")
    elif mode == 61:
        schroder_number = [1, 1]
        number = int(input("请输入要列出0~第几个施罗德数："))
        for n in range(3, number + 2):
            schroder_number.append(
                int(gmpy2.divexact(schroder_number[-1] * (6 * n - 9) - (n - 3) * schroder_number[-2], n)))
        text = "、".join(str(i_7) for i_7 in schroder_number)
        total = np.sum(schroder_number)
        print(f"第0~{number}个施罗德数分别是{text}\n它们的和为{total}")
    elif mode == 62:
        schroder_number = [1, 1]
        number = int(input("请输入要列出0~第几个施罗德数："))
        cnt = 1
        n = 3
        while schroder_number[-1] < number:
            schroder_number.append(
                int(gmpy2.divexact(schroder_number[-1] * (6 * n - 9) - (n - 3) * schroder_number[-2], n)))
            cnt += 1
            n += 1
        if number == 1:
            print("1是第1个施罗德数")
        elif number < schroder_number[-1]:
            print(f"{number}不是施罗德数")
        elif number == schroder_number[-1]:
            print(f"{number}是第{cnt}个施罗德数")
        else:
            print("错误！")
    elif mode == 63:
        number = int(input("请输入要计算第几个梅森数："))
        mersenne_number = int(mp.power(2, number)) - 1
        print(f"第{number}个梅森数是{mersenne_number}")
    elif mode == 64:
        number = int(input("请输入要计算第几个梅森数："))
        flag = True
        a = sympy.factorint(number + 1)
        for key in a.keys():
            if key != 2:
                print(f"{number}不是梅森数")
                flag = False
                break
        if flag:
            print(f"{number}是梅森数")
    elif mode == 65:
        def generating_harmonic_number(startvalue=1):
            for n_h in itertools.count(max(startvalue, 1)):
                f_2 = sympy.factorint(n_h)
                s_a = math.prod((p_a ** (e_1 + 1) - 1) // (p_a - 1) for p_a, e_1 in f_2.items())
                if not functools.reduce(lambda x_f, y: x_f * y % s_a, (e_1 + 1 for e_1 in f_2.values()), 1) * n_h % s_a:
                    yield n_h


        number = int(input("请输入要计算1~第几个调和数"))
        harmonic_number = list(itertools.islice(generating_harmonic_number(), number))
        text = "、".join(str(i_7) for i_7 in harmonic_number)
        total = np.sum(harmonic_number)
        print(f"第1~{number}个调和数分别是{text}\n它们的和为{total}")
    elif mode == 66:
        def harmonic_number(n_h):
            return (n_h * sympy.divisor_sigma(n_h, 0)) % sympy.divisor_sigma(n_h, 1) == 0


        number = int(input("请输入要计算哪个数以内的调和数："))
        harmonic_number = [n for n in range(1, number + 1) if harmonic_number(n)]
        length = len(harmonic_number)
        text = "、".join(str(i_7) for i_7 in harmonic_number)
        total = np.sum(harmonic_number)
        print(f"{number}以内有{length}个调和数\n它们分别是{text}\n它们的和为{total}")
    if mode == 67:
        x = int(input("请输入一个整数："))
        x_8 = str(x)
        text = sympy.divisors(x)
        total = 0
        list4 = []
        for c in text:
            list4.append(int(c))
        print(list4)
        count = len(list4)
        for i_f in list4:
            total += Fraction(1, i_f)
        total_1 = count / total
        total_2 = count // total
        if total_1 == total_2:
            print(f"{x}是调和数")
        else:
            print(f"{x}不是调和数")
    elif mode == 68:
        summation = 0
        i = 1
        number_max = Decimal(input("请输入调和级数要超过哪个数："))
        while summation < number_max:
            summation += 1 / i
            i += 1
        print(f"当n = {i - 1}时，结果才能大于{number_max}")
    elif mode == 69:
        n = 0
        list_1 = []
        number_max = int(input("请输入n的值： "))
        for i in range(1, number_max):
            list_1.append(Fraction(1, i))
        summation = str(np.sum(list_1))
        p = int(summation.split("/", 1)[0])
        b = int(summation.split("/", 1)[1])
        a = p / b
        print(f"当n = {number_max}时，总和为{summation}，化为小数约是{a}")
    elif mode == 70:
        def kolakoski():
            x_e = y_a = -1
            while True:
                yield [2, 1][x_e & 1]
                f_2 = y_a & ~ (y_a + 1)
                x_e ^= f_2
                y_a = (y_a + 1) | (f_2 & (x_e >> 1))


        K = kolakoski()
        number = int(input("请输入要列出1~第几个科拉科斯基数："))
        kolakoski_sequence = [next(K) for _ in range(number)]
        text = "、".join(str(i_7) for i_7 in kolakoski_sequence)
        total = np.sum(kolakoski_sequence)
        print(f"第1~{number}个科拉科斯基数分别是{text}\n它们的和为{total}")
    elif mode == 71:
        number = int(input("请输入要计算第几个欧拉函数的值："))
        euler_totient_function = [totient(i) for i in range(1, number + 1)]
        text = "、".join(str(i_7) for i_7 in euler_totient_function)
        total = np.sum(euler_totient_function)
        print(f"第1~{number}个欧拉函数的值分别是{text}\n它们的和为{total}")
    elif mode == 72:
        sylvester_sequence = [2]
        number = int(input("请输入要计算0~第几个西尔维斯特数："))
        for n in range(1, number + 1):
            sylvester_sequence.append(sylvester_sequence[n - 1] * (sylvester_sequence[n - 1] - 1) + 1)
        text = "、".join(str(i_7) for i_7 in sylvester_sequence)
        total = np.sum(sylvester_sequence)
        print(f"第0~{number}个西尔维斯特数分别是{text}\n它们的和为{total}")
    elif mode == 73:
        def pell_number():
            a_g, b_g = 0, 1
            yield from [a_g, b_g]
            while True:
                a_g, b_g = b_g, a_g + 2 * b_g
                yield b_g


        number = int(input("请输入要计算0~第几个佩尔数："))
        pell_number_list = list(itertools.islice(pell_number(), number + 1))
        text = "、".join(str(i_7) for i_7 in pell_number_list)
        total = np.sum(pell_number_list)
        print(f"第0~{number}个佩尔数分别是{text}\n它们的和为{total}")
    elif mode == 74:
        def menage_number(c_2):
            if c_2 == 0:
                return 1
            else:
                return sum((-2 * c_2 if k1 & 1 else 2 * c_2) * comb(m1 := 2 * c_2 - k1, k1) *
                           factorial(c_2 - k1) // m1 for k1 in range(c_2 + 1))


        number = int(input("请输入要计算第几个梅纳日数："))
        print(f"第{number}个梅纳日数是{menage_number(number)}")
    elif mode == 75:
        def zag_number(n_j):
            return abs(((2 - (2 << (m_j := n_j << 1))) * sympy.bernoulli(m_j) << m_j - 2) // n_j)


        number = int(input("请输入要计算第几个扎格数："))
        print(f"第{number}个扎格数是{zag_number(number)}")
    elif mode == 76:
        def zag_number_list(n_k):
            t_3 = [1 for _ in range(1, n_k + 2)]
            t_3[1] = 1
            for k_5 in range(2, n_k + 1):
                t_3[k_5] = (k_5 - 1) * t_3[k_5 - 1]
            for k_5 in range(2, n_k + 1):
                for j_2 in range(k_5, n_k + 1):
                    t_3[j_2] = (j_2 - k_5) * t_3[j_2 - 1] + (j_2 - k_5 + 2) * t_3[j_2]
            return t_3


        number = int(input("请输入要计算1~第几个扎格数："))
        zag_numbers = zag_number_list(number)
        del zag_numbers[0]
        text = "、".join(str(i_7) for i_7 in zag_numbers)
        total = np.sum(zag_numbers)
        print(f"第1~{number}个扎格数分别是{text}\n它们的和为{total}")
    elif mode == 77:
        def lower_wythoff(n_n):
            return (n_n + math.isqrt(5 * n_n ** 2)) // 2


        number = int(input("请输入要计算第几个洛厄威佐夫数："))
        print(f"第{number}个洛厄威佐夫数是{lower_wythoff(number)}")
    elif mode == 78:
        def aupton(terms):
            alst, aset = [None, 1], {1}
            for n_l in range(1, terms):
                an = alst[n_l] + (1 if n_l not in aset else 2)
                alst.append(an)
                aset.add(an)
            return alst[1:]


        number = int(input("请输入要计算1~第几个洛厄威佐夫数："))
        lower_wythoff = aupton(number)
        text = "、".join(str(i_7) for i_7 in lower_wythoff)
        total = np.sum(lower_wythoff)
        print(f"第1~{number}个洛厄威佐夫数分别是{text}\n它们的和为{total}")
    elif mode == 79:
        def fermat_numbers(n_m):
            return 2 ** (2 ** n_m) + 1


        number = int(input("请输入要计算第几个费马数："))
        print(f"第{number}个费马数是{fermat_numbers(number)}")
    elif mode == 80:
        def fermat_numbers(n_m):
            return 2 ** (2 ** n_m) + 1


        number = int(input("请输入要计算0~第几个费马数："))
        fermat_numbers_list = [fermat_numbers(n) for n in range(number + 1)]
        text = "、".join(str(i_7) for i_7 in fermat_numbers_list)
        total = np.sum(fermat_numbers_list)
        print(f"第0~{number}个费马数分别是{text}\n它们的和为{total}")
    elif mode == 81:
        complementary_bell_numbers, blist, b = [1, -1], [1], -1
        number = int(input("请输入要计算0~第几个互补贝尔数："))
        for _ in range(number - 1):
            blist = list(itertools.accumulate([b] + blist))
            b = -blist[-1]
            complementary_bell_numbers.append(b)
        text = "、".join(str(i_7) for i_7 in complementary_bell_numbers)
        total = np.sum(complementary_bell_numbers)
        print(f"第0~{number}个互补贝尔数分别是{text}\n它们的和为{total}")
    elif mode == 82:
        def ramanujan_numbers(n_o):
            return n_o ** 4 * sigma(n_o) - 24 * \
                ((m_n := n_o + 1 >> 1) ** 2 *
                 (0 if n_o & 1 else (m_n * (35 * m_n - 52 * n_o) + 18 * n_o ** 2) * sigma(m_n) ** 2) +
                 sum((i_l * (i_l * (i_l * (70 *
                                           i_l - 140 * n_o) + 90 * n_o ** 2) - 20
                             * n_o ** 3)
                      + n_o ** 4) * sigma(i_l) * sigma(n_o - i_l)
                     for i_l in range(1, m_n)))


        number = int(input("请输入要计算第几个拉马努金数："))
        print(f"第{number}个拉马努金数是{ramanujan_numbers(number)}")
    time.sleep(10)
