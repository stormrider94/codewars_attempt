class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    def is_worth_it(self):
        booty = self.draft - self.crew * 1.5
        return booty > 20
