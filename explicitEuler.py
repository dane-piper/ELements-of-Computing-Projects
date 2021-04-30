from cmath import exp


def main():
    delt = 0.0001
    x = 0.01
    y = x * exp(-x)
    z = 0
    while z <= 10:
        x1 = x + -2 * ((exp(-2 * x) / x) - 1.326) * 0.01 * 0.0001
        x = x1
        z += delt
    print(x)
    print('wtf')
main()
