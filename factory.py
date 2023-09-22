import json
import xml.etree.ElementTree as ET
import player_pb2 as PlayerList

from player import Player

class PlayerFactory:
    def to_json(self, players):
        '''
            This function should transform a list of Player objects into a list with dictionaries.
        '''
        player_list = []
        for player in players:
            player_dict = {
                'nickname': player.nickname,
                'email': player.email,
                'date_of_birth': player.date_of_birth.strftime("%Y-%m-%d"),
                'xp': player.xp,
                'class': player.cls
            }
            player_list.append(player_dict)
        return player_list
        pass

    def from_json(self, list_of_dict):
        '''
            This function should transform a list of dictionaries into a list with Player objects.
        '''
        players = []
        for player_dict in list_of_dict:
            player = Player(
                player_dict['nickname'],
                player_dict['email'],
                player_dict['date_of_birth'],
                player_dict['xp'],
                player_dict['class']
            )
            players.append(player)
        return players
        pass

    def from_xml(self, xml_string):
        '''
            This function should transform a XML string into a list with Player objects.
        '''
        players = []
        root = ET.fromstring(xml_string)
        for player_element in root.findall('player'):
            nickname = player_element.find('nickname').text
            email = player_element.find('email').text
            date_of_birth = player_element.find('date_of_birth').text
            xp = int(player_element.find('xp').text)
            cls = player_element.find('class').text
            player = Player(nickname, email, date_of_birth, xp, cls)
            players.append(player)
        return players
        pass

    def to_xml(self, list_of_players):
        '''
            This function should transform a list with Player objects into a XML string.
        '''
        root = ET.Element('data')
        for player in list_of_players:
            player_element = ET.SubElement(root, 'player')
            nickname_element = ET.SubElement(player_element, 'nickname')
            nickname_element.text = player.nickname
            email_element = ET.SubElement(player_element, 'email')
            email_element.text = player.email
            dob_element = ET.SubElement(player_element, 'date_of_birth')
            dob_element.text = player.date_of_birth.strftime("%Y-%m-%d")
            xp_element = ET.SubElement(player_element, 'xp')
            xp_element.text = str(player.xp)
            cls_element = ET.SubElement(player_element, 'class')
            cls_element.text = player.cls
        xml_string = ET.tostring(root, encoding='utf-8')
        return xml_string.decode('utf-8')
        pass

    def from_protobuf(self, binary):
        '''
        This function transforms a binary protobuf string into a list with Player objects.
        '''
        players = []
        players_list = PlayerList.PlayersList()
        players_list.ParseFromString(binary)

        for player_msg in players_list.player:
            player = Player(
                player_msg.nickname,
                player_msg.email,
                player_msg.date_of_birth,
                player_msg.xp,
                PlayerList.Class.Name(player_msg.cls)
            )
            players.append(player)

        return players
    
    def to_protobuf(self, list_of_players):
        '''
        This function transforms a list with Player objects into a binary protobuf string.
        '''
        players_list = PlayerList.PlayersList()

        for player in list_of_players:
            player_msg = players_list.player.add()
            player_msg.nickname = player.nickname
            player_msg.email = player.email
            player_msg.date_of_birth = player.date_of_birth.strftime("%Y-%m-%d")
            player_msg.xp = player.xp
            player_msg.cls = PlayerList.Class.Value(player.cls)

        return players_list.SerializeToString()
