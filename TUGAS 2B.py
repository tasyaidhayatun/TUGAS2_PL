def ganjil_genap():
    numbers = []
    while True:
        number = int(input("Masukkan nilai (0 untuk berhenti): "))
        if number == 0:
            break
        numbers.append(number)

    print("Nilai-nilai yang dimasukkan:", numbers)

    ganjil_values = [num for num in numbers if num % 2 != 0]
    print("Nilai-nilai ganjil:", ganjil_values)

    print("Nilai kuadrat dari nilai-nilai ganjil:")
    for num in ganjil_values:
        print(f"{num} ^ 2 = {num**2}")

ganjil_genap()
