import time


print("\n\nWrite \"Hello my name is name\"")

for i in range(3):
    print(i+1)
    time.sleep(1)

dtime1 = time.time()
input("START:\t")
dtime2 = time.time()

sonuc = str(float(dtime2)-float(dtime1))
print("Time : " + sonuc + " sec")

if float(sonuc) < 2:
    print("Wow! Very fast!")
elif float(sonuc) < 4:
    print("Not bad!")
else:
    print("Too slow!")

input()
