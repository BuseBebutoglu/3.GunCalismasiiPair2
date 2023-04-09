# 1. Bölüm: Fibonacci sayı dizisi oluşturma
fibonacciSeri = [1, 1]  
a= int(input("Bir değer giriniz: ")) 
while len(fibonacciSeri) < a:  
    sıradakiSayi = fibonacciSeri[-1] + fibonacciSeri[-2]  
    fibonacciSeri.append(sıradakiSayi)  
print("Fibonacci:",fibonacciSeri)


# 2. Bölüm: Mükemmel sayıyı gösterme

sayi = int(input("Bir sayı giriniz: "))  
bolenler = []  

for i in range(1, sayi):  
    if sayi % i == 0:  
        bolenler.append(i)  

if sum(bolenler) == sayi:  
    print(sayi, "mükemmel bir sayıdır.")
else:
    print(sayi, "mükemmel bir sayı değildir.")