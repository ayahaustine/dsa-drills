import pygame
from random import randint

# Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WIDTH, HEIGHT = 800, 600
SQUARESIZE = int((WIDTH / 8))
BORDER = 4

def initialize_board():
    board = [[0 for _ in range(8)] for _ in range(8)]
    pieces_pos = []

    for row in range(8):
        for col in range(8):
            if row in (0, 7):
                if (col % 2) == 0:
                    board[row][col] = 1 if row == 0 else 2
                    pieces_pos.append((row, col))
            elif row in (1, 6):
                if (col % 2) != 0:
                    board[row][col] = 2 if row == 1 else 1
                    pieces_pos.append((row, col))
            else:
                board[row][col] = 0
    
    return board, pieces_pos

def draw_board(screen, board):
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(
                screen,
                color,
                (col * SQUARESIZE, row * SQUARESIZE, SQUARESIZE - BORDER, SQUARESIZE - BORDER)
            )

def draw_pieces(screen, board, pieces_pos):
    for pos in pieces_pos:
        row, col = pos
        color = RED if board[row][col] == 1 else GREEN if board[row][col] == 2 else WHITE
        pygame.draw.circle(
            screen,
            color,
            (int(col * SQUARESIZE + SQUARESIZE // 2), int(row * SQUARESIZE + SQUARESIZE // 2)),
            int(SQUARESIZE // 2 - BORDER // 2)
        )

def is_valid_move(board, start_row, start_col, end_row, end_col, piece):
    if piece == 1:  # Black piece
        if start_row - end_row == 1 and start_col - end_col == 1:  # Up left move
            if board[end_row][end_col] == 2:  # If there is an opposite piece
                if (end_row, end_col) in pieces_pos:  # If the opposite piece is in the right position to be jumped
                    if (start_row - 2, start_col - 2) not in pieces_pos or board[start_row - 2][start_col - 2] != 0:  # Check for pieces in between
                        return False
                return True
        if start_row - end_row == 1 and start_col + end_col == 1:  # Up right move
            if board[end_row][end_col] == 2:  # If there is an opposite piece
                if (end_row, end_col) in pieces_pos:  # If the opposite piece is in the right position to be jumped
                    if (start_row - 2, start_col + 2) not in pieces_pos or board[start_row - 2][start_col + 2] != 0:  # Check for pieces in between
                        return False
                return True

    if piece == 2:  # White piece
        if start_row + end_row == 1 and start_col - end_col == 1:  # Down left move
            if board[end_row][end_col] == 1:  # If there is an opposite piece
                if (end_row, end_col) in pieces_pos:  # If the opposite piece is in the right position to be jumped
                    if (start_row + 2, start_col - 2) not in pieces_pos or board[start_row + 2][start_col - 2] != 0:  # Check for pieces in between
                        return False
                return True
        if start_row + end_row == 1 and start_col + end_col == 1:  # Down right move
            if board[end_row][end_col] == 1:  # If there is an opposite piece
                if (end_row, end_col) in pieces_pos:  # If the opposite piece is in the right position to be jumped
                    if (start_row + 2, start_col + 2) not in pieces_pos or board[start_row + 2][start_col + 2] != 0:  # Check for pieces in between
                        return False
                return True

    return False

def piece_jump(board, pieces_pos, start_row, start_col, end_row, end_col):
    board[end_row][end_col] = board[start_row][start_col]
    board[start_row][start_col] = 0
    pieces_pos.remove((start_row, start_col))
    if abs(start_row - end_row) == 2:  # If the piece jumped two rows, it means it's an attacking move and the attacked piece is removed
        if start_col - end_col == 1:  # Left jump
            pieces_pos.remove((start_row + end_row) // 2, start_col - 1)
        else:  # Right jump
            pieces_pos.remove((start_row + end_row) // 2, start_col + 1)

def user_input(screen, board, pieces_pos):
    selected_piece = None
    valid_move = False

    while not valid_move:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return True

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                col = pos[0] // SQUARESIZE
                row = pos[1] // SQUARESIZE

                if board[row][col] in (1, 2):  # If a piece of any color is clicked
                    if selected_piece is None:  # If no piece has been selected yet, this piece is selected
                        selected_piece = (row, col)
                        print(f"Selected piece at: {selected_piece}")
                    else:  # If a piece is already selected
                        if get_piece(board, row, col) == get_piece(board, selected_piece[0], selected_piece[1]):  # If the clicked piece is the same color as the selected one
                            selected_piece = None  # Deselect the piece
                            print("Deselected the piece.")
                        else:  # If the clicked piece is of opposite color
                            start_row, start_col = selected_piece
                            end_row, end_col = row, col
                            move = (start_row, start_col, end_row, end_col)  # Store the move
                            print(f"Move: {move}")
                            if is_valid_move(board, start_row, start_col, end_row, end_col, board[start_row][start_col]):  # Check if the move is valid
                                piece_jump(board, pieces_pos, start_row, start_col, end_row, end_col)  # Make the jump if valid
                                valid_move = True  # Set valid_move to True to end the loop
                                selected_piece = None
                            else:
                                print("Invalid move. Try again.")
        # Re-draw the board and pieces to show the selected piece (highlight it)
        draw_board(screen, board)
        draw_pieces(screen, board, pieces_pos)
        if selected_piece:
            pygame.draw.rect(screen, GREEN, (col * SQUARESIZE, row * SQUARESIZE, SQUARESIZE - BORDER, SQUARESIZE - BORDER), 4)
        pygame.display.flip()
    return False


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Checkers Game")

    board, pieces_pos = initialize_board()
    
    running = True
    while running:
        # Draw the game board and pieces
        draw_board(screen, board)
        draw_pieces(screen, board, pieces_pos)

        # Handle user input
        running = not user_input(screen, board, pieces_pos)
        
        # Update the display
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
