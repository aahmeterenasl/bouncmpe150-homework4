

question = int(input())


def power(b, e):
    # DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    if e == 0:
        return 1
    return b * power(b,e-1)



    # DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE


def sum_digits(n):
    # DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

    n = str(n)
    if len(n) == 1:
        return int(n)
    if n[0] == "-":
        n=n[1:]
        return -1 * (int(n[0]) +sum_digits(n[1:]))
    return int(n[0]) +sum_digits(n[1:])


    # DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE


def g(n):
    # DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    if n <= 1:
        return  0
    elif n%2 == 0:
        return n/2 + g(n/2)
    elif n%2 == 1:
        return (n-1)/2 + g((n-1)/2)


    # DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE


def h(n):
    # DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    if n <= 1:
        return  n
    elif n%2 == 0:
        return h(n/2)
    elif n%2 == 1:
        return h((n-1)/2) + h((n+1)/2)


    # DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE


def ack(m, n):
    # DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return ack(m-1,1)
    elif m > 0 and n > 0:
        return ack(m-1,ack(m,n-1))



    # DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE


def candy(c):
    # DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

    if c < 3:
        return 1
    return candy(c-3) + candy(c-1)
    # DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE


def expr(n, x):
    # DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    if x == n:
        return x + (1/(x+1))

    return x + (1/(expr(n,x+2)))
    # DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE


def is_reverse(str1, str2):
    # DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    if len(str1) != len(str2):
        return False
    elif len(str1) <= 1:
        return True
    if str1[0].lower() == str2[-1].lower():
        return is_reverse(str1[1:],str2[:-1])
    else:
        return False
    # DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE


def count_binary(n, i=0, b_str=""):
    # DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    if n == 0:
        return b_str
    elif n == 1:
        return "0\n1\n"

    for el in count_binary(n-1).split("\n")[:-1]:
        b_str += "0" + el + "\n"
    for el in count_binary(n-1).split("\n")[:-1]:
        b_str += "1" + el + "\n"

    return b_str

    # DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE


def comb(container, r, temp_container):
    # DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    if r == 0:
        return ""
    res_str = ""
    lst = sorted(container)
    if r == 1:
        for el in lst:
            res_str += el + "\n"
        return res_str.strip()
    for i in range(len(lst)-r+1):
        for com in comb(lst[i+1:],r-1,[]).strip().split("\n"):
            res_str += lst[i] + com + "\n"
    return res_str.strip()
    # DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE


# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
'''
if question == 1:
    b = float(input())
    e = int(input())
    print("{:.4f}".format(power(b,e)))

elif question == 2:
    digits = int(input())
    print(sum_digits(digits))

elif question == 3:
    arg3 = int(input())
    print(int(g(arg3)))

elif question == 4:
    arg4 = int(input())
    print(int(h(arg4)))

elif question == 5:
    arg5_m = int(input())
    arg5_n = int(input())
    print(int(ack(arg5_m,arg5_n)))

elif question == 6:
    arg6 = int(input())
    print(int(candy(arg6)))

elif question == 7:
    arg7 = int(input())
    print("{:.6f}".format(expr(arg7,1)))

elif question == 8:
    arg8_1 = input()
    arg8_2 = input()
    print(is_reverse(arg8_1,arg8_2))

elif question == 9:
    arg9 = int(input())
    print(count_binary(arg9)[:-1])

elif question == 10:
    arg10_1 = int(input())
    arg10_2 = input()
    print(comb(arg10_2,arg10_1,[]))
'''
x = 10
b = "zero" if x==0 else "non-zero"
print(b)
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

