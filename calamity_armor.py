class Armor:
    def __init__(self, set_identifier, name, defense, damage, crit, movement, melee_damage, melee_crit, melee_speed, ranged_damage, ranged_crit, 
                 magic_damage, magic_crit, mana, summon_damage, minion_slots, ability, set_bonus):
        self.set_identifier = set_identifier
        self.name = name
        self.defense = defense
        self.damage = damage
        self.crit = crit
        self.movement = movement
        self.melee_damage = melee_damage
        self.melee_crit = melee_crit
        self.melee_speed = melee_speed
        self.ranged_damage = ranged_damage
        self.ranged_crit = ranged_crit
        self.magic_damage = magic_damage
        self.magic_crit = magic_crit
        self.mana = mana
        self.summon_damage = summon_damage
        self.minion_slots = minion_slots
        self.ability = ability     # As a string
        self.set_bonus = set_bonus      # Set bonuses linked to a specific piece of armor will be put here (i.e. the beetle scale mail gives a different set bonus than the beetle shell)


class MiningSet:
    helmets = [Armor(0, 'Mining Helmet', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Provides light when worn', None), Armor(0, 'Ultrabright Helmet', 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Improves vivsion and provides light when worn', None)]
    chestplates = [Armor(0, 'Mining Shirt', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '10% increased mining speed', None)]
    leggings = Armor(0, 'Mining Pants', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '10% increased mining speed', None)
    set_bonus = Armor(0, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '10% increased mining speed', None)
    stage = 'Pre-Boss'

