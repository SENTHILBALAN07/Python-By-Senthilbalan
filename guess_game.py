scecrete_number=8
guess_count=1
guess_numbers=4
while guess_count<guess_numbers:
    guess=int(input(f"guess { guess_count}= "))
    if guess==scecrete_number:
        print("You won!!!")
        break
    guess_count+=1

