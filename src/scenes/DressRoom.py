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
def dressing(w: World):
    luna = w.get("luna")
    yoko = w.get("yoko")
    return w.scene("着替え",
            w.change_stage("DressRoom"),
            )
