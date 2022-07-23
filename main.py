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

champion_pool = []

champion_pool.append(Champion("Zyra ", True, True))
champion_pool.append(Champion("Zoe ", True, True))
champion_pool.append(Champion("Zilean ", True, True))
champion_pool.append(Champion("Ziggs ", True, True))
champion_pool.append(Champion("Zeri ", True, True))
champion_pool.append(Champion("Zed ", False, False))
champion_pool.append(Champion("Zac ", False, False))
champion_pool.append(Champion("Yuumi ", True, True))
champion_pool.append(Champion("Yorick ", True, False))
champion_pool.append(Champion("Yone ", False, False))
champion_pool.append(Champion("Yasuo ", False, False))
champion_pool.append(Champion("Xin Zhao ", True, False))
champion_pool.append(Champion("Xerath ", True, True))
champion_pool.append(Champion("Xayah ", True, True))
champion_pool.append(Champion("Wukong ", True, False))
champion_pool.append(Champion("Warwick ", True, False))
champion_pool.append(Champion("Volibear ", True, False))
champion_pool.append(Champion("Vladimir ", False, True))
champion_pool.append(Champion("Viktor ", True, True))
champion_pool.append(Champion("Viego ", False, False))
champion_pool.append(Champion("Vi ", True, False))
champion_pool.append(Champion("Vex ", True, True))
champion_pool.append(Champion("Vel'Koz ", True, True))
champion_pool.append(Champion("Veigar ", True, True))
champion_pool.append(Champion("Vayne ", True, True))
champion_pool.append(Champion("Varus ", True, True))
champion_pool.append(Champion("Urgot ", True, True))
champion_pool.append(Champion("Udyr ", True, False))
champion_pool.append(Champion("Twitch ", True, True))
champion_pool.append(Champion("Twisted Fate ", True, True))
champion_pool.append(Champion("Tryndamere ", False,False))
champion_pool.append(Champion("Trundle ", True, False))
champion_pool.append(Champion("Thresh ", True, True))
champion_pool.append(Champion("Teemo ", True, True))
champion_pool.append(Champion("Taric ", True, False))
champion_pool.append(Champion("Talon ", True, False))
champion_pool.append(Champion("Taliyah ", True, True))
champion_pool.append(Champion("Tahm Kench ", True, False))
champion_pool.append(Champion("Syndra ", True, True))
champion_pool.append(Champion("Sylas ", True, False))
champion_pool.append(Champion("Swain ", True, True))
champion_pool.append(Champion("Soraka ", True, True))
champion_pool.append(Champion("Sona ", True, True))
champion_pool.append(Champion("Skarner", True, False))
champion_pool.append(Champion("Sivir ", True, True))
champion_pool.append(Champion("Sion ", True, False))
champion_pool.append(Champion("Singed ", True, False))
champion_pool.append(Champion("Shyvanna ", False,False))
champion_pool.append(Champion("Shen ", False,False))
champion_pool.append(Champion("Shaco ", True, False))
champion_pool.append(Champion("Sett ", False,False))
champion_pool.append(Champion("Seraphine ", True,True))
champion_pool.append(Champion("Senna ", True,True))
champion_pool.append(Champion("Sejuani ", True,False))
champion_pool.append(Champion("Samira ", True,True))
champion_pool.append(Champion("Ryze ", True,True))
champion_pool.append(Champion("Rumble ", False,False))
champion_pool.append(Champion("Riven ", False,False))
champion_pool.append(Champion("Rengar", False,False))
champion_pool.append(Champion("Renekton", False,False))
champion_pool.append(Champion("Renata Glasc", True,True))
champion_pool.append(Champion("Rell", True,False))
champion_pool.append(Champion("Rek'Sai", False,False))
champion_pool.append(Champion("Rammus", True,False))
champion_pool.append(Champion("Rakan", True,False))
champion_pool.append(Champion("Quinn", True,True))
champion_pool.append(Champion("Qiyana", True,False))
champion_pool.append(Champion("Pyke", True,False))
champion_pool.append(Champion("Poppy", True,False))
champion_pool.append(Champion("Pantheon", True,False))
champion_pool.append(Champion("Ornn", True,False))