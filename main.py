# Trevor Loth
# 2025-1-28

import random
import time
import sys
from calcHand import calc_hand  # hand value calc function
from cardInfo import deck       # deck dictionary

NEW_DECK = ['CA', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C1', 'CJ', 'CQ', 'CK',
            'DA', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D1', 'DJ', 'DQ', 'DK',
            'HA', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H1', 'HJ', 'HQ', 'HK',
            'SA', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S1', 'SJ', 'SQ', 'SK']

def hit(hand, d, rt):
    card = d.pop()
    hand.append(card)
    count_card(rt, card)
    result = calc_hand(hand)
    return len(result) > 0

def bet(players, index):
    bet = 0
    valid = False
    while not valid:
        try:
            bet = int(input(f"\033[32mPlease enter a positive integer between 1 and {players[index][0]}.\033[0m\n"))
            if bet > players[index][0] or bet <= 0:
                ValueError
            else:
                players[index][1] = bet
                players[index][0] -= bet
                print(f"Player {index+1} has {player_chips[index][0]} chips remaining.")
                valid = True
        except ValueError:
            bet = 0
            print("Not enought chips for bet. You have", players[index][0], "chips available to bet.")
        except:
            bet = 0
            print("Invalid input. Please give a positive integer value.")

    return True

def reshuffle(d, p_hands, d_hand):
    # Reshuffle deck excluding in-play cards
    if len(d) < 2* (len(p_hands) + 1): # 2 cards per player + 1 for the dealer hand
        print("\033[33mShuffling remaining cards.\033[0m")
        d = NEW_DECK[:]
        random.shuffle(d)
        for i in p_hands:
            for j in i:
                d.remove(j)
        for i in d_hand:
            d.remove(i)
    return d

def count_card(rt, card):
    if "2" in card or "3" in card or "4" in card or "5" in card or "6" in card:
        rt[0] += 1
    elif "A" in card or "K" in card or "Q" in card or "J" in card or "1" in card:
        rt[0] -= 1
    return rt


if __name__ == "__main__":
    print(
    "\033[34m==============================\n" + 
    "Welcome to Blackjack!\nThis is Version 1.2\n" + 
    "------------------------------" + 
    "\nWhats New?\n" +
    "- Added color for visual clarity\n" + 
    "- Fixed a clarity bug where dealer's new card was misidentified, even though the math and value were correct." +
    "- Added a card counting toggle option." +
    "------------------------------\n" + 
    "Contacts \"steraks\" on discord for queries\n" + 
    "==============================\n\033[0m"
    )
    
    print(
        "⢠⣾⡿⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆\n" +
        "⣿⠃⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀\n" +
        "⣷⣀⢀⠀⣀⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀\n" +
        "⣿⣿⣏⣀⣘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀\n" +
        "⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀\n" +
        "⣿⣿⣿⣿⣿⣿⣿⡟⣼⣆⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀\n" +
        "⣿⣿⣿⣿⣿⣿⡿⣰⣿⣿⡄⠘⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀\n" +
        "⣿⣿⣿⣿⣿⣿⢡⣭⣭⣭⣭⡀⠸⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀\n" +
        "⣿⣿⣿⣿⠿⠋⠸⢿⣿⣿⡿⠷⠀⠹⢿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀\n" +
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡍⠉⣹⣿⣿⠀⠀⠀⠀⠀\n" +
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠉⠉⠀⠁⠉⢿⠀⠀⠀⠀⠀\n" +
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⢠⣿⠀⠀⠀⠀⠀\n" +
        "⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣾⡿⠏⠀⠀⠀⠀⠀\n\n"
    )


    # New Game
    while True:
        playing_deck = NEW_DECK[:]
        random.shuffle(playing_deck)
        num_of_players = 0
        running_total = [0]
        show_count = None

        # Get desired number of players
        while num_of_players < 1 or num_of_players > 8:
            try:
                num_of_players = int(input("\033[32mEnter number of players between 1 and 8.\033[0m\n"))
                if num_of_players < 1 or num_of_players > 8:
                    ValueError
                else:
                    break

            except:
                print("Invalid number of players! Try again.")
        
        # Get player pref to see card count
        while show_count == None:
            try:
                tmp = input("\033[32mWould you like to see the card count? Y/N?\033[0m\n")
                if tmp.upper() == "Y":
                    show_count = True
                    break
                elif tmp.upper() == "N":
                    show_count = False
                    break
                else:
                    ValueError
            except:
                print("Don't be a rat.", end="")
        
        player_chips = [[30, 0] for x in range(num_of_players)] # [total chips, active bet] if None, player is out

        print("==============================\nNew Game Starting...\n------------------------------")
        print("The game ends when all players chips reach 0,\nor when at least one player reaches atleast 100 chips.\n==============================")
        
        while True:
            player_hands = [[] for x in range(num_of_players)]
            player_hands_bust = [False for x in range(num_of_players)]
            dealer_hand = []

            player_turn = True

            playing_deck = reshuffle(playing_deck, player_hands, dealer_hand)

            # Place bets before cards are dealth
            for num in range(num_of_players):
                if player_chips[num] == None:
                    continue
                print(f"Player {num+1}, what bet would you like to place?")
                bet(player_chips, num)

            # Deal Hands - Each card is dealt to each player then the dealer
            for i in range(2):
                for j in range(len(player_hands)):
                    if player_chips[j] == None:
                        continue
                    player_hands[j].append(playing_deck.pop())
                dealer_hand.append(playing_deck.pop())
            
            # count player cards
            for num in range(len(player_hands)):
                for j in range(len(player_hands[num])):
                    card = player_hands[num][j]
                    count_card(running_total, card)
            # count dealer 1st card
            count_card(running_total, dealer_hand[0])

            d_calc = calc_hand(dealer_hand)

            playing_deck = reshuffle(playing_deck, player_hands, dealer_hand)

            # player turn
            for num in range(len(player_hands)):
                player_turn = True

                if player_chips[num] == None:
                    continue

                # Show dealer hand
                print("==============================")
                if dealer_hand[0][1] == "A":
                    print(f"Dealer has {deck[dealer_hand[0]]} and a hidden card. " +
                    f"\n\033[36mMin Value: 12\033[0m, " +
                    f"\n\033[36mMax Value: 21\033[0m\n------------------------------")
                else:
                    tmp = calc_hand([dealer_hand[0]])[0]
                    print(f"Dealer has {deck[dealer_hand[0]]} and a hidden card. " +
                        f"\n\033[36mMin hand value: {tmp + 2} \033[0m" +
                        f"\n\033[36mMax hand value: {tmp + 11}\033[0m\n------------------------------")

                while player_turn:
                    try:
                        # Show Player Hand
                        print(f"Player number {num+1} hand is ", end="")
                        for i in range(len(player_hands[num])-1):
                            print(deck[player_hands[num][i]], end=", ")
                        print(f"{deck[player_hands[num][-1]]}. \033[36mValue: ", end="")

                        # Check current hand values
                        hand_vals = calc_hand(player_hands[num])
                        print(hand_vals[0], end="\033[0m")
                        if len(hand_vals) > 1:
                            for i in range(1, len(hand_vals)):
                                print(" or\033[36m", hand_vals[i], end="\033[0m")
                            print(".")
                        print()
                        
                        if show_count:
                            print("\033[36mRunning total:", running_total[0], "\033[0m")

                        if max(hand_vals) == 21:
                            print("Player", num+1, "got Blackjack!")
                            player_turn = False
                            time.sleep(0.5)
                            break

                        time.sleep(0.5)
                        user_input = int(input("\033[32mHit or Stand? 1 for Hit, 2 for Stand, 3 to exit...\033[0m\n"))

                        if user_input == 1:
                            print("Player", num+1, "hit.")
                            
                            hit_res = hit(player_hands[num], playing_deck, running_total)

                            print(f"Player number {num+1} drew a {deck[player_hands[num][-1]]}. New \033[36mvalue: ", end="")
                            p_hand = calc_hand(player_hands[num])
                            print(str(max(p_hand)) + "\033[0m" if hit_res else "BUST!\033[0m")
                            
                            time.sleep(0.5)
                            if not hit_res:
                                print("You lost this hand.")
                                player_hands_bust[num] = True
                                player_turn = False
                            else:
                                if max(p_hand) == 21:
                                    print(f"Player {num+1} got a 21!\nPlayer {num+1} stands.")
                                    player_turn = False
                                    break
                            print("------------------------------")
                        elif user_input == 2:
                            print("Player", num+1, "stands.")
                            player_turn = False
                        elif user_input == 3:
                            print("Exit")
                            sys.exit()
                        else:
                            ValueError()

                    except SystemExit:
                        sys.exit()
                    except:
                        print("==============================\nInvalid command. Please try again.\n==============================")

            # Dealer Turn
            print("==============================\nDealer Turn\n==============================")
            # Stand on 17 or higher: The dealer must always stand when their hand value reaches 17 or more.
            # Hit on 16 or less: If the dealer's hand totals 16 or less, they must take another card (hit).
            # No choice to "beat" players: The dealer's actions are dictated by the rules, not by the goal of beating each player at the table.
            
            # count dealer 2nd card which was not counted originially
            count_card(running_total, dealer_hand[1])

            while True:
                time.sleep(0.5)
                dealer_stand = False

                # Show dealer Hand
                print(f"Dealer hand is ", end="")
                for i in range(len(dealer_hand)-1):
                    print(deck[dealer_hand[i]], end=", ")
                print(f"{deck[dealer_hand[-1]]}.\033[36m Value: ", end="")
                print(d_calc[0], end="\033[0m")
                if len(d_calc) > 1:
                    for i in range(1, len(d_calc)):
                        print(" or\033[36m", d_calc[i], end="\033[0m")
                    print(".")
                print()
                
                if show_count:
                    print("\033[36mRunning total:", running_total[0], "\033[0m")

                time.sleep(0.5)
                if max(d_calc) >= 17:
                    dealer_stand = True

                if not dealer_stand:
                    print("Dealer must hit!")
                    time.sleep(0.5)
                    hit_res = hit(dealer_hand, playing_deck, running_total)
                    time.sleep(0.5)
                    # Show dealer's draw
                    print(f"Dealer drew a {deck[dealer_hand[-1]]}. New\033[36m value: ", end="")
                    d_calc = calc_hand(dealer_hand)
                    print(str(max(d_calc)) + "\033[0m" if hit_res else "BUST!\033[0m") # Print the new Value

                    if not hit_res:
                        print("Dealer Bust! Standing players win!")
                        for num in range(len(player_hands_bust)):
                            if player_chips[num] == None:
                                continue

                            if not player_hands_bust[num]:
                                # payout to players
                                player_chips[num][0] += player_chips[num][1]*2
                        
                        if show_count:
                            print("\033[36mRunning total:", running_total[0], "\033[0m")
                        break
                else:
                    d_max = max(d_calc) # Print the value
                    for num in range(len(player_hands)):
                        if player_chips[num] == None:
                            continue

                        time.sleep(0.5)
                        p_max = 0
                        if not player_hands_bust[num]:
                            p_max = max(calc_hand(player_hands[num]))
                        if p_max > d_max:
                            print(f"\033[33mPlayer {num+1} beat the Dealer!\033[0m")
                            player_chips[num][0] += player_chips[num][1]*2
                        elif p_max < d_max:
                            print(f"\033[33mDealer wins against Player {num+1}.\033[0m")
                        else:
                            print(f"\033[33mPlayer {num + 1} Dealer push, no winner.\033[0m")
                            player_chips[num][0] += player_chips[num][1]
                    break


            # Game end conditions checks
            # Reset bets
            print("\n==============================")
            winners = []
            active_players = False
            for num in range(len(player_chips)):
                if player_chips[num] == None:
                    continue
                player_chips[num][1] = 0
                if player_chips[num][0] <= 0:
                    player_chips[num] = None
                    print(f"\033[33mPlayer {num+1} is now out!\033[0m")
                    time.sleep(0.5)
                    continue
                active_players = True
                if player_chips[num][0] >= 100:
                    winners.append(num)

            print("------------------------------")
            
            if len(winners) > 0:
                for i in winners:
                    time.sleep(0.5)
                    print(F"\033[35mPlayer {i+1} won with {player_chips[i][0]} chips!\033[0m")
                a = input("\033[32mPlay again? Y/N?\033[0m\n")
                if a.upper() == "Y":
                    break
                sys.exit()
            
            if not active_players:
                print("\033[33mAll players ran out of chips. The house wins!\033[0m")
                a = input("\033[32mPlay again? Y/N?\033[0m\n")
                if a.upper() == "Y":
                    break
                sys.exit()
