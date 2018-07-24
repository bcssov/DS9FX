# Handles enable\disable local forces

import App
import MissionLib
from Custom.DS9FX import DS9FXmain
from Custom.DS9FX.DS9FXMissions import MissionIDs
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig

ships = ["Attacker 1", "Attacker 2", "Attacker 3", "Attacker 4", "Attacker 5",
         "USS Excalibur", "USS Defiant", "USS Oregon", "USS_Lakota", "Verde", "Guadiana", "Lankin",
         "Maroni", "Kuban", "Paraguay", "Tigris", "Dreadnought", "Bugship 1", "Bugship 2", "Bugship 3",
         "Bugship Patrol 1", "Bugship Patrol 2",
         "Bugship Patrol 3", "Bugship Patrol 4",
         "Bugship Patrol 5", "Bugship Patrol 6", "Bugship Patrol 7", "Bugship Patrol 8", "Bugship Patrol 9",
         "Bugship Patrol 10", "Bugship Patrol 11", "Dreadnought 1", "Dreadnought 2", "Bugship 1", "Bugship 2",
         "Bugship 3", "Bugship 4", "Dreadnought", "USS Majestic", "USS Bonchune", "Bugship 1", "Bugship 2", "Bugship 3",
         "IKS K'mpec", "IKS Amar", "IKS Ki'Tang", "Hutet 1", "Keldon 1", "Keldon 2", "Galor 1", "Galor 2"]

mission_id = ""

excludedShips = {MissionIDs.MM5: ["Dreadnought"]}


def ShouldEnforceLocalForces():
    global mission_id
    return mission_id != ""


def DisableForces(missionId):
    reload(DS9FXSavedConfig)
    if DS9FXSavedConfig.DisableLocalForces == 0:
        return

    global mission_id
    mission_id = missionId

    pSequence = App.TGSequence_Create()
    pAction = App.TGScriptAction_Create(__name__, "DisableDelay")
    # 10 second delay, to ensure it's executed last
    pSequence.AddAction(pAction, None, 10)
    pSequence.Play()


def DisableDelay(pAction):
    player = MissionLib.GetPlayer()
    if not player:
        return 0

    set = player.GetContainingSet()
    if not set:
        return 0

    set_name = set.GetName()
    if not set_name:
        return 0

    toIgnore = []
    if excludedShips.has_key(set_name):
        toIgnore = excludedShips[set_name]

    for ship in ships:
        if not ship in toIgnore:
            try:
                set.DeleteObjectFromSet(ship)
            except:
                pass

    return 1


def EnableForces(missionId):
    reload(DS9FXSavedConfig)
    if DS9FXSavedConfig.DisableLocalForces == 0:
        return

    global mission_id
    # No need to handle mission end, reset global string
    mission_id = ""

    pSequence = App.TGSequence_Create()
    pAction = App.TGScriptAction_Create(__name__, "EnableDelay")
    # 10 second delay, to ensure it's executed last
    pSequence.AddAction(pAction, None, 10)
    pSequence.Play()


def EnableDelay(pAction):
    player = MissionLib.GetPlayer()
    if not player:
        return 0

    set = player.GetContainingSet()
    if not set:
        return 0

    set_name = set.GetName()
    if not set_name:
        return 0

    DS9FXmain.CreateDS9FXShips()

    return 1
