from enum import Enum

from List.configDict import locationType, itemType
from List.inventory import magic, keyblade, ability, misc, report
from List.location.graph import DefaultLogicGraph, RequirementEdge, chest, popup, item_bonus, hybrid_bonus, stat_bonus, \
    LocationGraphBuilder, START_NODE
from Module.itemPlacementRestriction import ItemPlacementHelpers


class NodeId(str, Enum):
    Passage = "Passage"
    PassageChests = "Passage Chests"
    InnerChamber = "Inner Chamber"
    InnerChamberChests = "Inner Chamber Chests"
    CerberusBonus = "Cerberus Bonus"
    ColiseumMapPopup = "Coliseum Map Popup"
    UrnsBonus = "Urns Bonus"
    UnderworldEntrance = "Underworld Entrance"
    UnderworldEntranceChests = "Underworld Entrance Chests"
    CavernsEntrance = "Caverns Entrance"
    CavernsEntranceChests = "Caverns Entrance Chests"
    LostRoad = "Lost Road"
    LostRoadChests = "Lost Road Chests"
    Atrium = "Atrium"
    AtriumChests = "Atrium Chests"
    DemyxOlympusColiseum = "Demyx (OC)"
    TheLock = "The Lock"
    TheLockChests = "The Lock Chests"
    PeteOlympusColiseum = "Pete (OC)"
    Hydra = "Hydra"
    AuronsStatue = "Auron Statue"
    Hades = "Hades"
    PainAndPanicCup = "Pain and Panic Cup"
    CerberusCup = "Cerberus Cup"
    TitanCup = "Titan Cup"
    GoddessOfFateCup = "Goddess of Fate Cup"
    ParadoxCups = "Paradox Cups"
    Zexion = "AS Zexion"
    DataZexion = "Data Zexion"


class CheckLocation(str, Enum):
    PassageMythrilShard = "Passage Mythril Shard"
    PassageMythrilStone = "Passage Mythril Stone"
    PassageEther = "Passage Ether"
    PassageApBoost = "Passage AP Boost"
    PassageHiPotion = "Passage Hi-Potion"
    InnerChamberUnderworldMap = "Inner Chamber Underworld Map"
    InnerChamberMythrilShard = "Inner Chamber Mythril Shard"
    Cerberus = "Cerberus"
    ColiseumMap = "Coliseum Map"
    Urns = "Urns"
    UnderworldEntrancePowerBoost = "Underworld Entrance Power Boost"
    CavernsEntranceLucidShard = "Caverns Entrance Lucid Shard"
    CavernsEntranceApBoost = "Caverns Entrance AP Boost"
    CavernsEntranceMythrilShard = "Caverns Entrance Mythril Shard"
    LostRoadBrightShard = "The Lost Road Bright Shard"
    LostRoadEther = "The Lost Road Ether"
    LostRoadMythrilShard = "The Lost Road Mythril Shard"
    LostRoadMythrilStone = "The Lost Road Mythril Stone"
    AtriumLucidStone = "Atrium Lucid Stone"
    AtriumApBoost = "Atrium AP Boost"
    DemyxOlympusColiseum = "Demyx OC"
    DemyxOcSecretAnsemReport5 = "Secret Ansem Report 5"
    OlympusStone = "Olympus Stone"
    LockCavernsMap = "The Lock Caverns Map"
    LockMythrilShard = "The Lock Mythril Shard"
    LockApBoost = "The Lock AP Boost"
    PeteOlympusColiseum = "Pete (OC)"
    Hydra = "Hydra"
    HerosCrest = "Hero's Crest"
    AuronssStatue = "Auron's Statue"
    Hades = "Hades"
    GuardianSoul = "Guardian Soul"
    PainPanicCupProtectBelt = "Protect Belt (Pain and Panic Cup)"
    PainPanicCupSerenityGem = "Serenity Gem (Pain and Panic Cup)"
    CerberusCupRisingDragon = "Rising Dragon (Cerberus Cup)"
    CerberusCupSerenityCrystal = "Serenity Crystal (Cerberus Cup)"
    TitanCupGenjiShield = "Genji Shield (Titan Cup)"
    TitanCupSkillfulRing = "Skillful Ring (Titan Cup)"
    GoddessOfFateCupFatalCrest = "Fatal Crest (Goddess of Fate Cup)"
    GoddessOfFateCupOrichalcumPlus = "Orichalcum+ (Goddess of Fate Cup)"
    ParadoxCupsHadesCupTrophy = "Hades Cup Trophy (Paradox Cups)"
    ZexionBonus = "Zexion Bonus"
    ZexionBookOfShadows = "Zexion (AS) Book of Shadows"
    DataZexionLostIllusion = "Zexion (Data) Lost Illusion"

