NORMAL = "normal"
WILD = "wild"
WILD4 = "wild4"
REVERSE = "reverse"
NULL = "null"

class Card:
    def __init__(self) -> None:
        self.ctype = None
        self.colour = None
        self.number = None

    def can_be_placed_on(self, card) -> bool:
        if self.ctype == NORMAL:
            if self.colour and card.colour:
                if self.colour == card.colour:
                    return True
            
            if self.number and card.number:
                if self.number == card.number:
                    return True

            return False
            
        elif self.ctype == WILD or self.ctype == WILD4: return True

        elif self.ctype == NULL or card.ctype == REVERSE:
            if self.colour and card.colour:
                if self.colour == card.colour:
                    return True

            if card.ctype == self.ctype:
                return True

            return False

class NormalCard(Card):
    def __init__(self, colour, number) -> None:
        super().__init__()
        self.ctype = "normal"
        self.colour = colour
        self.number = number

class WildCard(Card):
    def __init__(self) -> None:
        super().__init__()
        self.ctype = "wild"
        
class Wild4Card(Card):
    def __init__(self) -> None:
        super().__init__()
        self.ctype = "wild4"
        
class ReverseCard(Card):
    def __init__(self, colour) -> None:
        super().__init__()
        self.ctype = "reverse"
        self.colour = colour
        
class NullCard(Card):
    def __init__(self, colour) -> None:
        super().__init__()
        self.ctype = "null"
        self.colour = colour