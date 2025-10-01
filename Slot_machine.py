# Python Slot Machine
# win+;
import random

def spin_row():
    symbols = ["🍒","🍉","🍋","🔔","🌟"]

  # """ results = []
  #    for symbols in range(3):
  #          results.append(random.choice(symbols))
  #        return results"""

    return [random.choice(symbols) for _ in range(3)]
    



def print_row(row):
    print("***********")
    print(" | ".join(row))
    print("***********")

def get_payout(row , bet):
    if row [0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🍋":
            return bet *5
        elif row[0] == "🔔":
            return bet *6
        elif row[0] == "🌟":
            return bet * 10
    return 0
    

def main():
    balance = 100


    print("************************")
    print(" Welcome to Python Slots")
    print("Symbols:🍒 🍉 🍋 🔔 🌟")
    print("************************")

    while balance > 0:
        print(f"Current balance : ${balance}")

        bet = input("place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number")
            continue


        bet = int(bet)

        if bet > balance:
            print("Insufficient fund")
            continue

        if bet <=0 :
            print("bet must be greater than 0")
            continue

        balance -= bet
        
        row = spin_row()
        print("Spinning....\n")
        print_row(row)
        

        payout = get_payout(row , bet)

        if payout > 0:
            print(f"you won ${payout}")
        else:
            print("Sorry you lost this round")

        balance += payout

        play_again = input("Do you want to spin again? (y/n): ").lower()

        if play_again != "y":
            break
    print("*******************************************")
    print(f"Game over your final balance is ${balance}")
    print("*******************************************")

if __name__=="__main__":
    main()
