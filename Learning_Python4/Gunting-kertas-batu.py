pemain1 = input("Player 1 memilih :")
pemain2 = input("Player 2 memilih :")

pilihan1 = "batu"
pilihan2 = "gunting" 
pilihan3 = "kertas"

if pemain1 == pilihan1 and pemain2 == pilihan2:
  print(f"Player 1 menang")
elif pemain1 == pilihan2 and pemain2 == pilihan1:
  print(f"Player 2 menang")
elif pemain1 == pilihan1 and pemain2 == pilihan3:
  print(f"Player 2 menang")
elif pemain1 == pilihan3 and pemain2 == pilihan1:
  print(f"Player 1 menang")
elif pemain1 == pilihan2 and pemain2 == pilihan3:
  print(f"Player 1 menang")
elif pemain1 == pilihan3 and pemain2 == pilihan2:
  print(f"Player 2 menang")
else:
  print(f"Hasil seimbang")