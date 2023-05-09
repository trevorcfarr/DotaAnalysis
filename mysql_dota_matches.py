import requests
import json
import pymysql
import pandas as pd
pd.options.display.max_columns = 50

# Initializing
print('Starting...')

# MySQL
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='xxxxxxx',
					    db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute('USE dota2analysis')

# API Query for Wins
account_id = 20122248
games_won = {"win": 1} # Games I won

sess = requests.Session()
html = f"https://api.opendota.com/api/players/{account_id}/matches?api_key=API_KEY"
response = sess.get(html, params=games_won)
content = response.content.decode("utf-8")
wins = json.loads(content)

# API Query for Losses
games_lost = {"win": 0} # Games I lost
response = sess.get(html, params=games_lost)
content = response.content.decode("utf-8")
losses = json.loads(content)

# Write Wins into MySQL
total_matches = len(wins) + len(losses)
count = 1

for match in wins:

	query = """INSERT IGNORE INTO dota_matches (match_id, player_slot,
										 radiant_win, duration,
										 game_mode, lobby_type,
										 hero_id, start_time,
										 version, kills, deaths, 
										 assists, skill, result) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,1)"""

	cur.execute(query, (match['match_id'], match['player_slot'],
						match['radiant_win'], match['duration'],
						match['game_mode'], match['lobby_type'],
						match['hero_id'], match['start_time'],
						match['version'], match['kills'],
						match['deaths'], match['assists'], match['skill']))
	conn.commit()
	print(f'Match {count} of {total_matches} added.')
	count += 1

# Write Losses into MySQL
for match in losses:

	query = """INSERT IGNORE INTO dota_matches (match_id, player_slot,
										 radiant_win, duration,
										 game_mode, lobby_type,
										 hero_id, start_time,
										 version, kills,
										 deaths, assists, skill, result) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,0)"""

	cur.execute(query, (match['match_id'], match['player_slot'],
						match['radiant_win'], match['duration'],
						match['game_mode'], match['lobby_type'],
						match['hero_id'], match['start_time'],
						match['version'], match['kills'],
						match['deaths'], match['assists'], match['skill']))
	conn.commit()
	print(f'Match {count} of {total_matches} added.')
	count += 1

csvmatchquery = """SELECT result, radiant_win, duration, start_time, game_mode,
		localized_name, kills, deaths, assists, primary_attr,
		attack_type, carry, jungler, pusher, nuker, disabler,
		initiator, durable, support, legs

		FROM dota_matches JOIN dota_heroes ON (hero_id=id)"""

df = pd.read_sql_query(csvmatchquery, conn)
df.to_csv('/Users/trevorfarr/Desktop/stuff/python_stuff/Dota2Analysis/dota_stats.csv', index=False)


# Close MySQL Database
cur.close()
conn.close()
print('Done.')
