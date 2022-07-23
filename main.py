class Champion:

    def __init__(self, name, hasMana, isRanged) -> None:
        #name = string
        #hasMana = bool
        #isRanged = bool
        self.name = name
        self.hasMana = hasMana
        self.isRanged = isRanged

class Item:
    def __init__(self, name, isMythic) -> None:
        self.name = name
        self.isMythic = isMythic