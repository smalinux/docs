import chess
import chess.svg

#
import time
import pyautogui
from selenium import webdriver
import selenium
from selenium.webdriver.common import keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
#

#
def run_brawser():
    browser = webdriver.Firefox()
    exe_path = 'D:\python\geckodriver.exe'
    binary = FirefoxBinary('C:\Program Files\Mozilla Firefox\\firefox.exe')
    browser = webdriver.Firefox(firefox_binary=binary, executable_path=exe_path)

    browser.get("file:///D:/python/board.svg")
    browser.save_screenshot("board.png")
#

###################################
# Board maninpulations
###################################
board = chess.Board()
board.push_san("e4")
board.push_san("e5")
board.push_san("Qh5")
board.push_san("Nc6")
board.push_san("Bc4")
board.push_san("Nf6")
board.push_san("Qxf7")
board.is_checkmate()



str = chess.svg.board(board, size=350)

###################################
# Write the board back to svg file
###################################
f = open("board.svg", "w+")
f.write(str)
f.close()

###################################
# Run
###################################
print(board)
print(board.is_stalemate())
print(board.is_checkmate())
print(board.is_check())
print("==")
print(board.is_attacked_by(chess.WHITE, chess.E8))
print("==")
attackers = board.attackers(chess.WHITE, chess.F3)
print(attackers)
print(chess.G2 in attackers)
print(attackers)
# invoke the brawser
# run_brawser()
################################################################
# Core
################################################################
print(chess.WHITE)
print(chess.BLACK)
print(chess.Color)

print("Chess.PieceType")
print(chess.PAWN)
print(chess.KNIGHT)
print(chess.PieceType)
print(chess.piece_name(6))
print(chess.piece_name(chess.KNIGHT))

print("Squares")
print(chess.A1) # 0
print(chess.B1) # 1
print(chess.C1) # 2
print(chess.H8) # 63

for i in chess.SQUARES:
    print(i, end="-")

print(chess.SQUARE_NAMES)
print(chess.FILE_NAMES)
print(chess.RANK_NAMES)
print(chess.parse_square("h1"))
print(chess.square_name(chess.G8))

print(chess.square_distance(chess.C3, chess.E5))
print("==")
print(chess.square_mirror(chess.G8))

print("Pieces")
print(chess.Piece(chess.ROOK, chess.BLACK))
print(chess.piece_symbol(chess.ROOK))

while True:
    pass
