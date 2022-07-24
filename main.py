import random

class Champion:

    def __init__(self, name, hasMana, isRanged) -> None:
        #name = string
        #hasMana = bool
        #isRanged = bool
        self.name = name
        self.hasMana = hasMana
        self.isRanged = isRanged

class Mythic:
    def __init__(self, name, hasMana, hasManaRegen) -> None:
        self.name = name
        self.hasMana = hasMana
        self.hasManaRegen = hasManaRegen

class Boots:
    def __init__(self, name) -> None:
        self.name = name

class Legendary:
    def __init__(self, name, hasMana, hasManaRegen) -> None:
        self.name = name
        self.hasMana = hasMana
        self.hasManaRegen = hasManaRegen

class Runes:
    def __init__(self, name) -> None:
        self.name = name

class Shards:
    def __init__(self, type, slot) -> None:
        self.type = type
        self.slot = slot

champion_pool = []  #✓
boots_pool = [] #✓
mythic_pool = [] #✓
legendary_pool = [] #✓
runes_pool = [] #✓
shard_pool = [] #✓

precision = []
precision_keystone = []
precision_slot1 = []
precision_slot2 = []
precision_slot3 = []

domination = []
domination_keystone = []
domination_slot1 = []
domination_slot2 = []
domination_slot3 = []

sorcery = []
sorcery_keystone = []
sorcery_slot1 = []
sorcery_slot2 = []
sorcery_slot3 = []

resolve = []
resolve_keystone = []
resolve_slot1 = []
resolve_slot2 = []
resolve_slot3 = []

inspiration = []
inspiration_keystone = []
inspiration_slot1 = []
inspiration_slot2 = []
inspiration_slot3 = []

#Champs
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

#Boots
boots_pool.append(Boots("Boots of Speed")) #Tier 1 boots
boots_pool.append(Boots("Berserker's Greaves"))
boots_pool.append(Boots("Mobility Boots"))
boots_pool.append(Boots("Boots of Swiftness"))
boots_pool.append(Boots("Ionian Boots of Lucidity"))
boots_pool.append(Boots("Mercury's Threads"))
boots_pool.append(Boots("Plated Steelcaps"))
boots_pool.append(Boots("Sorcerer's Shoes"))

#Mythics
mythic_pool.append(Mythic("Eclipse",False,False))
mythic_pool.append(Mythic("Crown of the Shattered Queen",True,False))
mythic_pool.append(Mythic("Duskblade of Draktharr",False,False))
mythic_pool.append(Mythic("Evenshroud",False,False))
mythic_pool.append(Mythic("Everfrost",True,False))
mythic_pool.append(Mythic("Frostfire Gauntlet",False,False))
mythic_pool.append(Mythic("Galeforce",False,False))
mythic_pool.append(Mythic("Goredrinker",False,False))
mythic_pool.append(Mythic("Hextech Rocketbelt",False,False))
mythic_pool.append(Mythic("Immortal Shieldbow",False,False))
mythic_pool.append(Mythic("Imperial Mandate",False,True))
mythic_pool.append(Mythic("Kraken Slayer",False,False))
mythic_pool.append(Mythic("Liandry's Anguish",True,False))
mythic_pool.append(Mythic("Locket of the Iron Solari",False,False))
mythic_pool.append(Mythic("Luden's Tempest",True,False))
mythic_pool.append(Mythic("Moonstone Renewer",False,True))
mythic_pool.append(Mythic("Night Harvester",False,False))
mythic_pool.append(Mythic("Prowler's Claw",False,False))
mythic_pool.append(Mythic("Riftmaker",False,False))
mythic_pool.append(Mythic("Shurelya's Battlesong",False,True))
mythic_pool.append(Mythic("Stridebreaker",False,False))
mythic_pool.append(Mythic("Sunfire Aegis",False,False))
mythic_pool.append(Mythic("Trinity Force",False,False))
mythic_pool.append(Mythic("Turbo Chemtank",False,False))

