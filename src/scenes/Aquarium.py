# -*- coding: utf-8 -*-
'''
Stage: "stage name"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def fishes(w: World):
    return w.scene("水槽の魚たち",
            )


def alone(w: World):
    return w.scene('空虚な水槽',
            )

