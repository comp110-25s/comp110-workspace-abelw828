"""File to define River class."""

from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear


class River:
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        fish_copy: list[Fish] = self.fish
        bears_copy: list[Bear] = self.bears
        idxf: int = 0
        idxb: int = 0
        for obj in fish_copy:
            if Fish.age > 3:
                fish_copy.pop(idxf)
            idxf += 1
        for bear in bears_copy:
            if Bear.age > 5:
                bears_copy.pop(idxb)
            idxb += 1
        self.fish = fish_copy
        self.bears = bears_copy

    def bears_eating(self):
        if len(self.fish) >= 5:
            for bear in self.bears:
                idx: int = 0
                self.remove_fish(3)
                self.bears[idx].eat(num_fish=3)
                idx += 1

    def check_hunger(self):
        bear_copy: list[Bear] = self.bears
        for bear in bear_copy:
            idx: int = 0
            if Bear.hunger_score < 0:
                bear_copy.pop(idx)
            idx += 1
        self.bears = bear_copy

    def repopulate_fish(self):
        n: int = len(self.fish)
        for _ in range(0, (n // 2) * 4):
            self.fish.append(Fish())

    def repopulate_bears(self):
        n: int = len(self.bears)
        for _ in range(0, n // 2):
            self.bears.append(Bear())

    def view_river(self):
        print(f"~~~ Day {self.day} ~~~")
        print(f"Fish Population: {len(self.fish)}")
        print(f"Bear Population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        idx: int = 1
        if idx < 8:
            self.one_river_day()
            idx += 1
        return None

    def remove_fish(self, amount: int):
        idx: int = 0
        if idx < amount:
            self.fish.pop(idx)
            idx += 1
