SET sql_safe_updates = FALSE;

USE defaultdb;
DROP DATABASE IF EXISTS game CASCADE;
CREATE DATABASE IF NOT EXISTS game;

USE game;

CREATE TABLE scores (
    id uuid PRIMARY KEY NOT NULL DEFAULT gen_random_uuid(),
    playername STRING,
    score INT8,
    UNIQUE INDEX scores_playername (playername ASC)
);

INSERT INTO scores (playername, score)
  VALUES ('Mario', 1298);

INSERT INTO scores (playername, score)
  VALUES ('Luigi', 800);

INSERT INTO scores (playername, score)
  VALUES ('Sonic', 765);

INSERT INTO scores (playername, score)
  VALUES ('Pacman', 721);