#Legendary
legendary_pool.append(Legendary("Abyssal Mask", False, False))
legendary_pool.append(Legendary("Anathema's Chains", False, False))
legendary_pool.append(Legendary("Archangel's Staff", True, False)) #tear unfinished
legendary_pool.append(Legendary("Ardent Censer", False, True))
legendary_pool.append(Legendary("Axiom Arc", False, False))
legendary_pool.append(Legendary("Banshee's Veil", False, False))
legendary_pool.append(Legendary("Black Cleaver", False, False))
legendary_pool.append(Legendary("Black Mist Scythe", False, True)) #support starter
legendary_pool.append(Legendary("Blade of the Ruined King", False, False))
legendary_pool.append(Legendary("Bloodthirster", False, False))
legendary_pool.append(Legendary("Bulkward of the Mountain", False, False)) #support starter
legendary_pool.append(Legendary("Chempunk Chainsword", False, False))
legendary_pool.append(Legendary("Chemptech Putrifier", False, True))
legendary_pool.append(Legendary("Cosmic Drive", False, False))
legendary_pool.append(Legendary("Dead Man's Plate", False, False))
legendary_pool.append(Legendary("Death's Dance", False, False))
legendary_pool.append(Legendary("Demonic Embrace", False, False))
legendary_pool.append(Legendary("Edge of Night", False, False))
legendary_pool.append(Legendary("Essence Reaver", False, False)) #Mana is on hit
legendary_pool.append(Legendary("Fimbulwinter", True, False)) #tear finished
legendary_pool.append(Legendary("Force of Nature", False, False))
legendary_pool.append(Legendary("Frozen Heart", True, False))
legendary_pool.append(Legendary("Gargoyle Stoneplate", False, False))
legendary_pool.append(Legendary("Guardian Angel", False, False))
legendary_pool.append(Legendary("Guinsoo's Rageblade", False, False))
legendary_pool.append(Legendary("Horizon Focus", False, False))
legendary_pool.append(Legendary("Hullbreaker", False, False))
legendary_pool.append(Legendary("Infinity Edge", False, False))
legendary_pool.append(Legendary("Knight's Vow", False, False))
legendary_pool.append(Legendary("Lich Bane", False, False))
legendary_pool.append(Legendary("Lord Dominik's Regards", False, False))
legendary_pool.append(Legendary("Manamune", True, False)) #tear unfinished
legendary_pool.append(Legendary("Maw of Malmortius", False, False))
legendary_pool.append(Legendary("Mejai's Soulstealer", False, False))
legendary_pool.append(Legendary("Mercurial Scimitar", False, False))
legendary_pool.append(Legendary("Mikael's Blessing", False, True))
legendary_pool.append(Legendary("Morellonomicon", False, False))
legendary_pool.append(Legendary("Mortal Reminder", False, False))
legendary_pool.append(Legendary("Muramana", True, False)) #tear finished
legendary_pool.append(Legendary("Nashor's Tooth", False, False))
legendary_pool.append(Legendary("Navori Quickblades", False, False))
legendary_pool.append(Legendary("Pauldrons of Whiterock", False, False))
legendary_pool.append(Legendary("Phantom Dancer", False, False))
legendary_pool.append(Legendary("Rabadon's Deathcap", False, False))
legendary_pool.append(Legendary("Randuin's Omen", False, False))
legendary_pool.append(Legendary("Rapid Firecannon", False, False))
legendary_pool.append(Legendary("Ravenous Hydra", False, False))
legendary_pool.append(Legendary("Redemption", False, True))
legendary_pool.append(Legendary("Runnan's Hurricane", False, False))
legendary_pool.append(Legendary("Rylai's Crystal Scepter", False, False))
legendary_pool.append(Legendary("Seraph's Embrace", True, False)) # tear finished
legendary_pool.append(Legendary("Serpent's Fang", False, False))
legendary_pool.append(Legendary("Serylda's Grudge", False, False))
legendary_pool.append(Legendary("Shadowflame", False, False))
legendary_pool.append(Legendary("Shard of True Ice", False, True))
legendary_pool.append(Legendary("Silvermere Dawn", False, False))
legendary_pool.append(Legendary("Spirit Visage", False, False))
legendary_pool.append(Legendary("Staff of Flowing Water", False, True))
legendary_pool.append(Legendary("Sterak's Gage", False, False))
legendary_pool.append(Legendary("Stormrazor", False, False))
legendary_pool.append(Legendary("The Collector", False, False))
legendary_pool.append(Legendary("Thronmail", False, False))
legendary_pool.append(Legendary("Titanic Hydra", False, False))
legendary_pool.append(Legendary("Umbral Glaive", False, False))
legendary_pool.append(Legendary("Vigilant Wardstone", False, False))
legendary_pool.append(Legendary("Void Staff", False, False))
legendary_pool.append(Legendary("Warmog's Armor", False, False))
legendary_pool.append(Legendary("Winter's Approach", True, False)) #tear unfinished
legendary_pool.append(Legendary("Wit's End", False, False))
legendary_pool.append(Legendary("Youmuu's Ghostblade", False, False))
legendary_pool.append(Legendary("Zeke's Convergence", False, False))
legendary_pool.append(Legendary("Zhonya's Hourglass", False, False))

