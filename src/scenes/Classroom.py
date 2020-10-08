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
    luna = w.get("luna")
    return w.scene('スーツの生徒たち',
            w.change_stage("Classroom"),
            # TODO
            "ライトで安全を示す。ライトや色をモチーフとして使うこと",
            "生徒の顔がよく分からないのを示しておくこと。先生とかも",
            "あと「閉じ込められている感」を見せる",
            luna.come("教室に入ってくる"),
            luna.do("誰もが防護スーツ姿で着席している"),
            luna.do("端末を手におしゃべり"),
            luna.do("窓ははめ殺しで、空調整備がグリーンライトを灯している"),
            luna.do("正常な空気が保たれているのに、誰一人としてスーツを脱ぐ者はいない"),
            luna.do("先生が入ってくる"),
            )


def missing(w: World):
    luna = w.get("luna")
    return w.scene("彼女のいない教室",
            w.change_stage("Classroom"),
            luna.be("けれど翌日から、$yokoの姿はなくなった"),
            luna.do("担任は親の都合で急遽転校したと説明していたが、何か問題があったことは明白だった"),
            luna.do("あの後彼女は抗議にいくと言っていたけれど、連絡は何もない"),
            luna.do("返信のない端末をぼんやりと見つめて"),
            )