class WoodSet:
    helmets = [Armor(2, 'Wood Helmet', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(2, 'Wood Breastplate', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(2, 'Wood Greaves', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(2, '', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    stage = 'Pre-Boss'

class MahoganySet:
    helmets = [Armor(3, 'Rich Mahogany Helmet', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(3, 'Rich Mahogany Breastplate', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(3, 'Rich Mahogany Greaves', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(3, '', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    stage = 'Pre-Boss'

class BorealSet:
    helmets = [Armor(4, 'Boreal Wood Helmet', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(4, 'Boreal Wood Breastplate', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(4, 'Boreal Wood Greaves', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(4, '', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    stage = 'Pre-Boss'

class PalmSet:
    helmets = [Armor(5, 'Palm Wood Helmet', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(5, 'Palm Wood Breastplate', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(5, 'Palm Wood Greaves', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(5, '', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    stage = 'Pre-Boss'

class EbonwoodSet:
    helmets = [Armor(6, 'Ebonwood Helmet', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(6, 'Ebonwood Breastplate', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(6, 'Ebonwood Greaves', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(6, '', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    stage = 'Pre-Boss'

class ShadewoodSet:
    helmets = [Armor(7, 'Shadewood Helmet', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(7, 'Shadewod Breastplate', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(7, 'Shadewood Greaves', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(7, '', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    stage = 'Pre-Boss'

class AshWoodSet:
    helmets = [Armor(8, 'Ash Wood Helmet', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(8, 'Ash Wood Breastplate', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(8, 'Ash Wood Greaves', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(8, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    stage = 'Pre-Boss'

class RainSet:
    helmets = [Armor(9, 'Rain Hat', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(9, 'Rain Coat', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    set_bonus = Armor(9, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    stage = 'Pre-Boss'

class SnowSet:
    helmets = [Armor(10, 'Snow Hood', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(10, 'Snow Coat', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(10, 'Snow Pants', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(10, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Cannot be frozen or chilled', None)
    stage = 'Pre-Boss'

class PinkSnowSet:
    helmets = [Armor(11, 'Pink Snow Hood', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(11, 'Pink Snow Coat', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(11, 'Pink Snow Pants', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(11, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Cannot be frozen or chilled',  None)
    stage = 'Pre-Boss'

class AnglerSet:
    helmets = [Armor(12, 'Angler Hat', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Increases fishing power by 5', None)]
    chestplates = [Armor(12, 'Angler Vest', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Increases fishing power by 5', None)]
    leggings = Armor(12, 'Angler Pants', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Increases fishing power by 5', None)
    set_bonus = Armor(12, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Decreased enemy spawn rate', None)
    stage = 'Pre-Boss'

class CactusSet:
    helmets = [Armor(13, 'Cactus Helmet', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(13, 'Cactus Breastplate', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(13, 'Cactus Leggings', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(13, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Attackers take damage from the cactus spikes', None)
    stage = 'Pre-Boss'

class CopperSet:
    helmets = [Armor(14, 'Copper Helmet', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(14, 'Copper Chainmail', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(14, 'Copper Greaves', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(14, '', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    stage = 'Pre-Boss'

class TinSet:
    helmets = [Armor(15, 'Tin Helmet', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(15, 'Tin Chainmail', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(15, 'Tin Greaves', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(15, '', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    stage = 'Pre-Boss'

class PumpkinSet:
    helmets = [Armor(16, 'Pumpkin Helmet', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(16, 'Pumpkin Breastplate', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(16, 'Pumpkin Greaves', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(16, '', 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    stage = 'Pre-Boss'

class NinjaSet:
    helmets = [Armor(17, 'Ninja Hood', 2, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(17, 'Ninja Shirt', 4, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(17, 'Ninja Pants', 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(17, '', 0, 0, 0, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    stage = 'Pre-Brain of Cthulhu/Eater of Worlds'

class IronSet:
    helmets = [Armor(18, 'Iron Helmet', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(18, 'Iron Chainmail', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(18, 'Iron Greaves', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(18, '', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    stage = 'Pre-Boss'
   
class LeadSet:
    helmets = [Armor(19, 'Lead Helmet', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(19, 'Lead Chainmail', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(19, 'Lead Greaves', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(19, '', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    stage = 'Pre-Boss' 

class SilverSet:
    helmets = [Armor(20, 'Silver Helmet', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(20, 'Silver Chainmail', 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(20, 'Silver Greaves', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(20, '', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    stage = 'Pre-Boss'

class TungstenSet:
    helmets = [Armor(21, 'Tungsten Helmet', 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(21, 'Tungsten Chainmail', 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(21, 'Tungsten Greaves', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(21, '', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    stage = 'Pre-Boss'

class GoldSet:
    helmets = [Armor(22, 'Gold Helmet', 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(22, 'Gold Chainmail', 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(22, 'Gold Greaves', 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '',  None)
    set_bonus = Armor(22, '', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    stage = 'Pre-Boss'

class PlatinumSet:
    helmets = [Armor(23, 'Platinum Helmet', 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(23, 'Platinum Chainmail', 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(23, 'Platinum Greaves', 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(23, '', 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    stage = 'Pre-Boss'

class FossilSet:
    helmets = [Armor(24, 'Fossil Helmet', 4, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(24, 'Fossil Plate', 5, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(24, 'Fossil Greaves', 4, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(24, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '20% chance to save ammo', None)
    stage = 'Pre-Boss'

class BeeSet:
    helmets = [Armor(25, 'Bee Headgear', 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 1, '', None)]
    chestplates = [Armor(25, 'Bee Breastplate', 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 1, '', None)]
    leggings = Armor(25, 'Bee Greaves', 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, '', None)
    set_bonus = Armor(25, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, '', None)
    stage = 'Pre-Brain of Cthulhu/Eater of Worlds'

class ObsidianSet:
    helmets = [Armor(26, 'Obsidian Outlaw Hat', 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, '', None)]
    chestplates = [Armor(26, 'Obsidian Longcoat', 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, '', None)]
    leggings = Armor(26, 'Obsidian Pants', 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, '', None)
    set_bonus = Armor(26, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 'Increases whip range by 30%', None)
    stage = 'Pre-Skeletron'

class GladiatorSet:
    helmets = [Armor(27, 'Gladiator Helmet', 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(27, 'Gladiator Breastplate', 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(27, 'Gladiator Leggings', 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(27, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Grants immunity to knockback', None)
    stage = 'Pre-Boss'

class MeteorSet:
    helmets = [Armor(28, 'Meteor Helmet', 5, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(28, 'Meteor Suit', 6, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, '', None)]
    leggings = Armor(28, 'Meteor Leggings', 5, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, '', None)
    set_bonus = Armor(28, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Space Gun costs 0 mana', None)
    stage = 'Pre-Skeletron'

class JungleSet:
    helmets = [Armor(29, 'Jungle Hat', 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 40, 0, 0, '', None)]
    chestplates = [Armor(29, 'Jungle Shirt', 6, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 20, 0, 0, '', None)]
    leggings = Armor(29, 'Jungle Pants', 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 20, 0, 0, '', None)
    set_bonus = Armor(29, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '16% reduced mana costs', None)
    stage = 'Pre-Boss'

class AncientCobaltSet:
    helmets = [Armor(30, 'Ancient Cobalt Helmet', 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 40, 0, 0, '', None)]
    chestplates = [Armor(30, 'Ancient Cobalt Breastplate', 6, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 20, 0, 0, '', None)]
    leggings = Armor(30, 'Ancient Cobalt Leggings', 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 20, 0, 0, '', None)
    set_bonus = Armor(30, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '16% reduced mana costs', None)
    stage = 'Pre-Boss'

class NecroSet:
    helmets = [Armor(31, 'Necro Helmet', 6, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(31, 'Necro Breastplate', 7, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(31, 'Necro Greaves', 6, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(31, '', 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, '', None)
    stage = 'Pre-Wall of Flesh'

class ShadowSet:
    helmets = [Armor(32, 'Shadow Helmet', 6, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(32, 'Shadow Scalemail', 7, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(32, 'Shadow Greaves', 6, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(32, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '75% increase to player acceleration and 1.15x player max movement speed', None)
    stage = 'Pre-Skeletron'

class AncientShadowSet:
    helmets = [Armor(33, 'Ancient Shadow Helmet', 6, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(33, 'Ancient Shadow Scalemail', 7, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(33, 'Ancient Shadow Greaves', 6, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(33, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '75% increase to player acceleration and 1.15x player max movement speed', None)
    stage = 'Pre-Boss'

class CrimsonSet:
    helmets = [Armor(34, 'Crimson Helmet', 6, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(34, 'Crimson Scalemail', 7, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(34, 'Crimsow Greaves', 6, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(34, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Greatly increased life regen', None)
    stage = 'Pre-Skeletron'

class MoltenSet:
    helmets = [Armor(35, 'Molten Helmet', 8, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(35, 'Molten Breastplate', 9, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(35, 'Molten Greaves', 8, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(35, '', 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Cannot be set on fire', None)
    stage = 'Pre-Skeletron'

class PearlwoodSet:
    helmets = [Armor(36, 'Pearlwood Helmet', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(36, 'Pearlwood Breastplate', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(36, 'Pearlwood Greaves', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(36, '', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    stage = 'Pre-Mech Bosses'

class SpiderSet:
    helmets = [Armor(37, 'Spider Mask', 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1, '', None)]
    chestplates = [Armor(37, 'Spider Breastplate', 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1, '', None)]
    leggings = Armor(37, 'Spider Greaves', 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 1, '', None)
    set_bonus = Armor(37, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 0, '', None)
    stage = 'Pre-Mech Bosses'

class CobaltSet:
    helmets = [Armor(38, 'Cobalt Helmet', 14, 0, 0, 10, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', set_bonus = Armor(38, '', 0, 0, 0, 0, 0, 0, 15, 0, 0, 0, 0, 0, 0, 0, '', None)), Armor(38, 'Cobalt Mask', 5, 0, 0, 0, 0, 0, 0, 10, 10, 0, 0, 0, 0, 0, '', set_bonus = Armor(38, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '20% chance to save ammo', None)), Armor(38, 'Cobalt Hat', 3, 0, 0, 0, 0, 0, 0, 0, 0, 10, 9, 40, 0, 0, '', set_bonus = Armor(40, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '14% reduced mana costs', None))]
    chestplates = [Armor(38, 'Cobalt Breastplate', 10, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(38, 'Cobalt Leggings', 8, 3, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = None
    stage = 'Pre-Mech Bosses'

class PalladiumSet:
    helmets = [Armor(41, 'Palladium Mask', 14, 0, 0, 0, 12, 0, 12, 0, 0, 0, 0, 0, 0, 0, '', None), Armor(41, 'Palladium Helmet', 5, 0, 0, 0, 0, 0, 0, 9, 9, 0, 0, 0, 0, 0, '', None), Armor(41, 'Palladium Headgear', 3, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 60, 0, 0, '', None)]
    chestplates = [Armor(41, 'Palladium Breastplate', 10, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(41, 'Palladium Leggings', 8, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(41, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Greatly increases life regeneration after striking an enemy', None)
    stage = 'Pre-Mech Bosses'

class MythrilSet:
    helmets = [Armor(44, 'Mythril Helmet', 16, 0, 0, 0, 10, 8, 0, 0, 0, 0, 0, 0, 0, 0, '', set_bonus = Armor(44, '', 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, '', None)), Armor(44, 'Mythril Hat', 6, 0, 0, 0, 0, 0, 0, 12, 7, 0, 0, 0, 0, 0, '',  set_bonus = Armor(44, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '20% chance to save ammo', None)), Armor(44, 'Mythril Hood', 3, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 60, 0, 0, '',  set_bonus = Armor(44, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '17% reduced mana costs', None))]
    chestplates = [Armor(44, 'Mythril Chainmail', 12, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(44, 'Mythril Greaves', 9, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = None
    stage = 'Pre-Mech Bosses'

class OrichalcumSet:
    helmets = [Armor(47, 'Orichalcum Mask', 19, 0, 0, 7, 11, 0, 11, 0, 0, 0, 0, 0, 0, 0, '', None), Armor(47, 'Orichalcum Helmet', 7, 0, 0, 8, 0, 0, 0, 0, 15, 0, 0, 0, 0, 0, '', None), Armor(47, 'Orichalcum Headgear', 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 18, 80, 0, 0, '', None)]
    chestplates = [Armor(47, 'Orichalcum Breastplate', 13, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(47, 'Orichalcum Leggings', 10, 8, 0, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(47, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Flower petals will fall on your target for extra damage', None)
    stage = 'Pre-Mech Bosses'

class AdamantiteSet:
    helmets = [Armor(50, 'Adamantite Helmet', 22, 0, 0, 0, 14, 7, 0, 0, 0, 0, 0, 0, 0, 0, '', set_bonus = Armor(50, '', 0, 0, 0, 20, 0, 0, 20, 0, 0, 0, 0, 0, 0, 0, '', None)), Armor(50, 'Adamantite Mask', 8, 0, 0, 0, 0, 0, 0, 14, 10, 0, 0, 0, 0, 0, '', set_bonus = Armor(50, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '25% chance to save ammo', None)), Armor(50, 'Adamantite Headgear', 4, 0, 0, 0, 0, 0, 0, 0, 0, 12, 12, 80, 0, 0, '', set_bonus = Armor(50, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '19% reduced mana costs', None))]
    chestplates = [Armor(50, 'Adamantite Breastplate', 16, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(50, 'Adamantite Leggings', 12, 0, 7, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = None
    stage = 'Pre-Mech Bosses'

class TitaniumSet:
    helmets = [Armor(53, 'Titanium Mask', 23, 0, 0, 0, 9, 9, 9, 0, 0, 0, 0, 0, 0, 0, '', None), Armor(53, 'Titanium Helmet', 8, 0, 0, 0, 0, 0, 0, 16, 7, 0, 0, 0, 0, 0, '', None), Armor(53, 'Titanium Headgear', 4, 0, 0, 0, 0, 0, 0, 0, 0, 16, 7, 100, 0, 0, '', None)]
    chestplates = [Armor(53, 'Titanium Breastplate', 15, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(53, 'Titanium Leggings', 11, 3, 3, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(53, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Attacking generates a defensive barrier of titanium shards', None)
    stage = 'Pre-Mech Bosses'

class CrystalAssassinSet:
    helmets = [Armor(56, 'Crystal Assassin Hood', 12, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '10% reduced mana cost', None)]
    chestplates = [Armor(56, 'Crystal Assassin Shirt', 14, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '10% chance to save ammo', None)]
    leggings = Armor(56, 'Crystal Assassin Pants', 10, 0, 0, 20, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(56, '', 0, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Allows the ability to dash', None)
    stage = 'Pre-Mech Bosses'

class FrostSet:
    helmets = [Armor(57, 'Frost Helmet', 10, 0, 0, 0, 16, 0, 0, 16, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(57, 'Frost Breastplate', 20, 0, 0, 0, 0, 11, 0, 0, 11, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(57, 'Frost Leggings', 13, 0, 0, 8, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(57, '', 0, 0, 0, 0, 10, 0, 0, 10, 0, 0, 0, 0, 0, 0, 'Melee and ranged attacks cause frostburn', None)
    stage = 'Pre-Mech Bosses'

class ForbiddenSet:
    helmets = [Armor(58, 'Forbidden Mask', 6, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 0, 15, 0, '', None)]
    chestplates = [Armor(58, 'Forbidden Robes', 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 40, 10, 1, '', None)]
    leggings = Armor(58, 'Forbidden Treads', 8, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 40, 0, 1, '', None)
    set_bonus = Armor(58, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Double tap to call an ancient storm to cursor location', None)
    stage = 'Pre-Mech Bosses'

class SquireSet:
    helmets = [Armor(59, "Squire's Great Helm", 13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 'Increases your life regeneration', None)]
    chestplates = [Armor(59, "Squire's Plating", 27, 0, 0, 0, 15, 0, 0, 0, 0, 0, 0, 0, 15, 0, '', None)]
    leggings = Armor(59, "Squire's Greaves", 18, 0, 0, 15, 0, 15, 0, 0, 0, 0, 0, 0, 15, 0, '', None)
    set_bonus = Armor(59, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 'Ballista pierces more targets and panics when you take damage', None)
    stage = 'Pre-Plantera'

class MonkSet:
    helmets = [Armor(60, "Monk's Bushy Brow Bald Cap", 8, 0, 0, 0, 0, 0, 20, 0, 0, 0, 0, 0, 0, 1, '', None)]
    chestplates = [Armor(60, "Monk's Shirt", 22, 0, 0, 0, 20, 0, 0, 0, 0, 0, 0, 0, 20, 0, '', None)]
    leggings = Armor(60, "Monk's Pants", 16, 0, 0, 20, 0, 15, 0, 0, 0, 0, 0, 0, 10, 0, '', None)
    set_bonus = Armor(60, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 'Lightning Aura can now crit and strikes faster', None)
    stage = 'Pre-Plantera'

class HuntressSet:
    helmets = [Armor(61, "Huntress's Wig", 7, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 1, '', None)]
    chestplates = [Armor(61, "Huntress's Jerkin", 17, 0, 0, 0, 0, 0, 0, 20, 0, 0, 0, 0, 20, 0, '10% chance to save ammo', None)]
    leggings = Armor(61, "Huntress's Pants", 12, 0, 0, 20, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, '', None)
    set_bonus = Armor(61, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 'Explosive Traps recharge faster and oil enemies\nSet oiled enemies on fire for extrs damage', None)
    stage = 'Pre-Plantera'

class ApprenticeSet:
    helmets = [Armor(62, "Apprentice's Hat", 7, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 1, '10% reduced mana cost', None)]
    chestplates = [Armor(62, "Apprentice's Robe", 15, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 20, 0, '', None)]
    leggings = Armor(62, "Apprentice's Trousers", 10, 0, 0, 20, 0, 0, 0, 0, 0, 0, 20, 0, 10, 0, '', None)
    set_bonus = Armor(62, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 'FLameburst field of view and range are dramatically increased', None)
    stage = 'Pre-Plantera'

class HallowedSet:
    helmets = [Armor(63, 'Hallowed Mask', 24, 0, 0, 0, 10, 10, 10, 0, 0, 0, 0, 0, 0, 0, '', None), Armor(63, 'Hallowed Helmet', 9, 0, 0, 0, 0, 0, 0, 15, 8, 0, 0, 0, 0, 0, '', None), Armor(63, 'Hallowed Headgear', 5, 0, 0, 0, 0, 0, 0, 0, 0, 12, 12, 100, 0, 0, '', None), Armor(63, 'Hallowed Hood', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 1, '', set_bonus = Armor(66, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, '',  None))]
    chestplates = [Armor(63, 'Hallowed Plate Mail', 15, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(63, 'Hallowed Greaves', 11, 7, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(63, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Become immune after striking an enemy', None)
    stage = 'Pre-Mech Bosses'

class ChlorophyteSet:
    helmets = [Armor(67, 'Chlorophyte Mask', 20, 0, 0, 0, 16, 6, 0, 0, 0, 0, 0, 0, 0, 0, '', None), Armor(67, 'Chlorophyte Helmet', 13, 0, 0, 0, 0, 0, 0, 16, 0, 0, 0, 0, 0, 0, '20% chance to save ammo', None), Armor(67, 'Chlorophyte Headgear', 7, 0, 0, 0, 0, 0, 0, 0, 0, 16, 0, 80, 0, 0, '17% reduced mana cost', None)]
    chestplates = [Armor(67, 'Chlorophyte Plate Mail', 18, 5, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(67, 'Chlorophyte Greaves', 13, 0, 8, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(67, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Summons a powerful leaf crystal to shoot at nearby enemies\nReduces damage taken by 5%', None)
    stage = 'Pre-Plantera'

class TurtleSet:
    helmets = [Armor(70, 'Turtle Helmet', 21, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Enemies are more likely to target you', None)]
    chestplates = [Armor(70, 'Turtle Scale Mail', 27, 0, 0, 0, 8, 8, 0, 0, 0, 0, 0, 0, 0, 0, 'Enemies are more likely to target you', None)]
    leggings = Armor(70, 'Turtle Leggings', 17, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 'Enemies are more likely to target you', None)
    set_bonus = Armor(70, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Attackers also take double damage\nReduces damage taken by 15%', None)
    stage = 'Pre-Plantera'

class TikiSet:
    helmets = [Armor(71, 'Tiki Mask', 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 1, 'Increases whip range by 10%', None)]
    chestplates = [Armor(71, 'Tiki Shirt', 17, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 1, '', None)]
    leggings = Armor(71, 'Tiki Pants', 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 1, '', None)
    set_bonus = Armor(71, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 'Increases whip range by 20%', None)
    stage = 'Pre-Golem'

class BeetleSet:
    helmets = [Armor(72, 'Beetle Helmet', 23, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Enemies are more likely to target you', None)]
    chestplates = [Armor(72, 'Beetle Scale Mail', 20, 0, 0, 6, 8, 8, 6, 0, 0, 0, 0, 0, 0, 0, '', set_bonus = Armor(72, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Beetles increase your melee damage and speed', None)), Armor(72, 'Beetle Helmet', 23, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Enemies are more likely to target you', set_bonus = Armor(72, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Beetles protect you from damage', None))]
    leggings = Armor(72, 'Beetle Leggings', 18, 0, 0, 6, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 'Enemies are more likely to target you', None)
    set_bonus = None
    stage = 'Pre-Lunatic Cultist'

class ShroomiteSet:
    helmets = [Armor(73, 'Shroomite Headgear', 11, 0, 0, 0, 0, 0, 0, 15, 5, 0, 0, 0, 0, 0, 'Note: 15% ranged damage buff only applies to bows', None), Armor(73, 'Shroomite Mask', 11, 0, 0, 0, 0, 0, 0, 15, 5, 0, 0, 0, 0, 0, 'Note: 15% ranged damage buff only applies to guns', None), Armor(73, 'Shroomite Helmet', 11, 0, 0, 0, 0, 0, 0, 15, 5, 0, 0, 0, 0, 0, 'Note: 15% ranged damage buff only applies to non-bow and non-gun weapons', None)]
    chestplates = [Armor(73, 'Shroomite Breastplate', 24, 0, 0, 0, 0, 0, 0, 13, 13, 0, 0, 0, 0, 0, '20% chance to save ammo', None)]
    leggings = Armor(73, 'Shroomite Leggings', 16, 0, 0, 12, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(73, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Not moving puts you in stealth, increasing ranged ability and reducing chance to enemies to target you', None)
    stage = 'Pre-Golem'

class SpectreSet:
    helmets = [Armor(76, 'Spectre Mask', 18, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 60, 0, 0, '13% reduced mana cost', set_bonus = Armor(76, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Magic damage done will hurt extra nearby enemies', None)), Armor(76, 'Spectre Hood', 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', set_bonus = Armor(77, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Reduces Magic dmage done by 4% and converts it to healing force\nMagic damage done to enemies heals the player with the lowest health', None))]
    chestplates = [Armor(76, 'Spectre Robe', 14, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 0, 0, 0, '', None)]
    leggings = Armor(76, 'Spectre Pants', 10, 0, 0, 8, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, '', None)
    set_bonus = None
    stage = 'Pre-Golem'

class SpookySet:
    helmets = [Armor(78, 'Spooky Helmet', 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 1, '', None)]
    chestplates = [Armor(78, 'Spooky Breastplate', 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 2, '', None)]
    leggings = Armor(78, 'Spooky Leggings', 10, 0, 0, 20, 0, 0, 0, 0, 0, 0, 0, 0, 11, 1, '', None)
    set_bonus = Armor(78, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 0, '', None)
    stage = 'Pre-Golem'

class ValhallaKnightSet:
    helmets = [Armor(79, "Valhalla Knight's Helm", 20, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 10, 2, '', None)]
    chestplates = [Armor(79, "Valhalla Knight's Breastplate", 24, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0, 30, 0, 'Massively increased life regen', None)]
    leggings = Armor(79, "Valhalla Knight's Greaves", 24, 0, 0, 20, 0, 20, 0, 0, 0, 0, 0, 0, 20, 0, '', None)
    set_bonus = Armor(79, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 'Greatly enhances Ballista effectiveness', None)
    stage = 'Pre-Lunatic Cultist'

class ShinobiInfiltratorSet:
    helmets = [Armor(80, "Shinobi Infiltrator's Helmet", 10, 0, 0, 0, 20, 0, 0, 0, 0, 0, 0, 0,  20, 2, '', None)]
    chestplates = [Armor(80, "Shinobi Infiltrator's Torso", 26, 0, 0, 0, 0, 5, 20, 0, 0, 0, 0, 0, 20, 0, '', None)]
    leggings = Armor(80, "Shinobi Infiltrator's Pants", 18, 0, 0, 30, 0, 20, 0, 0, 0, 0, 0, 0, 20, 0, '', None)
    set_bonus = Armor(80, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 'Greatly enhances Lightning Aura effectiveness', None)
    stage = 'Pre-Lunatic Cultist'

class RedRidingSet:
    helmets = [Armor(81, 'Red Riding Hood', 8, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 10, 2, '', None)]
    chestplates = [Armor(81, 'Red Riding Dress', 24, 0, 0, 0, 0, 0, 0, 25, 0, 0, 0, 0, 25, 0, '20% chance to save ammo', None)]
    leggings = Armor(81, 'Red Riding Leggings', 16, 0, 0, 20, 0, 0, 0, 0, 10, 0, 0, 0, 25, 0, '', None)
    set_bonus = Armor(81, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 'Greatly enhances Explosive Trap effectiveness', None)
    stage = 'Pre-Lunatic Cultist'

class DarkArtistSet:
    helmets = [Armor(82, "Dark Artist's Hat", 7, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 0, 15, 2, '', None)]
    chestplates = [Armor(82, "Dark Artist's Robes", 21, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 25, 0, '15% reduced mana cost', None)]
    leggings = Armor(82, "Dark Artist's Leggings", 14, 0, 0, 20, 0, 0, 0, 0, 0, 0, 25, 0, 20, 0, '', None)
    set_bonus = Armor(82, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 'Greatly enhances Flameburst effectiveness', None)
    stage = 'Pre-Lunatic Cultist'

class SolarFlareSet:
    helmets = [Armor(83, 'Solar Flare Helmet', 24, 0, 0, 0, 0, 26, 0, 0, 0, 0, 0, 0, 0, 0, 'Grants minor life regeneration\nEnemies are more likely to target you', None)]
    chestplates = [Armor(83, 'Solar Flare Breastplate', 34, 0, 0, 0, 29, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Grants minor life regeneration\nEnemies are more likely to target you', None)]
    leggings = Armor(83, 'Solar Flare Leggings', 20, 0, 0, 15, 0, 0, 15, 0, 0, 0, 0, 0, 0, 0, 'Grants minor life regeneration\nEnemies are more likely to target you', None)
    set_bonus = Armor(83, '', 0, 0, 0, 0, 0,0 ,0 ,0 ,0 ,0 , 0, 0, 0, 0, 'Solar shields charge over time to protect you and let you dash\nA charge is used to damage enemies you touch\nConsumed carges explode and damage enemies', None)
    stage = 'Endgame'

class VortexSet:
    helmets = [Armor(84, 'Vortex Helmet', 14, 0, 0, 0, 0, 0, 0, 16, 7, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(84, 'Vortex Breastplate', 28, 0, 0, 0, 0, 0, 0, 12, 12, 0, 0, 0, 0, 0, '25% chance to save ammo', None)]
    leggings = Armor(84, 'Vortex Leggings', 20, 0, 0, 10, 0, 0, 0, 8, 8, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(84, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Double tap to toggle stealth, increasing ranged ability and reducing chance for enemies to target you but slowing movement speed', None)
    stage = 'Endgame'

class NebulaSet:
    helmets = [Armor(85, 'Nebula Helmet', 14, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 60, 0, 0, '15% reduced mana cost', None)]
    chestplates = [Armor(85, 'Nebula Breastplate', 18, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 0, 0, 0, '', None)]
    leggings = Armor(85, 'Nebula Leggings', 14, 0, 0, 10, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, '', None)
    set_bonus = Armor(85, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Magic damage has a chance to spawn buff boosters, pick boosters up to get stacking buffs', None)
    stage = 'Endgame'
    
class StardustSet:
    helmets = [Armor(86, 'Stardust Helmet', 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 2, '', None)]
    chestplates = [Armor(86, 'Startdust Plate', 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 2, 'Increases whip range by 15%', None)]
    leggings = Armor(86, 'Stardust Leggings', 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 2, 'Increases whip range by 15%', None)
    set_bonus = Armor(86, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'A stardust guardian will protect you from nearby enemies', None)
    stage = 'Endgame'

class WizardSet:
    helmets = [Armor(87, 'Magic Hat', 2, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 0, 0, 0, '', Armor(87, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 60, 0, 0, '', None)), Armor(87, 'Wizard Hat', 4, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, '', Armor(87, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, '', None))]
    chestplates = [Armor(87, 'Amethyst Robe', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 0, 0, '-5% mana usage', None), Armor(87, 'Topaz Robe', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 40, 0, 0, '-7% mana usage', None), Armor(87, 'Sapphire Robe', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 40, 0, 0, '-9% mana usage', None), Armor(87, 'Emerald Robe', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 60, 0, 0, '-11% mana usage', None), Armor(87, 'Ruby Robe', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 60, 0, 0, '-13% mana usage', None), Armor(87, 'Amber Robe', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 60, 0, 0, '-13% mana usage', None), Armor(87, 'Diamond Robe', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 80, 0, 0, '-15% mana usage', None), Armor(87, 'Mystic Robe', 2, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 0, 0, 0, '-10% mana usage', None)]
    set_bonus = None
    stage = 'Pre-Boss'

stage_tranlsation = {
    'Pre-Boss': 0,
    'Pre-Brain of Cthulhu/Eater of Worlds': 1,
    'Pre-Skeletron': 2,
    'Pre-Wall of Flesh': 3,
    'Pre-Mech Bosses': 4,
    'Pre-Plantera': 5,
    'Pre-Golem': 6,
    'Pre-Lunatic Cultist': 7,
    'Endgame': 8
}

mining = MiningSet
wood = WoodSet
rich_mahogany = MahoganySet
boreal = BorealSet
palm = PalmSet
ebonwood = EbonwoodSet
shadewood = ShadewoodSet
ashwood = AshWoodSet
rain = RainSet
snow = SnowSet
pink_snow = PinkSnowSet
angler = AnglerSet
cactus = CactusSet
copper = CopperSet
tin = TinSet
pumpkin = PumpkinSet
ninja = NinjaSet
iron = IronSet
lead = LeadSet
silver = SilverSet
tungsten = TungstenSet
gold = GoldSet
platinum = PlatinumSet
fossil = FossilSet
bee = BeeSet
obsidian = ObsidianSet
gladiator = GladiatorSet
meteor = MeteorSet
jungle = JungleSet
ancient_cobalt = AncientCobaltSet
necro = NecroSet
shadow = ShadowSet
ancient_shadow = AncientShadowSet
crimson = CrimsonSet
molten = MoltenSet
pearlwood = PearlwoodSet
spider = SpiderSet
cobalt = CobaltSet
palladium = PalladiumSet
mythril = MythrilSet
orichalcum = OrichalcumSet
adamantite = AdamantiteSet
titanium = TitaniumSet
crystal_assassin = CrystalAssassinSet
frost = FrostSet
forbidden = ForbiddenSet
squire = SquireSet
monk = MonkSet
huntress = HuntressSet
apprentice = ApprenticeSet
hallowed = HallowedSet
chlorophyte = ChlorophyteSet
turtle = TurtleSet
tiki = TikiSet
beetle = BeetleSet
shroomite = ShroomiteSet
spectre = SpectreSet
spooky = SpookySet
valhalla = ValhallaKnightSet
shinobi = ShinobiInfiltratorSet
red_riding = RedRidingSet
dark_artist = DarkArtistSet
solar = SolarFlareSet
vortex = VortexSet
nebula = NebulaSet
stardust = StardustSet
wizard = WizardSet


armor_sets = {mining, wood, rich_mahogany, boreal, palm, ebonwood, shadewood, ashwood, rain, snow, angler, cactus, copper, tin, pumpkin, 
              ninja, iron, lead, silver, tungsten, gold, platinum, fossil, bee, obsidian, gladiator, meteor, jungle, necro, 
              shadow, crimson, molten, pearlwood, spider, cobalt, palladium, mythril, orichalcum, adamantite,
              titanium, crystal_assassin, frost, forbidden, squire, monk, huntress, apprentice, hallowed, chlorophyte, turtle, tiki, beetle, shroomite,
              spectre, valhalla, shinobi, red_riding, dark_artist, solar, vortex, nebula, stardust, wizard}

redundant_armor_sets = {pink_snow, ancient_cobalt, ancient_shadow}

redundant_armor = False     # Setting this to True will include armor that is redundant or difficult to obtain

if redundant_armor:
    armor_sets = armor_sets.union(redundant_armor_sets)
else:
    PumpkinSet.stage = 'Pre-Brain of Cthulhu/Eater of Worlds'
    HallowedSet.stage = 'Pre-Plantera'

game_stage = input('Input your current stage of game [Pre-Boss, Pre-Brain of Cthulhu/Eater of Worlds, Pre-Skeletron, Pre-Wall of Flesh, Pre-Mech Bosses, Pre-Plantera, Pre-Golem, Pre-Lunatic Cultist, Endgame]: ')

armor_sets_remove = []

for set in armor_sets:
    if stage_tranlsation[set.stage] > stage_tranlsation[game_stage]:
        armor_sets_remove.append(set)

for set in armor_sets_remove:
    armor_sets.remove(set)
