# IITD-Game
COP290 Sem-ll 2024 A2 ST2 - Game Dev

# Running the server
- To run the server on localhost
```
./scripts/run_server.sh
```
- To run the server on the wifi network
```
./scripts/run_server.sh wifi
```
This will print the ip address of the server. Now we need to join the game at this ip address.

# Joining the game
Run the following command to join the game mentioning the ip address of the server and the alias of the player.

```
./scripts/run_game.sh ip_address alias_of_the_player
```