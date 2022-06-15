import chess.pgn
import csv

pgn = open("games/my_games.pgn")

f= open('games_data.csv', 'w')

writer = csv.writer(f)
header = ['result', 'win', 'loss', 'draw','white_player', 'black_player', 'white_elo', 'black_elo', 'timezone', 'start_time', 'end_time']
writer.writerow(header)
data = header

username = "SCHMITZ874"

def game_result(game):
    result = game.headers["Result"][0:2]
    white_player = game.headers["White"]
    black_player = game.headers["Black"]

    # player either won as white 
    if (white_player == username and result == "1-") or (black_player == username and result == "0-"):
        return "win"
    elif result == "1/":
        return "tie"
    else:
        return "loss"
    
    

while True:
    game = chess.pgn.read_game(pgn)
    if game is None:
        break
    else:
        data[0] = game_result(game)
        #wins, loses, draws
        data[1] = 0
        data[2] = 0
        data[3] = 0
        if data[0] == "win":
            data[1] = 1
        elif data[0] == "loss":
            data[2] = 1
        else:
            data[3] = 1
        data[4] = game.headers["White"]
        data[5] = game.headers["Black"]
        data[6] = game.headers["WhiteElo"]
        data[7] = game.headers["BlackElo"]
        data[8] = game.headers["Timezone"]
        data[9] = game.headers["StartTime"]
        data[10] = game.headers["EndTime"]
        
        writer.writerow(data)
        
    