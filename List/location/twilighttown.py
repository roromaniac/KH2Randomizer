from enum import Enum

from List.configDict import locationType
from List.inventory import keyblade, ability, report, form, misc
from List.location.graph import DefaultLogicGraph, RequirementEdge, chest, popup, stat_bonus, item_bonus, \
    LocationGraphBuilder, START_NODE
from Module.itemPlacementRestriction import ItemPlacementHelpers


class NodeId(str, Enum):
    OldMansion = "Old Mansion"
    OldMansionChests = "Old Mansion Chests"
    Woods = "Woods"
    WoodsChests = "Woods Chests"
    TramCommon = "Tram Common"
    TramCommonChests = "Tram Common Chests"
    StationFightPopup = "Station Fight Popup"
    CentralStation = "TT Central Station"
    CentralStationChests = "TT Central Station Chests"
    YenSidTower = "Yensid Tower"
    YenSidTowerChests = "Yensid Tower Chests"
    YenSidTowerEntryway = "Yensid Tower Entryway"
    YenSidTowerEntrywayChests = "Yensid Tower Entryway Chests"
    SorcerersLoft = "Sorcerer's Loft"
    SorcerersLoftChests = "Sorcerer's Loft Chests"
    TowerWardrobe = "Tower Wardrobe"
    TowerWardrobeChests = "Tower Wardrobe Chests"
    ValorForm = "Valor Form"
    SeifersTrophy = "Seifer's Trophy"
    LimitForm = "Limit Form"
    UndergroundConcourse = "Underground Concourse"
    UndergroundConcourseChests = "Underground Concourse Chests"
    Tunnelway = "Tunnelway"
    TunnelwayChests = "Tunnelway Chests"
    SunsetTerrace = "TT Sunset Terrace"
    SunsetTerraceChests = "TT Sunset Terrace Chests"
    MansionBonus = "TT Mansion Bonus"
    MansionFoyer = "TT Mansion Foyer"
    MansionFoyerChests = "TT Mansion Foyer Chests"
    MansionDiningRoom = "TT Mansion Dining Room"
    MansionDiningRoomChests = "TT Mansion Dining Room Chests"
    MansionLibrary = "TT Mansion Library"
    MansionLibraryChests = "TT Mansion Library Chests"
    TwilightTownBeam = "TT Beam"
    MansionBasement = "TT Mansion Basement"
    MansionBasementChests = "TT Mansion Basement Chests"
    BetwixtAndBetween = "Betwixt and Between"
    DataAxel = "Data Axel"