#runes
#precision
precision_keystone.append(Runes("Press the Attack",1,"Precision"))
precision_keystone.append(Runes("Lethal Tempo",1,"Precision"))
precision_keystone.append(Runes("Fleet Footwork",1,"Precision"))
precision_keystone.append(Runes("Conqueror",1,"Precision"))
precision_slot1.append(Runes("Overheal",2,"Precision"))
precision_slot1.append(Runes("Triumph",2,"Precision"))
precision_slot1.append(Runes("Presence of Mind",2,"Precision"))
precision_slot2.append(Runes("Legend:Alacrity",3,"Precision"))
precision_slot2.append(Runes("Legend:Tenacity",3,"Precision"))
precision_slot2.append(Runes("Legend:Bloodline",3,"Precision"))
precision_slot3.append(Runes("Coup de Grace",4,"Precision"))
precision_slot3.append(Runes("Cut Down",4,"Precision"))
precision_slot3.append(Runes("Last Stand",4,"Precision"))
#domination
domination_keystone.append(Runes("Electrocute",1,"Domination"))
domination_keystone.append(Runes("Predator",1,"Domination"))
domination_keystone.append(Runes("Dark Harvest",1,"Domination"))
domination_keystone.append(Runes("Hail of Blades",1,"Domination"))
domination_slot1.append(Runes("Cheap Shot",2,"Domination"))
domination_slot1.append(Runes("Taste of Blood",2,"Domination"))
domination_slot1.append(Runes("Sudden Impact",2,"Domination"))
domination_slot2.append(Runes("Zombie Ward",3,"Domination"))
domination_slot2.append(Runes("Ghost Poro",3,"Domination"))
domination_slot2.append(Runes("Eyeball Collection",3,"Domination"))
domination_slot3.append(Runes("Treasure Hunter",4,"Domination"))
domination_slot3.append(Runes("Ingenious Hunter",4,"Domination"))
domination_slot3.append(Runes("Relentless Hunter",4,"Domination"))
domination_slot3.append(Runes("Ultimate Hunter",4,"Domination"))
#sorcery
sorcery_keystone.append(Runes("Summon Aery",1,"Sorcery"))
sorcery_keystone.append(Runes("Arcane Comet",1,"Sorcery"))
sorcery_keystone.append(Runes("Phase Rush",1,"Sorcery"))
sorcery_slot1.append(Runes("Nullifying Orb",2,"Sorcery"))
sorcery_slot1.append(Runes("Manaflow Band",2,"Sorcery"))
sorcery_slot1.append(Runes("Nimbus Cloak",2,"Sorcery"))
sorcery_slot2.append(Runes("Transcendence",3,"Sorcery"))
sorcery_slot2.append(Runes("Celerity",3,"Sorcery"))
sorcery_slot2.append(Runes("Absolute Focus",3,"Sorcery"))
sorcery_slot3.append(Runes("Scorch",4,"Sorcery"))
sorcery_slot3.append(Runes("Waterwalking",4,"Sorcery"))
sorcery_slot3.append(Runes("Gathering Storm",4,"Sorcery"))
#resolve
resolve_keystone.append(Runes("Grasp of the Undying",1,"Resolve"))
resolve_keystone.append(Runes("Aftershock",1,"Resolve"))
resolve_keystone.append(Runes("Guardian",1,"Resolve"))
resolve_slot1.append(Runes("Demolish",2,"Resolve"))
resolve_slot1.append(Runes("Font of Life",2,"Resolve"))
resolve_slot1.append(Runes("Shield Bash",2,"Resolve"))
resolve_slot2.append(Runes("Conditioning",3,"Resolve"))
resolve_slot2.append(Runes("Second Wind",3,"Resolve"))
resolve_slot2.append(Runes("Bone Plating",3,"Resolve"))
resolve_slot3.append(Runes("Overgrowth",4,"Resolve"))
resolve_slot3.append(Runes("Revitalize",4,"Resolve"))
resolve_slot3.append(Runes("Unflinching",4,"Resolve"))
#inspiration
inspiration_keystone.append(Runes("Glacial Augment",1,"Inspiration"))
inspiration_keystone.append(Runes("Unsealed Spellbook",1,"Inspiration"))
inspiration_keystone.append(Runes("First Strike",1,"Inspiration"))
inspiration_slot1.append(Runes("Hextech Flashtraption",2,"Inspiration"))
inspiration_slot1.append(Runes("Magical Footwear",2,"Inspiration"))
inspiration_slot1.append(Runes("Perfect Timing",2,"Inspiration"))
inspiration_slot2.append(Runes("Future's Market",3,"Inspiration"))
inspiration_slot2.append(Runes("Minion Dematerializer",3,"Inspiration"))
inspiration_slot2.append(Runes("Biscuit Delivery",3,"Inspiration"))
inspiration_slot3.append(Runes("Cosmic Insight",4,"Inspiration"))
inspiration_slot3.append(Runes("Approach Velocity",4,"Inspiration"))
inspiration_slot3.append(Runes("Time Warp Tonic",4,"Inspiration"))
#trees
precision.append(precision_keystone)
precision.append(precision_slot1)
precision.append(precision_slot2)
precision.append(precision_slot3)

