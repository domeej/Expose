import django
import os


def populate():
    print("populate models...")

    l = Alias(alias_name='schimmliger Spiecker')
    m = Alias(alias_name='schabernak Spiecker')
    h = Alias(alias_name='Saftiger Spiecker')
    spiecker = Player.objects.get_or_create(name='Spiecker')[0]
    spiecker.aliases = [l, m, h]
    spiecker.save()

    l = Alias(alias_name='kausaler Köhli')
    m = Alias(alias_name='kometenhafter Köhli')
    h = Alias(alias_name='Kaiser Köhli')
    koehli = Player.objects.get_or_create(name='Köhli')[0]
    koehli.aliases = [l, m, h]
    koehli.save()

    l = Alias(alias_name='gratis Ginzel')
    m = Alias(alias_name='gefahrloser Ginzel')
    h = Alias(alias_name='geriffelter Ginzel')
    ginzel = Player.objects.get_or_create(name='Ginzel')[0]
    ginzel.aliases = [l, m, h]

    ginzel.save()





if __name__ == '__main__':
    from karma.models import Player, Alias, Game, Rank

    populate()