class OCLogicGraph(DefaultLogicGraph):
    def __init__(self,reverse_rando,keyblade_unlocks):
        DefaultLogicGraph.__init__(self,NodeId)
        keyblade_lambda = lambda inv : not keyblade_unlocks or ItemPlacementHelpers.need_oc_keyblade(inv)
        self.logic[NodeId.Passage][NodeId.PassageChests] = keyblade_lambda
        self.logic[NodeId.InnerChamber][NodeId.InnerChamberChests] = keyblade_lambda
        self.logic[NodeId.UnderworldEntrance][NodeId.UnderworldEntranceChests] = keyblade_lambda
        self.logic[NodeId.CavernsEntrance][NodeId.CavernsEntranceChests] = keyblade_lambda
        self.logic[NodeId.LostRoad][NodeId.LostRoadChests] = keyblade_lambda
        self.logic[NodeId.Atrium][NodeId.AtriumChests] = keyblade_lambda
        self.logic[NodeId.TheLock][NodeId.TheLockChests] = keyblade_lambda
        pain_and_panic_check = ItemPlacementHelpers.dc2_check
        cerberus_cup_check = lambda inv: ItemPlacementHelpers.ht1_check(inv) and ItemPlacementHelpers.ag1_check(inv) and ItemPlacementHelpers.pl1_check(inv)
        goddess_of_fate_check = lambda inv: cerberus_cup_check(inv) and pain_and_panic_check(inv) and ItemPlacementHelpers.twtnw_post_saix_check(inv)
        if not reverse_rando:
            self.logic[START_NODE][NodeId.Passage] = ItemPlacementHelpers.oc1_check
            self.logic[NodeId.Hydra][NodeId.AuronsStatue] = ItemPlacementHelpers.oc2_check
            self.logic[NodeId.Hydra][NodeId.PainAndPanicCup] = pain_and_panic_check
            self.logic[NodeId.Hydra][NodeId.CerberusCup] = cerberus_cup_check
            self.logic[NodeId.Hades][NodeId.GoddessOfFateCup] = goddess_of_fate_check
            self.logic[NodeId.Hades][NodeId.ParadoxCups] = lambda inv: ItemPlacementHelpers.need_forms(inv) and ItemPlacementHelpers.need_summons(inv)
        else:
            self.logic[START_NODE][NodeId.UnderworldEntrance] = ItemPlacementHelpers.oc1_check
            self.logic[NodeId.Zexion][NodeId.CerberusBonus] = ItemPlacementHelpers.oc2_check
            self.logic[NodeId.Hades][NodeId.PainAndPanicCup] = pain_and_panic_check
            self.logic[NodeId.Hades][NodeId.CerberusCup] = cerberus_cup_check
            self.logic[NodeId.Hydra][NodeId.GoddessOfFateCup] = goddess_of_fate_check
            self.logic[NodeId.Hydra][NodeId.ParadoxCups] = lambda inv: ItemPlacementHelpers.need_forms(inv) and ItemPlacementHelpers.need_summons(inv)

