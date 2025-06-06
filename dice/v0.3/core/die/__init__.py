from core.rune.types import Empty
from random import randint

class Die:
    _name = "base"
    def __init__(self, sides: int, runes:list = None, upgrades: int = None):
        self.sides = sides
        self.runes = runes or [Empty()]*sides
        self.upgrades = upgrades or 0
    
    @property
    def name(self):
        '''<type> <sides><upgrades>'''
        return f"{self._name} d{self.sides}{"+" if self.upgrades > 0 else ""}{self.upgrades if self.upgrades != 0 else ""}"

    @property
    def cost(self):
        cost = self.sides*2
        for rune in self.runes:
            cost += rune.cost
        return cost

    def attach_rune(self, rune, face_id):
        old_rune = self.runes[face_id]
        self.runes[face_id] = rune
        return old_rune

    def remove_rune(self, face_id):
        old_rune = self.runes[face_id]
        self.runes[face_id] = Empty()
        return old_rune
    
    def upgrade(self):
        self.upgrades += 1
    
    def roll(self):
        raw = randint(0, self.sides-1) + 1
        value =  raw + self.upgrades
        rune = self.runes[raw-1]
        return rune, value, raw
    
    def __str__(self):
        '''<type> <sides><upgrades>: <runes>'''
        return f"{self._name} d{self.sides}{"+" if self.upgrades > 0 else ""}{self.upgrades if self.upgrades != 0 else ""}: {', '.join([str(r) for r in self.runes])}"