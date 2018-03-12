from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_coral',
        {
            'title': 'Coral Collector',
            'desc': 'Corals mined',
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:mined'],
            ['minecraft:.+_coral','minecraft:.+_coral_plant']
        )
    ))
