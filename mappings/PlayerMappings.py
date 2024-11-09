import json
import os


class PlayerMappings:

    mappings = None


    @staticmethod
    def fanduel_to_cbs(fanDuelId):
        PlayerMappings.ensureMappings()

        for mapping in PlayerMappings.mappings:
            if mapping["fanduel"] == fanDuelId:
                return mapping["cbs"]

        return None

    @staticmethod
    def add(fanduelId, cbsId):
        PlayerMappings.mappings.append({ "fanduel": fanduelId, "cbs": cbsId})

    @staticmethod
    def ensureMappings():
        if PlayerMappings.mappings is None:
            PlayerMappings.load()

    @staticmethod
    def load():
        with open("./mappings/player_mappings.json", 'r', encoding='utf-8') as f:
            PlayerMappings.mappings = json.load(f)

    @staticmethod
    def save():
        with open("./mappings/player_mappings.json", 'w', encoding='utf-8') as f:
            json.dump(PlayerMappings.mappings, f, ensure_ascii=False, indent=2)