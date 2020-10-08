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
def want_touching(w: World):
    luna = w.get("luna")
    yoko = w.get("yoko")
    return w.scene('触れたい気持ち',
            w.change_stage("Gymnasium"),
            luna.be("体育の授業中"),
            yoko.be(),
            luna.do("スポーツ用の軽量防護服に着替えて、バレーをしている"),
            yoko.do("$Sは飛び上がり、強烈なスパイクを放つ"),
            luna.do("その姿に見惚れる"),
            )

