from django.db import models
from django.conf import settings

class Character(models.Model):
    base_class_choices = [
        ('Lord (Lyndis)', 'Lord (Lyndis)'),
        ('Blade Lord', 'Blade Lord'),
        ('Lord (Eliwood)', 'Lord (Eliwood)'),
        ('Knight Lord', 'Knight Lord'),
        ('Lord (Hector)', 'Lord (Hector)'),
        ('Great Lord', 'Great Lord'),
        ('Mercenary', 'Mercenary'), ('Hero', 'Hero'),
        ('Myrmidon', 'Myrmidon'), ('Swordmaster', 'Swordmaster'),
        ('Thief', 'Thief'), ('Assassin', 'Assassin'),
        ('Armour Knight', 'Armour Knight'), ('General', 'General'),
        ('Fighter', 'Fighter'), ('Warrior', 'Warrior'),
        ('Bandit', 'Bandit'), ('Pirate', 'Pirate'),
        ('Beserker', 'Beserker'), ('Archer', 'Archer'),
        ('Sniper', 'Sniper'), ('Nomad', 'Nomad'),
        ('Nomad Trooper', 'Nomad Trooper'), ('Cavalier', 'Cavalier'),
        ('Paladin', 'Paladin'), ('Pegasus Knight', 'Pegasus Knight'),
        ('Falcon Knight', 'Falcon Knight'), ('Wyvern Rider', 'Wyvern Rider'),
        ('Wyvern Lord', 'Wyvern Lord'), ('Monk', 'Monk'), ('Cleric', 'Cleric'),
        ('Bishop', 'Bishop'), ('Troubadour', 'Troubadour'),
        ('Valkyrie', 'Valkyrie'), ('Mage', 'Mage'), ('Sage', 'Sage'),
        ('Archsage', 'Archsage'), ('Shaman', 'Shaman'), ('Druid', 'Druid'),
        ('Dark Druid', 'Dark Druid'), ('Bard', 'Bard'), ('Dancer', 'Dancer')
    ]

    affinity_choices = [
        ('FI', 'Fire'), ('TH', 'Thunder'), ('WD', 'Wind'), ('IC', 'Ice'),
        ('DK', 'Dark'), ('LT', 'Light'), ('AN', 'Anima'),
    ]

    name = models.CharField(max_length=30)
    description = models.CharField(max_length=150, default='')
    recruitment_chapter = models.IntegerField(default=0)
    strength_user = models.BooleanField(default=True)
    magic_user = models.BooleanField(default=False)
    base_class = models.CharField(
        max_length=20,
        choices=base_class_choices,
        default='Cavalier'
    )
    affinity = models.CharField(
        max_length=20,
        choices=affinity_choices,
        default='FI'
    )

    def __str__(self):
        return self.name


class Stats(models.Model):
    hp = models.IntegerField(default=0)
    strength = models.IntegerField(default=0)
    magic = models.IntegerField(default=0)
    skill = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)
    luck = models.IntegerField(default=0)
    defence = models.IntegerField(default=0)
    resistance = models.IntegerField(default=0)

    class Meta:
        abstract = True


class BaseStats(Stats):
    character = models.OneToOneField(
        Character,
        on_delete=models.CASCADE,
        related_name='base_stats'
    )
    constitution = models.IntegerField(default=0)
    move = models.IntegerField(default=0)
    level = models.IntegerField(default=0)

    def __str__(self):
        return character.name + " base stats"


class GrowthRates(Stats):
    character = models.OneToOneField(
        Character,
        on_delete=models.CASCADE,
        related_name='growth_rates'
    )

    def __str__(self):
        return character.name + " growth rates"
