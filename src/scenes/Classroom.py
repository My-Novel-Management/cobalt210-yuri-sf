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
    yoko = w.get("yoko")
    kita = w.get("kita")
    return w.scene('スーツの生徒たち',
            w.change_stage("Classroom"),
            "ライトで安全を示す。ライトや色をモチーフとして使うこと",
            "生徒の顔がよく分からないのを示しておくこと。先生とかも",
            "あと「閉じ込められている感」を見せる",
            luna.come("#教室に入ってくる"),
            yoko.be(),
            luna.do("扉の前に立ち端末を翳すと自動で電子学生証を認識して木目がプリントされた金属製のドアがスライドする",
                "教室は既に半分程度の席が埋まっていて各自思い思いに始業までの時間を過ごしていた",
                "$Mは「おはよう」と声に出すこともなくそのまま無言で入ると、視線を一番前の席でじっと自分の端末に見入っている生徒に投げやる",
                "入学して以来、一度としてその素顔を見たことのない委員長の$full_yokoは$Mの存在に気づくことなく後ろの席から掛けられた声に反応して振り返り、",
                "「ここ分からないんだけど」という懇願に答えて宿題の面倒を見始める"),
            luna.do("零した小さな溜息が一瞬防護ヘッドのアイラインを曇らせたが、それはすぐに消え、$Mは一番窓際の前の席へと歩いていって腰を下ろした",
                "机の上に置いた鞄から教科書を取り出して引き出しに仕舞おうとしたところで電子音の短いメロディが響き、始業を伝える"),
            kita.come(),
            luna.do("担任の$kitaが入ってきてさっさと教壇に立つ",
                "教師といっても外見は$Mたちと何も変わらない",
                "白銀色の防護スーツとフルフェイスのその人物は三十六名が席に座ったのを確認すると自分の端末を手に、出欠データと照合を取る",
                "学生だけでなく校内の全ての人間や設備の管理は学内サーバで一括して行われていた"),
            kita.talk("本日の連絡事項は各自掲示板を確認しておくように",
                "先生からは特にありません",
                "ああ、そうそう",
                "$ln_lunaさんは後で職員室に来るように"),
            luna.think("またか、という空気が$Mだけでなく教室全体に広がる"),
            luna.do("ぼんやりと視線を先生の頭上に向けると、空気が安全であることを示す小さなライトがグリーンの光をそっと灯していた"),
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