def make_graph(graph: LocationGraphBuilder):
    oc = locationType.OC
    cups = locationType.OCCups
    oc_logic = OCLogicGraph(graph.reverse_rando,graph.keyblades_unlock_chests)
    graph.add_logic(oc_logic)

    passage_chests = graph.add_location(NodeId.PassageChests, [
        chest(7, CheckLocation.PassageMythrilShard, oc),
        chest(8, CheckLocation.PassageMythrilStone, oc),
        chest(144, CheckLocation.PassageEther, oc),
        chest(145, CheckLocation.PassageApBoost, oc),
        chest(146, CheckLocation.PassageHiPotion, oc),
    ])
    passage = graph.add_location(NodeId.Passage, [])
    inner_chamber_chests = graph.add_location(NodeId.InnerChamberChests, [
        chest(2, CheckLocation.InnerChamberUnderworldMap, oc),
        chest(243, CheckLocation.InnerChamberMythrilShard, oc),
    ])
    inner_chamber = graph.add_location(NodeId.InnerChamber, [])
    cerberus_bonus = graph.add_location(NodeId.CerberusBonus, [
        item_bonus(5, CheckLocation.Cerberus, oc, vanilla=ability.Counterguard),
    ])
    coliseum_map_popup = graph.add_location(NodeId.ColiseumMapPopup, [
        popup(338, CheckLocation.ColiseumMap, oc),
    ])
    urns_bonus = graph.add_location(NodeId.UrnsBonus, [
        item_bonus(57, CheckLocation.Urns, oc, vanilla=ability.AerialDive),
    ])
    underworld_entrance_chests = graph.add_location(NodeId.UnderworldEntranceChests, [
        chest(242, CheckLocation.UnderworldEntrancePowerBoost, oc),
    ])
    underworld_entrance = graph.add_location(NodeId.UnderworldEntrance, [])
    caverns_entrance_chests = graph.add_location(NodeId.CavernsEntranceChests, [
        chest(3, CheckLocation.CavernsEntranceLucidShard, oc),
        chest(11, CheckLocation.CavernsEntranceApBoost, oc),
        chest(504, CheckLocation.CavernsEntranceMythrilShard, oc),
    ])
    caverns_entrance = graph.add_location(NodeId.CavernsEntrance, [])
    lost_road_chests = graph.add_location(NodeId.LostRoadChests, [
        chest(9, CheckLocation.LostRoadBrightShard, oc),
        chest(10, CheckLocation.LostRoadEther, oc),
        chest(148, CheckLocation.LostRoadMythrilShard, oc),
        chest(149, CheckLocation.LostRoadMythrilStone, oc),
    ])
    lost_road = graph.add_location(NodeId.LostRoad, [])
    atrium_chests = graph.add_location(NodeId.AtriumChests, [
        chest(150, CheckLocation.AtriumLucidStone, oc),
        chest(151, CheckLocation.AtriumApBoost, oc),
    ])
    atrium = graph.add_location(NodeId.Atrium, [])
    demyx = graph.add_location(NodeId.DemyxOlympusColiseum, [
        stat_bonus(58, CheckLocation.DemyxOlympusColiseum, oc),
        popup(529, CheckLocation.DemyxOcSecretAnsemReport5, oc, vanilla=report.AnsemReport5),
        popup(293, CheckLocation.OlympusStone, oc, vanilla=misc.OlympusStone),
    ])
    lock_chests = graph.add_location(NodeId.TheLockChests, [
        chest(244, CheckLocation.LockCavernsMap, oc),
        chest(5, CheckLocation.LockMythrilShard, oc),
        chest(142, CheckLocation.LockApBoost, oc),
    ])
    lock = graph.add_location(NodeId.TheLock, [])
    pete = graph.add_location(NodeId.PeteOlympusColiseum, [
        item_bonus(6, CheckLocation.PeteOlympusColiseum, oc, vanilla=ability.TrinityLimit),
    ])
    hydra = graph.add_location(NodeId.Hydra, [
        hybrid_bonus(7, CheckLocation.Hydra, oc, vanilla=magic.Thunder),
        popup(260, CheckLocation.HerosCrest, oc, vanilla=keyblade.HerosCrest),
    ])
    aurons_statue = graph.add_location(NodeId.AuronsStatue, [
        popup(295, CheckLocation.AuronssStatue, oc, vanilla=misc.AuronsStatue),
    ])
    hades = graph.add_location(NodeId.Hades, [
        hybrid_bonus(8, CheckLocation.Hades, oc, vanilla=ability.MagnetBurst),
        popup(272, CheckLocation.GuardianSoul, oc, vanilla=keyblade.GuardianSoul),
    ])
    pain_panic_cup = graph.add_location(NodeId.PainAndPanicCup, [
        popup(513, CheckLocation.PainPanicCupProtectBelt, [oc, cups], invalid_checks=[itemType.TROPHY]),
        popup(540, CheckLocation.PainPanicCupSerenityGem, [oc, cups], invalid_checks=[itemType.TROPHY]),
    ])
    cerberus_cup = graph.add_location(NodeId.CerberusCup, [
        popup(515, CheckLocation.CerberusCupRisingDragon, [oc, cups], invalid_checks=[itemType.TROPHY]),
        popup(542, CheckLocation.CerberusCupSerenityCrystal, [oc, cups], invalid_checks=[itemType.TROPHY]),
    ])
    titan_cup = graph.add_location(NodeId.TitanCup, [
        popup(514, CheckLocation.TitanCupGenjiShield, [oc, cups], invalid_checks=[itemType.TROPHY]),
        popup(541, CheckLocation.TitanCupSkillfulRing, [oc, cups], invalid_checks=[itemType.TROPHY]),
    ])
    goddess_of_fate_cup = graph.add_location(NodeId.GoddessOfFateCup, [
        popup(516, CheckLocation.GoddessOfFateCupFatalCrest, [oc, cups], invalid_checks=[itemType.TROPHY],
              vanilla=keyblade.FatalCrest),
        popup(517, CheckLocation.GoddessOfFateCupOrichalcumPlus, [oc, cups], invalid_checks=[itemType.TROPHY]),
    ])
    paradox_cups = graph.add_location(NodeId.ParadoxCups, [
        popup(518, CheckLocation.ParadoxCupsHadesCupTrophy, [oc, locationType.OCParadoxCup],
              invalid_checks=[itemType.TROPHY, itemType.FORM, itemType.SUMMON], vanilla=misc.HadesCupTrophy),
    ])
    zexion = graph.add_location(NodeId.Zexion, [
        stat_bonus(66, CheckLocation.ZexionBonus, [oc, locationType.AS]),
        popup(546, CheckLocation.ZexionBookOfShadows, [oc, locationType.AS]),
    ])
    data_zexion = graph.add_location(NodeId.DataZexion, [
        popup(551, CheckLocation.DataZexionLostIllusion, [oc, locationType.DataOrg]),
    ])

    graph.register_superboss(data_zexion)
    
    graph.add_edge(passage, passage_chests)
    graph.add_edge(inner_chamber, inner_chamber_chests)
    graph.add_edge(underworld_entrance, underworld_entrance_chests)
    graph.add_edge(caverns_entrance, caverns_entrance_chests)
    graph.add_edge(lost_road, lost_road_chests)
    graph.add_edge(atrium, atrium_chests)
    graph.add_edge(lock, lock_chests)

    if not graph.reverse_rando:
        graph.add_edge(START_NODE, passage)
        graph.add_edge(passage, inner_chamber)
        graph.add_edge(inner_chamber, cerberus_bonus, RequirementEdge(battle=True))
        graph.add_edge(cerberus_bonus, coliseum_map_popup)
        graph.add_edge(coliseum_map_popup, urns_bonus)
        graph.add_edge(urns_bonus, underworld_entrance)
        graph.add_edge(underworld_entrance, caverns_entrance)
        graph.add_edge(caverns_entrance, lost_road)
        graph.add_edge(lost_road, atrium)
        graph.add_edge(atrium, demyx, RequirementEdge(battle=True))
        graph.add_edge(demyx, lock)
        graph.add_edge(lock, pete, RequirementEdge(battle=True))
        graph.add_edge(pete, hydra, RequirementEdge(battle=True))
        graph.add_edge(hydra, aurons_statue, RequirementEdge(battle=True))
        graph.add_edge(aurons_statue, hades, RequirementEdge(battle=True))

        graph.add_edge(hydra, pain_panic_cup, RequirementEdge(battle=True))
        graph.add_edge(hydra, cerberus_cup, RequirementEdge(battle=True))
        graph.add_edge(hades, titan_cup, RequirementEdge(battle=True))
        graph.add_edge(hades, goddess_of_fate_cup, RequirementEdge(battle=True))
        graph.add_edge(hades, paradox_cups)
        graph.add_edge(hades, zexion, RequirementEdge(battle=True))
        graph.add_edge(zexion, data_zexion)
        graph.register_first_boss(hydra)
        graph.register_last_story_boss(hades)
        graph.register_superboss(zexion)
    else:
        graph.add_edge(START_NODE, underworld_entrance)
        graph.add_edge(underworld_entrance, passage)
        graph.add_edge(passage, inner_chamber)
        graph.add_edge(inner_chamber, aurons_statue, RequirementEdge(battle=True))
        graph.add_edge(aurons_statue, hades, RequirementEdge(battle=True))
        graph.add_edge(hades, zexion, RequirementEdge(battle=True))
        graph.add_edge(zexion, cerberus_bonus, RequirementEdge(battle=True))
        graph.add_edge(cerberus_bonus, coliseum_map_popup)
        graph.add_edge(coliseum_map_popup, urns_bonus)
        graph.add_edge(urns_bonus, caverns_entrance)
        graph.add_edge(caverns_entrance, lost_road)
        graph.add_edge(lost_road, atrium)
        graph.add_edge(atrium, demyx, RequirementEdge(battle=True))
        graph.add_edge(demyx, lock)
        graph.add_edge(lock, pete, RequirementEdge(battle=True))
        graph.add_edge(pete, hydra, RequirementEdge(battle=True))
        graph.add_edge(hades, pain_panic_cup, RequirementEdge(battle=True))
        graph.add_edge(hades, cerberus_cup, RequirementEdge(battle=True))
        graph.add_edge(hydra, titan_cup, RequirementEdge(battle=True))
        graph.add_edge(hydra, goddess_of_fate_cup, RequirementEdge(battle=True))
        graph.add_edge(hydra, paradox_cups)
        graph.add_edge(hydra, data_zexion, RequirementEdge(battle=True))
        graph.register_first_boss(hades)
        graph.register_last_story_boss(hydra)