class CheckLocation(str, Enum):
    OldMansionPotion = "Old Mansion Potion"
    OldMansionMythrilShard = "Old Mansion Mythril Shard"
    WoodsPotion = "The Woods Potion"
    WoodsMythrilShard = "The Woods Mythril Shard"
    WoodsHiPotion = "The Woods Hi-Potion"
    TramCommonHiPotion = "Tram Common Hi-Potion"
    TramCommonApBoost = "Tram Common AP Boost"
    TramCommonTent = "Tram Common Tent"
    TramCommonMythrilShard1 = "Tram Common Mythril Shard (1)"
    TramCommonPotion1 = "Tram Common Potion (1)"
    TramCommonMythrilShard2 = "Tram Common Mythril Shard (2)"
    TramCommonPotion2 = "Tram Common Potion (2)"
    StationPlazaSecretAnsemReport2 = "Station Plaza Secret Ansem Report 2"
    MunnyPouchMickey = "Munny Pouch (Mickey)"
    CrystalOrb = "Crystal Orb"
    CentralStationTent = "Central Station Tent"
    CentralStationHiPotion = "TT Central Station Hi-Potion"
    CentralStationMythrilShard = "Central Station Mythril Shard"
    TowerPotion = "The Tower Potion"
    TowerHiPotion = "The Tower Hi-Potion"
    TowerEther = "The Tower Ether"
    TowerEntrywayEther = "Tower Entryway Ether"
    TowerEntrywayMythrilShard = "Tower Entryway Mythril Shard"
    SorcerersLoftTowerMap = "Sorcerer's Loft Tower Map"
    TowerWardrobeMythrilStone = "Tower Wardrobe Mythril Stone"
    StarSeeker = "Star Seeker"
    ValorForm = "Valor Form"
    SeifersTrophy = "Seifer´s Trophy"
    Oathkeeper = "Oathkeeper"
    LimitForm = "Limit Form"
    UndergroundConcourseMythrilGem = "Underground Concourse Mythril Gem"
    UndergroundConcourseOrichalcum = "Underground Concourse Orichalcum"
    UndergroundConcourseApBoost = "Underground Concourse AP Boost"
    UndergroundConcourseMythrilCrystal = "Underground Concourse Mythril Crystal"
    TunnelwayOrichalcum = "Tunnelway Orichalcum"
    TunnelwayMythrilCrystal = "Tunnelway Mythril Crystal"
    SunsetTerraceOrichalcumPlus = "Sunset Terrace Orichalcum+"
    SunsetTerraceMythrilShard = "Sunset Terrace Mythril Shard"
    SunsetTerraceMythrilCrystal = "Sunset Terrace Mythril Crystal"
    SunsetTerraceApBoost = "Sunset Terrace AP Boost"
    MansionNobodies = "Mansion Nobodies"
    MansionFoyerMythrilCrystal = "Mansion Foyer Mythril Crystal"
    MansionFoyerMythrilStone = "Mansion Foyer Mythril Stone"
    MansionFoyerSerenityCrystal = "Mansion Foyer Serenity Crystal"
    MansionDiningRoomMythrilCrystal = "Mansion Dining Room Mythril Crystal"
    MansionDiningRoomMythrilStone = "Mansion Dining Room Mythril Stone"
    MansionLibraryOrichalcum = "Mansion Library Orichalcum"
    BeamSecretAnsemReport10 = "Beam Secret Ansem Report 10"
    MansionBasementCorridorUltimateRecipe = "Mansion Basement Corridor Ultimate Recipe"
    BetwixtAndBetween = "Betwixt and Between"
    BetwixtAndBetweenBondOfFlame = "Betwixt and Between Bond of Flame"
    DataAxelMagicBoost = "Axel (Data) Magic Boost"

class TTLogicGraph(DefaultLogicGraph):
    def __init__(self,reverse_rando,keyblade_unlocks):
        DefaultLogicGraph.__init__(self,NodeId)
        keyblade_lambda = lambda inv : not keyblade_unlocks or ItemPlacementHelpers.need_tt_keyblade(inv)
        self.logic[NodeId.OldMansion][NodeId.OldMansionChests] = keyblade_lambda
        self.logic[NodeId.Woods][NodeId.WoodsChests] = keyblade_lambda
        self.logic[NodeId.TramCommon][NodeId.TramCommonChests] = keyblade_lambda
        self.logic[NodeId.CentralStation][NodeId.CentralStationChests] = keyblade_lambda
        self.logic[NodeId.UndergroundConcourse][NodeId.UndergroundConcourseChests] = keyblade_lambda
        self.logic[NodeId.Tunnelway][NodeId.TunnelwayChests] = keyblade_lambda
        self.logic[NodeId.SunsetTerrace][NodeId.SunsetTerraceChests] = keyblade_lambda
        self.logic[NodeId.MansionFoyer][NodeId.MansionFoyerChests] = keyblade_lambda
        self.logic[NodeId.MansionDiningRoom][NodeId.MansionDiningRoomChests] = keyblade_lambda
        self.logic[NodeId.MansionLibrary][NodeId.MansionLibraryChests] = keyblade_lambda
        self.logic[NodeId.MansionBasement][NodeId.MansionBasementChests] = keyblade_lambda
        # making tower checks logically need 3 ice creams to prevent softlocking
        self.logic[NodeId.YenSidTower][NodeId.YenSidTowerChests] = lambda inv: ItemPlacementHelpers.tt3_check(inv) and keyblade_lambda(inv)
        self.logic[NodeId.YenSidTowerEntryway][NodeId.YenSidTowerEntrywayChests] = lambda inv: ItemPlacementHelpers.tt3_check(inv) and keyblade_lambda(inv)
        self.logic[NodeId.SorcerersLoft][NodeId.SorcerersLoftChests] = lambda inv: ItemPlacementHelpers.tt3_check(inv) and keyblade_lambda(inv)
        self.logic[NodeId.TowerWardrobe][NodeId.TowerWardrobeChests] = lambda inv: ItemPlacementHelpers.tt3_check(inv) and keyblade_lambda(inv)
        if not reverse_rando:
            self.logic[START_NODE][NodeId.OldMansion] = ItemPlacementHelpers.tt1_check
            self.logic[NodeId.ValorForm][NodeId.SeifersTrophy] = ItemPlacementHelpers.tt2_check
            self.logic[NodeId.LimitForm][NodeId.UndergroundConcourse] = ItemPlacementHelpers.tt3_check
            self.logic[NodeId.LimitForm][NodeId.MansionBonus] = ItemPlacementHelpers.tt3_check
        else:
            self.logic[START_NODE][NodeId.CentralStation] = ItemPlacementHelpers.tt1_check
            self.logic[NodeId.BetwixtAndBetween][NodeId.SeifersTrophy] = ItemPlacementHelpers.tt2_check
            self.logic[NodeId.LimitForm][NodeId.StationFightPopup] = ItemPlacementHelpers.tt3_check

