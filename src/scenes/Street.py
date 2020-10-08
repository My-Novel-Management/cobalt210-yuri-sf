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
    luna = w.get("luna")
    return w.scene('ドローンの泳ぐ空',
            w.change_camera("luna"),
            w.change_stage("Street"),
            w.change_time("morning"),
            w.change_date(10,1, 2040),
            luna.come("歩いている"),
            luna.do("空を見上げると観測用ドローンや監視用ドローンが飛んでいる"),
            luna.do("$Sはそれを見て魚みたいだと思った"),
            luna.do("自分の体を見ると、スーツをまとっている"),
            luna.do("他にも学校に向かう同じスーツ姿の生徒たち"),
            luna.do("ドローンから音声で気象濃度が上昇するから外出を控えるようにと警告があった"),
            )

