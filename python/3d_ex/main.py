from math import exp

def korrel(x, y):
    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)
    cov = sum((i - mean_x) * (j - mean_y) for i, j in zip(x, y))
    nor = (sum((i - mean_x) ** 2 for i in x) * sum((j - mean_y) ** 2 for j in y)) ** 0.5

    return cov / nor

def aprox(x, y):
    n = len(x)
    xy_sum = sum(i * j for i, j in zip(x, y))
    x_sum = sum(x)
    y_sum = sum(y)
    x_sqr_sum = sum(i ** 2 for i in x)
    
    a = (n * xy_sum - x_sum * y_sum) / (n * x_sqr_sum - x_sum ** 2)
    b = (y_sum - a * x_sum) / n
    return a, b

def cofe(T, Ts, r, time):
    temperatures = []
    for i in range(time + 1):
        temperatures.append(Ts + (T - Ts) * exp(-r * i))
    return temperatures

if __name__ == "__main__":
    T = 90
    Ts = 26
    r_val = 0.01
    time = 60

    temperatures = cofe(T, Ts, r_val, time)
    times = [i for i in range(time + 1)]
    a, b = aprox(times, temperatures)
    r = korrel(times, temperatures)

    print(f"The angular coefficient of the approximating line a: {a}")
    print(f"Displacement coefficient b: {b}")
    print(f"Correlation coefficient r: {r}")

    for i, j in zip(times, temperatures):
        print(f"Time - {i}c: temperature - {j} C")
