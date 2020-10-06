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
def drone_sky(w: World):
    return w.scene('ドローンの泳ぐ空',
            w.change_camera("luna"),
            w.change_stage("Street"),
            w.change_time("morning"),
            w.change_date(10,1, 2040),
            )

