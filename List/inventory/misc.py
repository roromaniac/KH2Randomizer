from dataclasses import dataclass

from List.configDict import itemType
from List.inventory.item import InventoryItem


@dataclass(frozen=True)
class MiscItem(InventoryItem):
    id: int
    name: str
    type: itemType


NullItem = MiscItem(0, "", itemType.SYNTH)
TornPages = MiscItem(32, "Torn Pages", itemType.TORN_PAGE)
MunnyPouchOlette = MiscItem(362, "Munny Pouch", itemType.MUNNY_POUCH)
ObjectiveItem = MiscItem(363, "Objective Completion Item", itemType.OBJECTIVE) # previously crystal orb
EmblemItem = MiscItem(363, "Emblem", itemType.OBJECTIVE) # previously crystal orb
SeifersTrophy = MiscItem(364, "Seifer's Trophy", itemType.KEYITEM)
Poster = MiscItem(366, "Poster", itemType.KEYITEM)
OlympusStone = MiscItem(370, "Olympus Stone", itemType.OCSTONE)
AuronsStatue = MiscItem(371, "Auron's Statue", itemType.KEYITEM)
CursedMedallion = MiscItem(372, "Cursed Medallion", itemType.KEYITEM)
Present = MiscItem(373, "Presents", itemType.KEYITEM)
DecoyPresents = MiscItem(374, "Decoy Presents", itemType.KEYITEM)
ObjectiveReport = MiscItem(239, "Objective Report", itemType.KEYITEM)
UnknownDisk = MiscItem(462, "Unknown Disk", itemType.MANUFACTORYUNLOCK)  # Dummy 15
PromiseCharm = MiscItem(524, "PromiseCharm", itemType.PROMISE_CHARM)
MunnyPouchMickey = MiscItem(535, "Munny Pouch", itemType.MUNNY_POUCH)
HadesCupTrophy = MiscItem(537, "Hades Cup Trophy", itemType.TROPHY)
StruggleTrophy = MiscItem(538, '"The Struggle" Trophy', itemType.KEYITEM)
MiningPermit = MiscItem(459, "Mining Permit", itemType.MININGPERMIT)  # Dummy 12
