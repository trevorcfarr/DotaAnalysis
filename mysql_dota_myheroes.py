import requests
import json
import pymysql
import pandas as pd

print('Starting...')

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='xxxxxxx',
						db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute('USE dota2analysis')

account_id = 20122248

# API Query for Heroes
sess = requests.Session()
html = f"https://api.opendota.com/api/players/{account_id}/heroes?api_key=API_KEY"
response = sess.get(html)

content = response.content.decode("utf-8")
heroes = json.loads(content)

for myhero in heroes:

	query = """INSERT IGNORE INTO dota_myheroes (hero_id, last_played,
											 games, win,
											 with_games, with_win,
											 against_games, against_win) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""

	cur.execute(query, (myhero['hero_id'], myhero['last_played'], myhero['games'], myhero['win'],
						myhero['with_games'], myhero['with_win'], myhero['against_games'], myhero['against_win']))

	conn.commit()
	print('Added {}.'.format(myhero['hero_id']))

csvmyheroquery = """SELECT dota_heroes.id, dota_heroes.localized_name, dota_heroes.carry, dota_heroes.jungler, dota_heroes.pusher, 
 							dota_heroes.nuker, dota_heroes.disabler, dota_heroes.initiator, dota_heroes.durable, dota_heroes.support,
							dota_myheroes.last_played, dota_myheroes.games, dota_myheroes.win, dota_myheroes.with_games,
							dota_myheroes.against_games, dota_myheroes.against_win
					FROM dota_heroes
					JOIN dota_myheroes
					ON dota_heroes.id = dota_myheroes.hero_id
					ORDER BY dota_heroes.id"""

cur.execute(csvmyheroquery)
conn.commit()
df = pd.read_sql_query(csvmyheroquery, conn)

df.to_csv('/Users/trevorfarr/Desktop/stuff/python_stuff/Dota2Analysis/dota_myhero_stats.csv', index=False)

# Close MySQL Database
cur.close()
conn.close()
print('Done.')
