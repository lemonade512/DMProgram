CREATE TABLE IF NOT EXISTS Players
(player_id INTEGER PRIMARY KEY,
 Name TEXT, 
 AC INTEGER, 
 Listen INTEGER,
 Spot INTEGER, 
 Search INTEGER,
 Move_Silently INTEGER,
 Hide INTEGER);

CREATE TABLE IF NOT EXISTS Player_Owned_Items
(item_id INTEGER PRIMARY KEY,
 player_id INTEGER,
 Name TEXT,
 Description TEXT,
 FOREIGN KEY(player_id) REFERENCES Player(player_id));
