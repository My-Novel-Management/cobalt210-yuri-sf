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
def think_about_her(w: World):
    luna = w.get("luna")
    return w.scene('彼女のことを思う',
            w.change_stage("Room"),
            luna.be("自室で勉強している"),
            luna.do("ベッドの上に脱ぎ散らかした防護スーツがある"),
            luna.do("ハーフパンツに上はキャミソールという軽装"),
            luna.do("洗いたての髪でぼさぼさ"),
            luna.do("それでも気楽そうに"),
            luna.do("紙のノートに落書きをしている"),
            luna.do("実は言っていないだけで、今はもう古い表現手段とされている漫画を描きたいと考えていた"),
            luna.do("今は漫画ではなく簡易のアニメーションを作るのが当たり前になっていた"),
            luna.do("小説と同じで古典の部類だ"),
            luna.do("端末の中にも中古で購入した昔の漫画が大量にある"),
            luna.do("ノートには$yokoの素顔や昔の学生のスタイル、セーラー服姿が描かれていた"),
            luna.talk("実際に着てみてもらわないとわかんないなー"),
            luna.do("考え込む"),
            )

