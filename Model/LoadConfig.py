import configparser
from Model.player import Player
from Model.monster import Monster
from Model.Equip import Equip


class LoadConfig():
    def LoadConfigPlayer(player):
        conf = configparser.ConfigParser()
        conf.read(r"..\config\player.config")
        player = Player(conf.getint(player, 'player_strength'),
                        conf.getint(player, 'player_agile'),
                        conf.getint(player, 'player_intelligence'),
                        conf.getint(player, 'player_physique'),
                        conf.get(player, 'player_name'),
                        conf.getint(player, 'player_blood'),
                        conf.getint(player, 'player_mana'),
                        conf.getint(player, 'player_attack'),
                        conf.getint(player, 'player_speed'),
                        conf.getint(player, 'player_criticalChance'),
                        conf.getint(player, 'player_defenses'),
                        conf.getint(player, 'player_experience'),
                        conf.getint(player, 'player_level'))
        # 初始化
        player.attack = 0
        player.blood = 0
        player.mana = 0
        player.speed = 0
        player.defenses = 0
        return player

    def LoadConfigMonster(monster):
        conf = configparser.ConfigParser()
        conf.read(r"..\config\monster.config")
        monster = Monster(conf.get(monster, 'monster_name'),
                          conf.getint(monster, 'monster_blood'),
                          conf.getint(monster, 'monster_attack'),
                          conf.getint(monster, 'monster_speed'),
                          conf.getint(monster, 'monster_criticalChance'),
                          conf.getint(monster, 'monster_skillInjuryRate'),
                          conf.getint(monster, 'monster_defenses'),
                          conf.getint(monster, 'monster_level'),
                          conf.getint(monster, 'monster_exe'))
        return monster

    def LoadConfigbackpack(backpack):
        conf = configparser.ConfigParser()
        conf.read(r"..\config\backpack.config")
        for i in range(1, 6):
            BackpackBar = 'BackpackBar_' + str(i)
            equipid = conf.get(BackpackBar, 'equipid')
            if(equipid != ''):
                backpack.append(equipid)
            else:
                backpack.append('')

        return backpack

    def LoadConfigEquips(equipids):
        conf = configparser.ConfigParser()
        conf.read(r"..\config\equip.config", encoding="utf-8-sig")
        equips = []
        for equipid in equipids:
            equip = Equip(conf.getint(equipid, 'equip_id'),
                          conf.get(equipid, 'equip_name'),
                          conf.get(equipid, 'equip_quality'),
                          conf.getint(equipid, 'equip_attack'),
                          conf.getint(equipid, 'equip_strength'),
                          conf.getint(equipid, 'equip_agile'),
                          conf.getint(equipid, 'equip_intelligence'),
                          conf.getint(equipid, 'equip_physique'),
                          conf.getint(equipid, 'equip_speed'),
                          conf.getint(equipid, 'equip_blood'),
                          conf.getint(equipid, 'equip_mana'),
                          conf.getint(equipid, 'equip_defenses'))

            equips.append(equip)
        return equips

    def LoadConfigEquip(equipid):
        conf = configparser.ConfigParser()
        conf.read(r"..\config\equip.config", encoding="utf-8-sig")

        equip = Equip(conf.getint(equipid, 'equip_id'),
                      conf.get(equipid, 'equip_name'),
                      conf.get(equipid, 'equip_quality'),
                      conf.getint(equipid, 'equip_attack'),
                      conf.getint(equipid, 'equip_strength'),
                      conf.getint(equipid, 'equip_agile'),
                      conf.getint(equipid, 'equip_intelligence'),
                      conf.getint(equipid, 'equip_physique'),
                      conf.getint(equipid, 'equip_speed'),
                      conf.getint(equipid, 'equip_blood'),
                      conf.getint(equipid, 'equip_mana'),
                      conf.getint(equipid, 'equip_defenses'))

        return equip
