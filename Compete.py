#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'play2248' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING boardValues
#  2. STRING pathValues
#
def play2248(boardValues, pathValues):
    # Function to calculate the sum of the path values
    def calculate_path_sum(path):
        return sum(path)

    # Function to find the smallest power of 2 greater than or equal to a number
    def next_power_of_2(number):
        power = 1
        while power < number:
            power *= 2
        return power

    # Function to update the board after tile removal
    def update_board(board):
        for col in range(5):
            new_col = [board[row][col] for row in range(8) if board[row][col] != 0]
            for row in range(8 - len(new_col)):
                new_col.insert(0, 0)
            for row in range(8):
                board[row][col] = new_col[row]

    # Function to add new tiles to the board
    def add_new_tiles(board):
        power = 256
        for row in range(8):
            for col in range(5):
                if board[row][col] == 0:
                    board[row][col] = power
                    power //= 2
                    if power == 1:
                        power = 256

    # Convert boardValues and pathValues to integers
    board_values = list(map(int, boardValues.split()))
    path_values = list(map(int, pathValues.split()))

    # Initialize the board
    board = [[board_values[i * 5 + j] for j in range(5)] for i in range(8)]

    # Calculate path sum
    path_sum = calculate_path_sum(path_values)

    # Find the next power of 2
    replacement = next_power_of_2(path_sum)

    # Replace tiles
    last_tile_index = path_values[-1]
    row = last_tile_index // 10 - 1
    col = last_tile_index % 10 - 1
    if row < len(board) and col < len(board[0]):
        board[row][col] = replacement

    # Remove tiles
    for tile_index in path_values[:-1]:
        row = tile_index // 10 - 1
        col = tile_index % 10 - 1
        if row < len(board) and col < len(board[0]):
            board[row][col] = 0

    # Update the board
    update_board(board)

    # Add new tiles
    add_new_tiles(board)

    # Convert the final board to a single string
    final_board = [str(tile) for row in board for tile in row]
    result = ' '.join(final_board)

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    boardValues = input()

    pathValues = input()

    result = play2248(boardValues, pathValues)

    fptr.write(result + '\n')

    fptr.close()
