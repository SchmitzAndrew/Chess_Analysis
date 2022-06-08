import pandas as pd

df = pd.read_csv("games_data.csv")

print(df.head())

# determine wins and losses
result_freq = df['result'].value_counts(ascending = True)
print(result_freq.head())
wins = result_freq.win
losses = result_freq.loss
print(f"Winrate: { wins/ (wins +losses)}")

#group dataset by time

df.groupby('start_time')

print(df.head()).count()



