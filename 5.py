f = open("game_stats.txt" , "r")

class player:
    def __init__(self):
        name = "",
        HP,
        AP_cnt,
        AD,
        Armor

    def read_data(self):
        self.name = f.readline()
        self.HP = int(f.readline())
        self.AP_cnt = int(f.readline())
        self,AD = int(f.readline())
        self.Armor = int(f.readline())

    
class boss:
    def __init__(self):
        HP,
        AD,
        Armor

    def read_data(self):
        self.HP = int(f.readline())
        self.AD = int(f.readline())
        self,Armor = int(f.readline())

Player1 = player
Player2 = player
Player3 = player

Player1.read_data()
Player2.read_data()
Player3.read_data()
boss = boss()
boss.read_data
