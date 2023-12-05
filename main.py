def main():
    try:
        with open("bakiye.txt", "r") as file:
            balance = float(file.read())
    except FileNotFoundError:
        balance = 0

    while True:
        print("\nOnline ATM'ye Hos geldiniz")
        print("1. Bakiye Sorgulama")
        print("2. Para Çek")
        print("3. Para Yatır")
        print("4. Çıkış Yap")
        choice = input("Lütfen bir seçim yapınız: ")

        if not choice.isdigit():
            print("Hata.Sayı Girmeniz Gerekmektedir.")
            continue

        choice = int(choice)

        if choice == 1:
            print(f"Güncel Bakiyeniz: {balance:.2f}₺")
        elif choice == 2:
            withdrawal = float(input("Cekmek istediginiz tutari girin: "))
            if withdrawal > balance:
                print("Yetersiz Bakiye!")
            else:
                balance -= withdrawal
                print(f"{withdrawal:.2f}₺ Cekildi")
                print(f"Güncel Bakiyeniz: {balance:.2f}₺")
        elif choice == 3:
            deposit = float(input("Lütfen yatırmak istediğiniz tutarı giriniz: "))
            balance += deposit
            print(f"{deposit:.2f}₺ Yatirildi")
            print(f"Güncel Bakiyeniz: {balance:.2f}₺")
        elif choice == 4:
            print("ATM'yi kullandığız için teşekkürler.")
            break
        else:
            print("Hatalı tuşlama yaptınız.")

    with open("bakiye.txt", "w") as file:
        file.write(str(balance))


if __name__ == "__main__":
    main()
