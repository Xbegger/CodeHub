import math



def read(str):
    inStr = input(str)
    ans = inStr.split(",")
    if(len(ans) == 1):
        ans = ans[0]
    return ans
# max_x_power = input("请输入函数的最高次数")
# cofficient = input()
# a, b = input("请输入初始搜索区间")

    # fx = ""
    # ans = 0
    # for i in range(0, len(cofficient)):
    #     if cofficient[i] > 0:
    #         if(i == len(cofficient) - 1):
    #             tmp = str(cofficient[i])
    #         else:
    #             tmp = "+" + str(cofficient[i])
    #     else:
    #         tmp = str(cofficient[i])
    #     if(i != 0):
    #         fx = tmp + "x^" + str(i) + fx
    #     else:
    #         fx = tmp + fx
    #     ans = ans + cofficient[i] * math.pow(x, i)
    # print("计算函数" + fx)



def dealCofficinet(cofficient):
    cofficient.reverse()
    ans = list()
    for value in cofficient:
        ans.append(float(value))
    return ans


def gold( a, b, delta, epsilon = 0.00001):
    T = (math.sqrt(5) - 1) / 2
    phi_a = f(a)
    phi_b = f(b)
    p = a + (1 - T) * (b - a)
    q = a + T * (b - a)
    phi_p = f( p)
    phi_q = f( q)
    iter_count = 1
    G = list()
    while((b - a) > delta or abs(phi_a - phi_b) > epsilon):
        iter_count = iter_count + 1
        print("iter_count:", iter)
        if(phi_p <= phi_q):
            b = q
            phi_b = phi_q
            phi_q = phi_p
            q = p
            p = a + (1 - T) * (b - a)
            phi_p = f( p)
        else:
            a = p
            phi_a = phi_p
            phi_p = phi_q
            p = q
            q = a + T * (b - a)
            phi_q = f( q)
        G.append([a, p, q, b])
    ds = abs(b-a)
    dphi = abs(phi_b - phi_a)
    if(phi_p < phi_q):
        s = p
        phi_s = phi_p
    else:
        s = q
        phi_s = phi_q
    
    return [s, phi_s, iter_count, G, [ds, dphi] ]

def f( x):
    # ans = math.pow(x, 2) - math.sin(x)
    # ans = math.pow(x, 2) - x - 1
    ans = math.pow(x, 3) - 2 * x + 1
    return ans
# max_x_power = int(read("请输入x的最高次数:"))
# cofficient = read("请输入x的系数与常数(按次数从高到低):")
# cofficient = dealCofficinet(cofficient)
# if(len(cofficient) != max_x_power + 1):
#     raise "系数数量与次数不匹配"
# print(cofficient)
# print(f(cofficient, 0.5))
# a, b = read("请输入初始搜索区间:")
# epsilon = read("请输入容许误差:")


# ans = gold(0, 1, 0.0001)
# ans = gold( -1, 1, 0.05 )
ans = gold(0, 3, 0.15)

s, phi_s, iter_count, G, E = ans
print(ans)

print(E)
