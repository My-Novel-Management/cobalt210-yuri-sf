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
            luna.be("体育の授業が終わり、みんな更衣室に戻ってきていた"),
            yoko.come("$Sは先に個室に入っていく"),
            luna.do("じろじろと彼女の彼女の後ろ姿を見つめている"),
            luna.talk("あ、$yoko"),
            yoko.talk("ああ$luna、おつかれ", "どうかした？"),
            luna.talk("ううん"),
            luna.think("一緒に着替えてもいいかと聞きたくなった"),
            luna.do("しかし個室の利用は一人と制限されている"),
            yoko.do("学生証を当て、入室する$S"),
            luna.do("$Sも仕方なく諦めて、じっと彼女が出てくるのを待つ"),
            luna.do("他の生徒も次々と入っては着替えて出てくる"),
            luna.do("隣から$lunaや他の女子生徒の喋り声が響いている"),
            yoko.talk("ほんと、これでシャワーでもあれば最高なんだけど"),
            luna.do("$Sが体を動かす時間が好きなことをよく知っていた"),
            yoko.do("$Sが出てくる"),
            yoko.talk("どうかした？"),
            luna.talk("ううん、なんでも"),
            luna.do("そのすぐ後の個室に入る$S"),
            luna.do("個室の隅々まで見る"),
            luna.do("と、足元に彼女の髪の毛を見つけた"),
            luna.do("それをそっと拾い上げ、しまっておく"),
            luna.think("触れたい気持ちが抑えられなくなってきていた"),
            )
