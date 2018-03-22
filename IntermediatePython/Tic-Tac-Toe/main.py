#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 20:35:21 2018

"""

import random


def display_board(board):

    print("\n")
    print(" ", board[7], " | ", board[8], " | ", board[9])
    print("-----------------")
    print(" ", board[4], " | ", board[5], " | ", board[6])
    print("-----------------")
    print(" ", board[1], " | ", board[2], " | ", board[3])
    print("\n")

    return None


def player_input():

    player1 = ''
    player2 = ''

    while player1 == "":
        player1 = input("Please pick a marker 'X' or 'O': ")
        if player1 in ("X", "x"):
            player1 = "X"
            player2 = "O"
        elif player1 in ("O", "o"):
            player1 = "O"
            player2 = "X"
        else:
            player1 = ""

    print(f"Player 1 is {player1}'s and Player 2 is {player2}'s.")

    return player1, player2


def place_marker(board, marker, position):

    # board = ['#','','','','','','','','','']

    board.pop(position)
    board.insert(position, marker)

    return None


def win_check(board, mark):

    if set(mark) == (set([board[1], board[2], board[3]])):
        return True
    if set(mark) == (set([board[4], board[5], board[6]])):
        return True
    if set(mark) == (set([board[7], board[8], board[9]])):
        return True
    if set(mark) == (set([board[7], board[4], board[1]])):
        return True
    if set(mark) == (set([board[8], board[5], board[2]])):
        return True
    if set(mark) == (set([board[9], board[6], board[3]])):
        return True
    if set(mark) == (set([board[1], board[5], board[9]])):
        return True
    if set(mark) == (set([board[3], board[5], board[7]])):
        return True
    return False


def choose_first():
    if (random.randint(1, 2)) == 1:
        return "Player 1 will go first.", "1"
    else:
        return "Player 2 will go first.", "2"


def space_check(board, position):

    if board[position] == '':
        return True
    return False


def full_board_check(board):

    if '' in board:
        return False
    return True


def player_choice(board):

    position_open = False
    move = False
    position_error = True

    while not position_open:
        while not move:
            while position_error:
                position = int(input("Next player's move (1 through 9): "))
                if position in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    position_error = False
                if not position_error and space_check(board, position):
                    position_open = True
                    move = True
                else:
                    print("That position is taken - please try again!")
                    position_error = True
    return position


def replay():

    again_error = True

    while True:
        while again_error:
            again = input("Would you like to play again? ")
            if again in ["Yes", "yes", "y", "No", "no", "n"]:
                again_error = False
        if again in ["Yes", "yes", "y"]:
            return True
        return False


print('Welcome to Tic Tac Toe!')

# while True:
while True:

    board = ['#', '', '', '', '', '', '', '', '', '']
    display_board(board)
    game_on = True
    player1, player2 = player_input()
    first_name, first_num = (choose_first())
    if first_num == "1":
        first = True
    if first_num == "2":
        first = False
    second = True
    print(first_name)

    while game_on:
        # Player 1 Turn
        if first:
            position = player_choice(board)
            place_marker(board, player1, position)
            display_board(board)
            if win_check(board, player1):
                print(f"{player1}'s WIN!!!!")
                game_on = False
                second = False
        first = True
        if second:
            # Player2's turn.
            position = player_choice(board)
            place_marker(board, player2, position)
            display_board(board)
            if win_check(board, player2):
                print(f"{player2}'s WIN!!!!")
                game_on = False

    if not replay():
        print("That was fun - Let's play again soon!!!")
        break
