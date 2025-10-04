import pygame
from random import randint

pygame.init()

# define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255,0, 0)
GREEN = (0, 255, 0)

# Set the height and width of the screen
WIDTH, HEIGHT = 800, 600

# Create a game board
board = [[0 for x in range(8)] for y in range(8)]

SQUARESIZE = int((WIDTH / 8))

# This will be a list that will contain all the information about the position of our pieces on the board.
pieces_pos = []
for row in range(8):
    for col in range(8):
        if row in (0, 7):
            if (col % 2) == 0:
                board[row][col] = 1
                pieces_pos.append((row, col)) # Save initial position of black pieces
            else:
                board[row][col] = 2
                pieces_pos.append((row, col)) # Save initial position of white pieces
        elif row in (1, 6):
                if (col % 2) == 0:
                    board[row][col] = 0
        else:
            board[row][col] = 0

# The size of the board's border
border = 4

# Open a new window 
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Checkers")

clock = pygame.time.Clock()
myFont = pygame.font.SysFont("monospace", 74)

def draw_board(board):
    # Draw the board
    for row in range(8):
        for col in range(8):
            pygame.draw.rect(
                screen,
                WHITE if (row + col) % 2 == 0 else BLACK,
                (col * SQUARESIZE, row * SQUARESIZE, SQUARESIZE - border, SQUARESIZE - border)
            )
    
    # Draw the red and green pieces
    for row in range(8):
        for col in range(8):
            if board[row][col] == 1:
                pygame.draw.circle(screen, RED, (int(col * SQUARESIZE + SQUARESIZE / 2), 
                    int(row * SQUARESIZE + SQUARESIZE / 2)), int(SQUARESIZE / 2 - border / 2))
            elif board[row][col] == 2:
                pygame.draw.circle(screen, GREEN, (int(col * SQUARESIZE + SQUARESIZE / 2), 
                    int(row * SQUARESIZE + SQUARESIZE / 2)), int(SQUARESIZE / 2 - border / 2))

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
    
    if piece == 0:  # There is no piece on the current cell
        return False
    
    # If the move is not in the 2 directions mentioned above or there is no opposite piece, it's an invalid move
    return False

def piece_jump(board, start_row, start_col, end_row, end_col):
    board[end_row][end_col] = board[start_row][start_col]
    board[start_row][start_col] = 0
    if abs(start_row - end_row) == 2:  # If the piece jumped two rows, it means it's an attacking move and the attacked piece is removed
        if start_col - end_col == 1:  # Left jump
            board[(start_row + end_row) // 2][start_col - 1] = 0
        else:  # Right jump
            board[(start_row + end_row) // 2][start_col + 1] = 0

def get_piece(board, row, col):
    return board[row][col]

def draw_pieces(board, pieces_pos):
    # Draw the red and green pieces
    for pos in pieces_pos:
        row, col = pos
        if board[row][col] == 1:
            pygame.draw.circle(screen, RED, (int(col * SQUARESIZE + SQUARESIZE / 2), 
                int(row * SQUARESIZE + SQUARESIZE / 2)), int(SQUARESIZE / 2 - border / 2))
        elif board[row][col] == 2:
            pygame.draw.circle(screen, GREEN, (int(col * SQUARESIZE + SQUARESIZE / 2), 
                int(row * SQUARESIZE + SQUARESIZE / 2)), int(SQUARESIZE / 2 - border / 2))

def user_input():
    selected_piece = None
    valid_move = False


    while not valid_move:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                col = pos[0] // SQUARESIZE
                row = pos[1] // SQUARESIZE

                if board[row][col] in (1, 2):  # If a piece of any color is clicked
                    if selected_piece is None:  # If no piece has been selected yet, this piece is selected
                        selected_piece = (row, col)
                        print(f"Selected piece at: {selected_piece}")
                    else:  # If a piece is already selected
                        if get_piece(board, row, col) == get_piece(board, selected_piece[0],
                                                                selected_piece[1]):  # If the clicked piece is the same color as the selected one
                            selected_piece = None  # Deselect the piece
                            print("Deselected the piece.")
                        else:  # If the clicked piece is of opposite color
                            start_row, start_col = selected_piece
                            end_row, end_col = row, col
                            move = (start_row, start_col, end_row, end_col)  # Store the move
                            print(f"Move: {move}")
                            if is_valid_move(board, start_row, start_col, end_row, end_col,
                                            board[start_row][start_col]):  # Check if the move is valid
                                piece_jump(board, start_row, start_col, end_row, end_col)  # Make the jump if valid
                                valid_move = True  # Set valid_move to True to end the loop
                                selected_piece = None
                            else:
                                print("Invalid move. Try again.")
        # Re-draw the board and pieces to show the selected piece (highlight it)
        draw_board(board)
        draw_pieces(board, pieces_pos)
        if selected_piece:
            pygame.draw.rect(screen, GREEN, (col * SQUARESIZE, row * SQUARESIZE, SQUARESIZE - border,
                                            SQUARESIZE - border), 4)
        pygame.display.flip()
        clock.tick(60)


def main():
    # pygame.font.init()  # You don't need this line if you've already initialized pygame
    # myFont = pygame.font.SysFont("monospace", 74)  # Select the font and size
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Draw the board
        draw_board(board)
        draw_pieces(board, pieces_pos)
        
        # text = myFont.render("Checkers", False, (BLACK))
        # screen.blit(text, (200, 10))
        pygame.display.flip()

        user_input()  # Take user input for the moves
        
        # Check if the game is over (no more jumps for any player)
        if len(pieces_pos) == 0:  # If all pieces are captured
            running = False
            print("Game is over!")
            break

        # computer_move()  # Uncomment this line to enable computer moves after each player's move

    pygame.quit()

if __name__ == "__main__":
    main()





