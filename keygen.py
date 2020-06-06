import random

print("generating CD key...")

key_CD = random.choice(list(filter(lambda x: int(x) not in [333, 444, 555, 666, 777, 888, 999], [str(i).zfill(3) for i in range(1000)]))) + "-" + random.choice(list(filter(lambda x: (sum([int(i) for i in x]) % 7 == 0) and (int(x[-1]) not in [0, 8, 9]), [str(i).zfill(7) for i in range(10000000)])))

print("generating OEM key...")

key_OEM = str(random.randint(1, 366)).zfill(3) + str(random.randint(1995, 2003))[2:].zfill(2) + "-OEM-" + random.choice(list(filter(lambda x: (sum([int(i) for i in x]) % 7 == 0) and (int(x[-1]) not in [0, 8, 9]) and (int(x[0]) == 0), [str(i).zfill(7) for i in range(10000000)]))) + "-" + str(random.randint(0, 99999)).zfill(5)

print("\ndone!\n\nCD key: " + key_CD + "\nOEM key: " + key_OEM)
