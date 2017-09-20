import App
import Foundation

abbrev = "DS9FXHutet"
iconName = "DS9FXHutet"
longName = "Hutet"
shipFile = "DS9FXHutet"
species = App.SPECIES_GALAXY
menuGroup = "DS9FX Ships"
playerMenuGroup = "DS9FX Ships"

Foundation.ShipDef.DS9FXHutet = Foundation.CardShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.DS9FXHutet.SubMenu = "Cardassian Ships"
Foundation.ShipDef.DS9FXHutet.fMaxWarp = 9.4 + 0.0001
Foundation.ShipDef.DS9FXHutet.fCruiseWarp = 8.9 + 0.0001
Foundation.ShipDef.DS9FXHutet.fCrew = 1500

Foundation.ShipDef.DS9FXHutet.desc = "------- DESCRIPTION -------\nThe Hutet is a huge, powerful ship designed by the Cardassian Union meant to be the flagship.  It is huge, and has slow maneuverability, although its vast weapons array more than makes up for that.  It has multiple pulse torpedo launchers on all sides, except dorsal and ventral; and two spiral wave disruptors as well as many compressor beams that provide excellent coverage.   \n\n------- TACTICS -------\nKeep the ship on a good rotation, making full use of its toredo launchers.  When engaging, stay clear of its torpedo launchers.  Try to be fast and maneuverable, and stay in its blind spots.\n\n------- SHIP STATS -------\n\nHull Rating: 19500\n\nShield Rating:\n     Fore - 11000 @ 9chg\n     Aft - 11000 @ 9chg\n     Dorsal - 11000 @ 9chg\n     Ventral - 11000 @ 9chg\n     Port - 11000 @ 9chg\n     Starboard - 11000 @ 9chg\n\nImpulse Engines:\n     Max Speed - 6\n     Max Accel - 1.9\n     Max Ang Velocity - 0.15\n     Max Ang Accel - 0.15\n\nWarp Engines:\n     Max Warp - 9.4\n     Max Cruise Warp - 8.9\n\nCrew Complement: 1500\n\n------- SHIP WEAPONS -------\n\nCompressor Beams:\n   4xD 2xV 1xSD 1xSV \n   1xPD 1xPV 4xA\n     Max Chg - 1\n     Max Dmg - 750\n     Min Firing Chg - 1\n     Rechg Rate - 0.5\n     Max Damage Distance - 100\n\nSpiral Wave Disruptors:\n   2xF \n     Max Chg - 1\n     Max Dmg - 850\n     Min Firing Chg - 1\n     Rechg Rate - 0.75\n     Max Damage Distance - 100\n\nPulse Torpedoes: \n   5xF 2xA 8xP 8xS \n     Max Chg - 5\n     Max Dmg - 800\n     Min Firing Chg - 1\n     Rechg Rate - 0.1\n     Cooldown Time - 30\n     \n------- SHIP PROPERTIES -------\n\nCompressor Beam Emitters:\n     Max Condition - 1000\n     Repair Complexity - 1 \n     Disabled Percentage - 0.25   \n\nCompressor Beam System:\n     Max Condition System - 3000\n     Repair Complexity - 1 \n     Disabled Percentage - 0.25\n     Normal Power/Sec -  300\n\nHull:\n     Max Condition - 19500\n     Repair Complexity - 1\n     Disabled Percentage - 0\n\nLife Support System:\n     Max Condition - 30000\n     Repair Complexity - 1\n     Disabled Percentage - 0.1\n\nRepair System:\n     Max Condition - 12000\n     Repair Complexity - 2\n     Disabled Percentage - 0.1\n     Maximum Repair Points - 55\n     Repair Teams - 9\n\nSensor Array:\n     Max Condition - 3000\n     Repair Complexity - 1\n     Disabled Percentage - 0.25\n     Normal Power/Sec - 100\n     Max # of Probes - 10\n     Sensor Base Range - 2000\n\nShield Generator:\n     Max Condition - 13000\n     Repair Complexity - 1\n     Disabled Percentage - 0.25\n     Normal Power/Sec - 400\n\nSpiral Wave Disruptor Emitters:\n     Max Condition - 2000\n     Repair Complexity - 1 \n     Disabled Percentage - 0.25  \n\nPulse Torpedo Bays:\n   5xF 2xA 8xS 8xP\n     Max Condition - 2000\n     Repair Complexity - 1\n     Disabled Percentage - 0.25  \n\nPulse Torpedo System:\n     Max Condition System - 2000\n     Repair Complexity - 1 \n     Disabled Percentage - 0.25 \n     Normal Power/Sec - 1\n\nTractor Beam Emitters:\n   2xF 2xA 1xS 1xP\n     Max Condition - 4000\n     Repair Complexity - 4\n     Disabled Percentage - 0.25\n\nTractor Beam System:\n     Max Condition System - 4000\n     Repair Complexity - 4\n     Disabled Percentage - 0.25\n     Normal Power/Sec - 600\n     \nWarp Core:\n     Max Condition - 15000\n     Repair Complexity - 1\n     Disabled Percentage - 0.25\n     Power Output/Sec - 10000\n     Main Battery Limit - 250000\n     Backup Battery Limit - 80000\n     Main Conduit Capacity - 2000\n     Backup Battery Capacity - 200\n\n------- ENGINE PROPERTIES -------\n\nImpulse Engines:\n     Max Condition - 3000\n     Repair Complexity - 1\n     Disabled Percentage - 0.25\n     Normal Power/Sec - 150\n\n   Port Impulse:\n     Max Condition - 3000\n     Repair Complexity - 1\n     Disabled Percentage - 0.25\n\n   Star Impulse:\n     Max Condition - 3000\n     Repair Complexity - 2\n     Disabled Percentage - 0.25\n\nWarp Engines:\n     Max Condition - 4000\n     Repair Complexity - 3\n     Disabled Percentage - 0.25\n\n   Port Warp:\n     Max Condition - 4000\n     Repair Complexity - 3\n     Disabled Percentage - 0.25\n\n   Star Warp:\n     Max Condition - 4000\n     Repair Complexity - 3\n     Disabled Percentage - 0.25"

Foundation.ShipDef.DS9FXHutet.dTechs = {
   "AutoTargeting": {"Phaser": [2,0]}
}

if menuGroup:           Foundation.ShipDef.DS9FXHutet.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DS9FXHutet.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