domination.append(domination_keystone)
domination.append(domination_slot1)
domination.append(domination_slot2)
domination.append(domination_slot3)

sorcery.append(sorcery_keystone)
sorcery.append(sorcery_slot1)
sorcery.append(sorcery_slot2)
sorcery.append(sorcery_slot3)

resolve.append(resolve_keystone)
resolve.append(resolve_slot1)
resolve.append(resolve_slot2)
resolve.append(resolve_slot3)

inspiration.append(inspiration_keystone)
inspiration.append(inspiration_slot1)
inspiration.append(inspiration_slot2)
inspiration.append(inspiration_slot3)

#pool
runes_pool.append(precision)
runes_pool.append(domination)
runes_pool.append(sorcery)
runes_pool.append(resolve)
runes_pool.append(inspiration)

#shards
#slot 1
shard_pool.append(Shards("Adaptive", 1))
shard_pool.append(Shards("Attack Speed", 1))
shard_pool.append(Shards("Ability Haste", 1))
#slot 2
shard_pool.append(Shards("Adaptive", 2))
shard_pool.append(Shards("Armor", 2))
shard_pool.append(Shards("Magic Resist", 2))
#slot 3
shard_pool.append(Shards("Health", 2))
shard_pool.append(Shards("Armor", 2))
shard_pool.append(Shards("Magic Resist", 2))

final_build = []
final_build.append(random.choice(champion_pool))
final_build.append(random.choice(mythic_pool))
final_build.append(random.choice(boots_pool))
final_build.append(random.choice(legendary_pool))
final_build.append(random.choice(legendary_pool))
final_build.append(random.choice(legendary_pool))
final_build.append(random.choice(legendary_pool))

final_runes = []
primary_tree = random.choice(runes_pool)
secondary_tree = random.choice(runes_pool)

if primary_tree == secondary_tree:
    secondary_tree = random.choice(runes_pool)
secondary_tree.pop(0)
secondary_tree.pop(random.randrange(len(secondary_tree)))

for slot in primary_tree:
    final_runes.append(random.choice(slot))

for slot in secondary_tree:
    final_runes.append(random.choice(slot))

roles = ["top", "yongol", "mid", "adc", "support"]

print(f"{final_build[0].name}\nBuild: {final_build[1].name}, {final_build[2].name}, {final_build[3].name}, {final_build[4].name}, {final_build[5].name}, {final_build[6].name}")
print(f"Runes: {final_runes[0].name}, {final_runes[1].name}, {final_runes[2].name}, {final_runes[3].name}, {final_runes[4].name}, {final_runes[5].name}")

print(random.choice(roles))