def f(x):
    return x**2 

def trapezoidal_integration(a, b, n):
    #начало алгоритма
    S = 0.0
    h = (b - a) / n
    x = a + h
    
    #цикл пока x < b
    while x < b:
        F = f(x)
        S = S + F
        x = x + h
    
    #вычисляем
    Fa = f(a)
    Fb = f(b)
    
    #итоговая формула
    S = (h / 2) * (Fa + Fb + 2 * S)
    
    return S

#пример
if __name__ == "__main__":
    a = 0
    b = 2
    n = 100
    
    #вызываем алгоритм
    result = trapezoidal_integration(a, b, n)
    
    print(f"S = {result}")
