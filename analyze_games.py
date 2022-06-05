import chess.pgn

pgn = open("games.pgn")

games = []

username = "SCHMITZ874"

while True:
    game = chess.pgn.read_game(pgn)
    if game is None:
        break
    games.append(game)


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


wins = 0
ties = 0
losses = 0
for game in games:
    if game_result(game) == "win":
        wins += 1
    elif game_result(game) == "tie":
        ties += 1
    else:
        losses += 1

print(f"Winrate: {wins/ (wins + losses)}  Games played: {wins + losses + ties}")
