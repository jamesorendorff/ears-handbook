"""

barbarian, bard, cleric, druid, fighter, monk, paladin, ranger, rogue, sorcerer, warlock, wizard

Ideal examples:

The party teams up with a naive gnomish cobbler to face a ruthless drider and her pet violet fungi.

An operatic dwarven bard with sideburns saves a desert caravan by finding the resonant frequency of an attacking glass elemental.

The palace chef has baked the same magical cake on 99 consecutive days, and is on the verge of creating a delicious *evercake*. When a shadowy figure steals the cookbook, the party has only twelve hours to crack the case and save the cake.

A team of dwarvish miners is trapped when a tunnel collapses. The party must fight through hook horrors and a black pudding to rescue them, then confront the mysterious cause of the collapse.

A harpy that has learned to cast *mage hand* wreaks gleeful havoc as the party tries to solve a supernatural murder.

Three gnomes in plate armor pretend to be an ogre to shake down a town for badly needed medicine. (@detarame)

"""

productions = {
    'pc_race_plural': [
        'halflings',
        'dwarves',
        'elves',
        'gnomes',
    ],

    'monsters': [
        'hook horrors',
    ],

    'a_monster': [
        'an ogre',
        'a troll',
        'a harpy',
        'a black pudding',
    ],
    
    'people': [
        'three ${pc_race_plural} disguised as ${a_monster}',
        'some dwarvish miners',
    ],

    'vp': [
        'are trapped when a tunnel collapses',
        'must fight through ${monsters} and ${a_monster}',
        'try to solve a supernatural murder',
    ],
    
    'scenario': [
        '${people} ${vp}.'
    ],
}
