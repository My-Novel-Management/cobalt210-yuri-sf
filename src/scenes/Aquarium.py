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
            w.change_stage("Aquarium"),
            )


def black_out(w: World):
    return w.scene("停電",
            w.change_stage("Aquarium"),
            )


def out_suites(w: World):
    return w.scene("スーツを脱いで",
            w.change_stage("Aquarium"),
            )


def alone(w: World):
    return w.scene('空虚な水槽',
            w.change_stage("Aquarium"),
            )