def make_graph(graph: LocationGraphBuilder):
    tt = locationType.TT
    tt_logic = TTLogicGraph(graph.reverse_rando,graph.keyblades_unlock_chests)
    graph.add_logic(tt_logic)

    old_mansion_chests = graph.add_location(NodeId.OldMansionChests, [
        chest(447, CheckLocation.OldMansionPotion, tt),
        chest(448, CheckLocation.OldMansionMythrilShard, tt),
    ])
    old_mansion = graph.add_location(NodeId.OldMansion, [])
    woods_chests = graph.add_location(NodeId.WoodsChests, [
        chest(442, CheckLocation.WoodsPotion, tt),
        chest(443, CheckLocation.WoodsMythrilShard, tt),
        chest(444, CheckLocation.WoodsHiPotion, tt),
    ])
    woods = graph.add_location(NodeId.Woods, [])
    tram_common_chests = graph.add_location(NodeId.TramCommonChests, [
        chest(420, CheckLocation.TramCommonHiPotion, tt),
        chest(421, CheckLocation.TramCommonApBoost, tt),
        chest(422, CheckLocation.TramCommonTent, tt),
        chest(423, CheckLocation.TramCommonMythrilShard1, tt),
        chest(424, CheckLocation.TramCommonPotion1, tt),
        chest(425, CheckLocation.TramCommonMythrilShard2, tt),
        chest(484, CheckLocation.TramCommonPotion2, tt),
    ])
    tram_common = graph.add_location(NodeId.TramCommon, [])
    station_fight_popup = graph.add_location(NodeId.StationFightPopup, [
        popup(526, CheckLocation.StationPlazaSecretAnsemReport2, tt, vanilla=report.AnsemReport2),
        popup(290, CheckLocation.MunnyPouchMickey, tt, vanilla=misc.MunnyPouchMickey),
        popup(291, CheckLocation.CrystalOrb, tt),
    ])
    central_station_chests = graph.add_location(NodeId.CentralStationChests, [
        chest(431, CheckLocation.CentralStationTent, tt),
        chest(432, CheckLocation.CentralStationHiPotion, tt),
        chest(433, CheckLocation.CentralStationMythrilShard, tt),
    ])
    central_station = graph.add_location(NodeId.CentralStation, [])
    yen_sid_tower_chests = graph.add_location(NodeId.YenSidTowerChests, [
        chest(465, CheckLocation.TowerPotion, tt),
        chest(466, CheckLocation.TowerHiPotion, tt),
        chest(522, CheckLocation.TowerEther, tt),
    ])
    yen_sid_tower = graph.add_location(NodeId.YenSidTower, [])
    yen_sid_tower_entryway_chests = graph.add_location(NodeId.YenSidTowerEntrywayChests, [
        chest(467, CheckLocation.TowerEntrywayEther, tt),
        chest(468, CheckLocation.TowerEntrywayMythrilShard, tt),
    ])
    yen_sid_tower_entryway = graph.add_location(NodeId.YenSidTowerEntryway, [])
    sorcerers_loft_chests = graph.add_location(NodeId.SorcerersLoftChests, [
        chest(469, CheckLocation.SorcerersLoftTowerMap, tt),
    ])
    sorcerers_loft = graph.add_location(NodeId.SorcerersLoft, [])
    tower_wardrobe_chests = graph.add_location(NodeId.TowerWardrobeChests, [
        chest(470, CheckLocation.TowerWardrobeMythrilStone, tt),
    ])
    tower_wardrobe = graph.add_location(NodeId.TowerWardrobe, [])
    valor_form = graph.add_location(NodeId.ValorForm, [
        popup(304, CheckLocation.StarSeeker, tt, vanilla=keyblade.StarSeeker),
        popup(286, CheckLocation.ValorForm, tt, vanilla=form.ValorForm),
    ])
    seifers_trophy = graph.add_location(NodeId.SeifersTrophy, [
        popup(294, CheckLocation.SeifersTrophy, tt, vanilla=misc.SeifersTrophy),
    ])
    limit_form = graph.add_location(NodeId.LimitForm, [
        popup(265, CheckLocation.Oathkeeper, tt, vanilla=keyblade.Oathkeeper),
        popup(543, CheckLocation.LimitForm, tt, vanilla=form.LimitForm),
    ])
    underground_concourse_chests = graph.add_location(NodeId.UndergroundConcourseChests, [
        chest(479, CheckLocation.UndergroundConcourseMythrilGem, tt),
        chest(480, CheckLocation.UndergroundConcourseOrichalcum, tt),
        chest(481, CheckLocation.UndergroundConcourseApBoost, tt),
        chest(482, CheckLocation.UndergroundConcourseMythrilCrystal, tt),
    ])
    underground_concourse = graph.add_location(NodeId.UndergroundConcourse, [])
    tunnelway_chests = graph.add_location(NodeId.TunnelwayChests, [
        chest(477, CheckLocation.TunnelwayOrichalcum, tt),
        chest(478, CheckLocation.TunnelwayMythrilCrystal, tt),
    ])
    tunnelway = graph.add_location(NodeId.Tunnelway, [])
    sunset_terrace_chests = graph.add_location(NodeId.SunsetTerraceChests, [
        chest(438, CheckLocation.SunsetTerraceOrichalcumPlus, tt),
        chest(439, CheckLocation.SunsetTerraceMythrilShard, tt),
        chest(440, CheckLocation.SunsetTerraceMythrilCrystal, tt),
        chest(441, CheckLocation.SunsetTerraceApBoost, tt),
    ])
    sunset_terrace = graph.add_location(NodeId.SunsetTerrace, [])
    mansion_bonus = graph.add_location(NodeId.MansionBonus, [
        stat_bonus(56, CheckLocation.MansionNobodies, tt),
    ])
    mansion_foyer_chests = graph.add_location(NodeId.MansionFoyerChests, [
        chest(452, CheckLocation.MansionFoyerMythrilCrystal, tt),
        chest(453, CheckLocation.MansionFoyerMythrilStone, tt),
        chest(454, CheckLocation.MansionFoyerSerenityCrystal, tt),
    ])
    mansion_foyer = graph.add_location(NodeId.MansionFoyer, [])
    mansion_dining_room_chests = graph.add_location(NodeId.MansionDiningRoomChests, [
        chest(457, CheckLocation.MansionDiningRoomMythrilCrystal, tt),
        chest(458, CheckLocation.MansionDiningRoomMythrilStone, tt),
    ])
    mansion_dining_room = graph.add_location(NodeId.MansionDiningRoom, [])
    mansion_library_chests = graph.add_location(NodeId.MansionLibraryChests, [
        chest(460, CheckLocation.MansionLibraryOrichalcum, tt),
    ])
    mansion_library = graph.add_location(NodeId.MansionLibrary, [])
    beam = graph.add_location(NodeId.TwilightTownBeam, [
        popup(534, CheckLocation.BeamSecretAnsemReport10, tt, vanilla=report.AnsemReport10),
    ])
    mansion_basement_chests = graph.add_location(NodeId.MansionBasementChests, [
        chest(464, CheckLocation.MansionBasementCorridorUltimateRecipe, tt),
    ])
    mansion_basement = graph.add_location(NodeId.MansionBasement, [])
    betwixt_and_between = graph.add_location(NodeId.BetwixtAndBetween, [
        item_bonus(63, CheckLocation.BetwixtAndBetween, tt, vanilla=ability.Slapshot),
        popup(317, CheckLocation.BetwixtAndBetweenBondOfFlame, tt, vanilla=keyblade.BondOfFlame),
    ])
    data_axel = graph.add_location(NodeId.DataAxel, [
        popup(561, CheckLocation.DataAxelMagicBoost, [tt, locationType.DataOrg]),
    ])

    graph.register_superboss(data_axel)
    
    graph.add_edge(old_mansion, old_mansion_chests)
    graph.add_edge(woods, woods_chests)
    graph.add_edge(tram_common, tram_common_chests)
    graph.add_edge(central_station, central_station_chests)
    graph.add_edge(yen_sid_tower, yen_sid_tower_chests)
    graph.add_edge(yen_sid_tower_entryway, yen_sid_tower_entryway_chests)
    graph.add_edge(sorcerers_loft, sorcerers_loft_chests)
    graph.add_edge(tower_wardrobe, tower_wardrobe_chests)
    graph.add_edge(underground_concourse, underground_concourse_chests)
    graph.add_edge(tunnelway, tunnelway_chests)
    graph.add_edge(sunset_terrace, sunset_terrace_chests)
    graph.add_edge(mansion_foyer, mansion_foyer_chests)
    graph.add_edge(mansion_dining_room, mansion_dining_room_chests)
    graph.add_edge(mansion_library, mansion_library_chests)
    graph.add_edge(mansion_basement, mansion_basement_chests)

    if not graph.reverse_rando:
        graph.add_edge(START_NODE, old_mansion)
        graph.add_edge(old_mansion, tram_common)
        graph.add_edge(tram_common, woods)
        graph.add_edge(tram_common, station_fight_popup, RequirementEdge(battle=True))
        graph.add_edge(station_fight_popup, central_station)
        graph.add_edge(central_station, yen_sid_tower)
        graph.add_edge(yen_sid_tower, yen_sid_tower_entryway)
        graph.add_edge(yen_sid_tower_entryway, sorcerers_loft, RequirementEdge(battle=True))
        graph.add_edge(sorcerers_loft, tower_wardrobe)
        graph.add_edge(tower_wardrobe, valor_form)
        graph.add_edge(valor_form, seifers_trophy, RequirementEdge(battle=True))
        graph.add_edge(seifers_trophy, limit_form)
        graph.add_edge(limit_form, underground_concourse)
        graph.add_edge(underground_concourse, tunnelway)
        graph.add_edge(tunnelway, sunset_terrace)
        graph.add_edge(limit_form, mansion_bonus, RequirementEdge(battle=True))
        graph.add_edge(mansion_bonus, mansion_foyer)
        graph.add_edge(mansion_foyer, mansion_dining_room)
        graph.add_edge(mansion_foyer, mansion_library)
        graph.add_edge(mansion_foyer, beam)
        graph.add_edge(mansion_foyer, mansion_basement)
        graph.add_edge(beam, betwixt_and_between, RequirementEdge(battle=True))
        graph.add_edge(betwixt_and_between, data_axel, RequirementEdge(battle=True))
        graph.register_first_boss(valor_form)
        graph.register_last_story_boss(betwixt_and_between)
    else:
        graph.add_edge(START_NODE, central_station)
        graph.add_edge(central_station, underground_concourse)
        graph.add_edge(central_station, tram_common)
        graph.add_edge(tram_common, woods)
        graph.add_edge(underground_concourse, tunnelway)
        graph.add_edge(tunnelway, sunset_terrace)
        graph.add_edge(woods, mansion_bonus, RequirementEdge(battle=True))
        graph.add_edge(mansion_bonus, old_mansion)
        graph.add_edge(mansion_bonus, mansion_foyer)
        graph.add_edge(mansion_foyer, mansion_dining_room)
        graph.add_edge(mansion_foyer, mansion_library)
        graph.add_edge(mansion_foyer, beam)
        graph.add_edge(mansion_foyer, mansion_basement)
        graph.add_edge(beam, betwixt_and_between, RequirementEdge(battle=True))
        graph.add_edge(betwixt_and_between, seifers_trophy,RequirementEdge(battle=True))
        graph.add_edge(seifers_trophy, limit_form)
        graph.add_edge(limit_form, station_fight_popup,RequirementEdge(battle=True))
        graph.add_edge(station_fight_popup, yen_sid_tower)
        graph.add_edge(yen_sid_tower, yen_sid_tower_entryway)
        graph.add_edge(yen_sid_tower_entryway, sorcerers_loft, RequirementEdge(battle=True))
        graph.add_edge(sorcerers_loft, tower_wardrobe)
        graph.add_edge(tower_wardrobe, valor_form)
        graph.add_edge(valor_form, data_axel, RequirementEdge(battle=True))
        graph.register_first_boss(betwixt_and_between)
        graph.register_last_story_boss(valor_form)
