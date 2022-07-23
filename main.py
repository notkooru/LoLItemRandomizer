class Champion:

    def __init__(self, name, hasMana, isRanged) -> None:
        #name = string
        #hasMana = bool
        #isRanged = bool
        self.name = name
        self.hasMana = hasMana
        self.isRanged = isRanged

class Mythic:
    def __init__(self) -> None:
        pass

class Boots:
    def __init__(self) -> None:
        pass

champion_pool = []

champion_pool.append(Champion("Aatrox", False, False))
champion_pool.append(Champion("Ahri", True, True))
champion_pool.append(Champion("Akali", False, False))
champion_pool.append(Champion("Akshan", True, False))
champion_pool.append(Champion("Alistar", True, False))
champion_pool.append(Champion("Amumu", True, False))
champion_pool.append(Champion("Anivia", True, True))
champion_pool.append(Champion("Annie", True, True))
champion_pool.append(Champion("Aphelios", True, True))
champion_pool.append(Champion("Ashe", True, True))
champion_pool.append(Champion("Aurelion Sol", True, True))
champion_pool.append(Champion("Azir", True, True))
champion_pool.append(Champion("Bard", True, True))
champion_pool.append(Champion("Bel'Veth", False, False))
champion_pool.append(Champion("Blitzcrank", True, False))
champion_pool.append(Champion("Brand", True, True))
champion_pool.append(Champion("Caitlyn", True, True))
champion_pool.append(Champion("Camille", True, False))
champion_pool.append(Champion("Cassiopeia", True, True))
champion_pool.append(Champion("Cho'Gath", True, False))
champion_pool.append(Champion("Corki", True, True))
champion_pool.append(Champion("Darius", True, False))
champion_pool.append(Champion("Diana", True, False))
champion_pool.append(Champion("Dr. Mundo", True, False))
champion_pool.append(Champion("Draven", True, False))
champion_pool.append(Champion("Ekko", True, False))
champion_pool.append(Champion("Elise", True, True))
champion_pool.append(Champion("Evelynn", True, False))
champion_pool.append(Champion("Ezreal", True, True))
champion_pool.append(Champion("Fiddlesticks", True, False))
champion_pool.append(Champion("Fiora", True, False))
champion_pool.append(Champion("Fizz", True, False))
champion_pool.append(Champion("Galio", True, False))
champion_pool.append(Champion("Gangplank", True, False))
champion_pool.append(Champion("Gnar", False, True))
champion_pool.append(Champion("Gragas", True, False))
champion_pool.append(Champion("Graves", True, True))
champion_pool.append(Champion("Gwen", True, False))
champion_pool.append(Champion("Hecarim", True, False))
champion_pool.append(Champion("Heimerdinger", True, True))
champion_pool.append(Champion("Illaoi", True, False))
champion_pool.append(Champion("Irelia", True, False))
champion_pool.append(Champion("Ivern", True, True))
champion_pool.append(Champion("Janna", True, True))
champion_pool.append(Champion("Jarvan IV", True, False))
champion_pool.append(Champion("Jax", True, False))
champion_pool.append(Champion("Jhin", True, True))
champion_pool.append(Champion("Jinx", True, True))
champion_pool.append(Champion("Kai'Sa", True, True))
champion_pool.append(Champion("Kalista", True, True))
champion_pool.append(Champion("Karma", True, True))
champion_pool.append(Champion("Karthus", True, True))
champion_pool.append(Champion("Kassadin", True, True))
champion_pool.append(Champion("Katarina", False, False))
champion_pool.append(Champion("Kayle", True, True))
champion_pool.append(Champion("Kayn", True, False))
champion_pool.append(Champion("Kennen", False, True))
champion_pool.append(Champion("Kha'Zix", True, False))
champion_pool.append(Champion("Kindred", True, True))
champion_pool.append(Champion("Kled", False, True))
champion_pool.append(Champion("Kog'Maw", True, True))
champion_pool.append(Champion("LeBlanc", True, True))
champion_pool.append(Champion("Lee Sin", False, False))
champion_pool.append(Champion("Leona", True, False))
champion_pool.append(Champion("Lillia", True, True))
champion_pool.append(Champion("Lissandra", True, True))
champion_pool.append(Champion("Lux", True, True))
champion_pool.append(Champion("Malphite", True, False))
champion_pool.append(Champion("Malzahar", True, True))
champion_pool.append(Champion("Maokai", True, False))
champion_pool.append(Champion("Master Yi", True, False))
champion_pool.append(Champion("Miss Fortune", True, True))
champion_pool.append(Champion("Mordekaiser", False, False))
champion_pool.append(Champion("Morgana", True, True))
champion_pool.append(Champion("Nami", True, True))
champion_pool.append(Champion("Nasus", True, False))
champion_pool.append(Champion("Nautilus", True, False))
champion_pool.append(Champion("Neeko", True, True))
champion_pool.append(Champion("Nidalee", True, True))
champion_pool.append(Champion("Nilah", True, True))
champion_pool.append(Champion("Nocturne", True, False))
champion_pool.append(Champion("Nunu & Willump", True, False))
champion_pool.append(Champion("Olaf", True, False))
champion_pool.append(Champion("Orianna", True, True))
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