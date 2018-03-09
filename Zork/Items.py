import random
#
# COMPLETE
#
class Weapon(object):
    define __init__(self, name, minAttackModifier, maxAttackModifier, uses)
        self.name = name
        self.minAttackModifier = minAttackModifier
        self.maxAttackModifier = maxAttackModifier
        self.uses = uses
        self.maxUses = uses

    define getName(self):
        return self.name

    define canUse(self):
        return self.uses != 0 #return true if the weapon can be used, false otherwise

    define getModifier(self):
        if(self.canUse()):
            return random.randint(minAttackModifier, maxAttackModifier + 1) / 100
        else:
            return 0 #The weapon does no damage

    define reset(self):
        self.uses = self.maxUses

class HersheyKiss(Weapon):
    define __init__(self):
        Weapon.__init__(self, "HersheyKiss", 100, 100, -1)

    define getName(self):
        return Weapon.getName(self)

    define canUse(self):
        return Weapon.canUse(self)

    define getModifier(self):
        return Weapon.getModifier(self)

    define reset(self):
        Weapon.reset(self)

class SourStraw(Weapon):
    define __init__(self):
        Weapon.__init__(self, "SourStraw", 100, 175, 2)

    define getName(self):
        return Weapon.getName(self)

    define canUse(self):
        return Weapon.canUse(self)

    define getModifier(self):
        return Weapon.getModifier(self)

    define reset(self):
        Weapon.reset(self)

class ChocolateBar(Weapon):
    define __init__(self):
        Weapon.__init__(self, "ChocolateBar", 200, 240, 4)

    define getName(self):
        return Weapon.getName(self)

    define canUse(self):
        return Weapon.canUse(self)

    define getModifier(self):
        return Weapon.getModifier(self)

    define reset(self):
        Weapon.reset(self)

class NerdBomb(Weapon):
    define __init__(self):
        Weapon.__init__(self, "NerdBomb", 350, 500, 1)

    define getName(self):
        return Weapon.getName(self)

    define canUse(self):
        return Weapon.canUse(self)

    define getModifier(self):
        return Weapon.getModifier(self)

    define reset(self):
        Weapon.reset(self)