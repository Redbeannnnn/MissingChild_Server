from src.Server import Server
import asyncio
import random
from src.MissingChild.MC_Card import MC_Card


class MC_Server(Server):
    def __init__(self,socket_port:int = 8765):
        super().__init__(socket_port)
        self.players:list = []
        self.phase:str = "waiting"
        self.current_player:Player = None

    def next_player(self,player):
        count=self.players.index(player)
        while(not self.players[count+1].alive):
            count += 1
        return self.players[count+1]
    
    def last_player(self,player):
        count=self.players.index(player)
        while(not self.players[count-1].alive):
            count -= 1
        return self.players[count-1]
    

    async def __main__(self): 
        while True:
            if(len(self.players) == 3):
                break
            else:
                await asyncio.sleep(1)
        self.phase_enter("game")
        
        while True:
            #----------------------------------每轮游戏----------------------------------   
            for player in self.players:
                if(not player.alive):
                    continue

                player.refreash()
                self.current_player = player
                #从下一个玩家手里拿随机一张卡
                next_player = self.next_player(player)
                if(len(next_player.cards) > 0):
                    player.get_card_from_other = next_player.cards[random.randint(0, len(next_player.cards) - 1)]
                    next_player.cards.remove(player.get_card_from_other)

                #每个人30秒操作事件
                for i in range(60):
                    if(player.action_end):
                        continue
                    await asyncio.sleep(0.5)


    def get_command(self,player:str,message:str):
        if(not self.get_player_by_name(player,self.players) and self.phase == "waiting"):
            self.players.append(Player(player))
        pass

    def get_player_by_name(self,name:str,output):
        for player in self.players:
            if(player.name == name):
                output = player
                return True
        return False

    def phase_enter(self,phase:str):
        self.phase = phase
        self.send_message_to_all({"type":"phase_enter","phase":phase})
    
class Player:
    def __init__(self,name:str):
        self.name = name
        self.alive = True
        self.action_end = False
        self.get_card_from_other:MC_Card = None
        self.cards:list[MC_Card] = []

    def refreash(self):
        self.action_end = False
        self.get_card_from_other = None


    

    

