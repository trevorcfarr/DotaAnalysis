CREATE TABLE dota_matches
(match_id BIGINT NOT NULL AUTO_INCREMENT,
player_slot INT,
radiant_win TINYINT(1),
duration INT,
game_mode INT,
lobby_type INT,
hero_id INT,
start_time BIGINT,
version INT,
kills INT,
deaths INT,
assists INT,
skill INT,
result TINYINT(1),
PRIMARY KEY (match_id));