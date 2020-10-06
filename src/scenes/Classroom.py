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
def classmates(w: World):
    return w.scene('スーツの生徒たち',
            w.change_stage("Classroom"),
            )


def missing(w: World):
    return w.scene("彼女のいない教室",
            w.change_stage("Classroom"),
            )
