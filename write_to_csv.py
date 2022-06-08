import chess.pgn
import csv

pgn = open("games/my_games.pgn")

f= open('games_data.csv', 'w')

writer = csv.writer(f)
header = ['result', 'white_player', 'black_player', 'white_elo', 'black_elo', 'timezone', 'start_time', 'end_time']
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
        data[1] = game.headers["White"]
        data[2] = game.headers["Black"]
        data[3] = game.headers["WhiteElo"]
        data[4] = game.headers["BlackElo"]
        data[5] = game.headers["Timezone"]
        #only get the hours for times
        data[6] = game.headers["StartTime"]
        data[7] = game.headers["EndTime"]
        
        writer.writerow(data)
        
    