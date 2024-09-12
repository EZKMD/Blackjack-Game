import random as r
from colorama import Fore

print("Welcome to blackjack!")
cash = int(input("How much do you want to play with?"))

while cash > 0:
    try:
        bet = int(input("How much would you like to bet on this game?"))
        cash -= bet
        dealer_count = r.randrange(17, 24)
        player_count = 0
        player_bust = False

        choice = input("Would you like to draw a card? (Yes/No): ")
        if choice.upper() == "NO":
            quit()
        else:
            draw = True

        while draw == True:
            card_picker = r.randrange(0, 4)
            cards = ["Spades", "Clubs", "Diamonds", "Hearts"]
            suit_choice = cards[card_picker]
            Number_Val = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "X", "J", "Q", "K"]
            pick = r.randrange(1, 14)
            card_num = Number_Val[pick - 1]
            if card_num in ["X", "J", "Q", "K"]:
                value = 10
            elif card_num == "A":
                value = 1
            else:
                value = int(card_num)

            suit = suit_choice
            num = card_num

            if suit.lower() == "spades":
                suit_upper = f"│ {Fore.BLACK}{num}{Fore.WHITE}         │"
                suit_lower = f"│         {Fore.BLACK}{num}{Fore.WHITE} │"
                suits_centre = f"│     {Fore.BLACK}{chr(9824)}{Fore.WHITE}     │"
                colour = 3

            elif suit.lower() == "clubs":
                suit_upper = f"│ {Fore.BLACK}{num}{Fore.WHITE}         │"
                suit_lower = f"│         {Fore.BLACK}{num}{Fore.WHITE} │"
                suits_centre = f"│     {Fore.BLACK}{chr(9827)}{Fore.WHITE}     │"
                colour = 3

            elif suit.lower() == "hearts":
                suit_upper = f"│ {Fore.RED}{num}{Fore.WHITE}         │"
                suit_lower = f"│         {Fore.RED}{num}{Fore.WHITE} │"
                suits_centre = f"│     {Fore.RED}{chr(9829)}{Fore.WHITE}     │"
                colour = 3

            elif suit.lower() == "diamonds":
                suit_upper = f"│ {Fore.RED}{num}{Fore.WHITE}         │"
                suit_lower = f"│         {Fore.RED}{num}{Fore.WHITE} │"
                suits_centre = f"│     {Fore.RED}{chr(9830)}{Fore.WHITE}     │"
                colour = 3

            print(f"""
                        ┌───────────┐
                        {suit_upper}
                        │           │
                        │           │
                        {suits_centre}    
                        │           │
                        │           │
                        {suit_lower}
                        └───────────┘
                    """)

            player_count += value
            if player_count > 21:
                print("You have gone bust ")
                print(f"Player:{player_count}")
                draw = False
                player_bust = True
                break
            print(f"Count: {player_count}")
            choice = input("Again? (Yes/No): ")
            if choice.upper() == "NO":
                draw = False

        while player_bust != True:
            if dealer_count <= 21:
                if player_count < dealer_count:
                    print(f"You lose! \nDealer:{dealer_count} \nPlayer:{player_count}")
                    break
                else:
                    print(f"You win! \nDealer:{dealer_count} \nPlayer:{player_count}")
                    cash = cash + bet + (bet * 2)
                    break
            else:
                print(f"The dealer went bust so you win! \nDealer:{dealer_count} \nPlayer:{player_count}")
                cash = cash + bet + (bet * 2)
                break

        print(f"Your new total is: ${cash}")

    except ValueError:
        print("Error: Invalid input! Please enter a valid number.")
    except KeyboardInterrupt:
        print("\nProgram ended by user.")
        break
    except Exception as e:
        print("An error occurred:", e)

print("GAME OVER")
