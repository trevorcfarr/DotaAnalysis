CREATE TABLE dota_myheros
(hero_id INT NOT NULL AUTO_INCREMENT,
last_played BIGINT,
games INT,
win INT,
with_games INT,
with_win INT,
against_games INT,
against_win int,
PRIMARY KEY (hero_id));
