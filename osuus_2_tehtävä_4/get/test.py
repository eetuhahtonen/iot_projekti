from thingspeak import get_all, get_last

for row in get_all():
    print(row)


A = get_last()
if A:
    for row in A:
        print(row)
else:
    print("ID läpi.")
