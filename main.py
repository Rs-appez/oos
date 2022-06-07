import os
from bs4 import BeautifulSoup

from model.player import Player


tournaments = []
players  = []
matches = []

#load all tournament file
for file in os.listdir("./tournament"):
    if(file.endswith('.tournament')):
        with open("./tournament/"+file, 'rb') as f:
                data = f.read()
        
        tournaments.append(BeautifulSoup(data,'xml'))

for tournament in tournaments:

    #load player
    for player_xml in tournament.find_all('TournPlayer'):

        id = player_xml.find("ID").get_text()
        new = True

        for player in players:
            if(player.id == id):
                new = False
                player.participaton +=  1

        if new :
            player = Player(player_xml.find("FirstName").get_text()+" "+player_xml.find("LastName").get_text(),id)
            
            players.append(player)

    #load matches
    for match_xml in tournament.find_all('TournMatch'):

        id_players = []
        for player in match_xml.find_all("Player"):
            id_players.append("0"+player.get_text())


        winner_id = match_xml.find("Winner").get_text()

        print(id_players)

        for player_id in id_players:
            if not (player_id == '00'):
                print(player_id)
                player_index = players.index(Player('',player_id))

                player = players[player_index]

                if match_xml.find("Status").get_text() == 'Winner':
                    if player_id == winner_id:
                        player.win += 1
                    else :
                        player.loose += 1
                elif  match_xml.find("Status").get_text() == 'Draw':

                    player.draw +=1

#make html
players.sort(reverse = True,key=Player.triPts)
    
file = open('res.html','w')
file.write("<!DOCTYPE html><html><head></head> <body><h1>Resultats OOS </h1><div>")
for i in range(0,len(players)):
    file.write( f"N° {i+1} - {players[i]}" + "<br>")
file.write("<div></body></html>")
file.close()
