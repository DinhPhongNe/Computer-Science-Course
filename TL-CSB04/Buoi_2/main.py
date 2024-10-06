import time
a = []
b = [1207, 2802, 2904, 2405, 1305, 2702, 1010, 2309]


a.append("Trinh")
a.append("An")
a.append("Linh")
a.insert(0, "Uyen")
a.append("Huy")
a.remove("Huy")
a.pop()
a.clear()

(len(a) - 1)//2


b.sort()

for a in a:
    print(a, end=" ")
    
print("")
    
for b in b:
    print(b, end=" ")

with open("grade.txt", "a") as file:
    file.write("10")

