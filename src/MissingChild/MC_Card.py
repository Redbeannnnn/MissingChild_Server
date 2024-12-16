import json



class MC_CardList:
    def __init__(self):
        self.card_list = []

    def load_card_list(self):
        with open("src/CardList/MissingChildCardList.json", "r", encoding="utf-8") as f:
            self.card_list = json.load(f)

    def get_card_by_id(self, id: int):
        for card in self.card_list:
            if card["id"] == id:
                return card
        return None

    def get_card_by_name(self, name: str):
        for card in self.card_list:
            if card["name"] == name:
                return card
        return None



class MC_Card:
    def __init__(self,id:int,name:str,type:str,description:str,index_num:int,extra_round:int):
        self.id = id
        self.name = name
        self.type = type
        self.description = description
        self.index_num = index_num
        self.extra_round = extra_round

    def card_main(self):
        pass

    def to_dict(self):
        return {    
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "description": self.description,
            "index_num": self.index_num,
            "extra_round": self.extra_round
        }
