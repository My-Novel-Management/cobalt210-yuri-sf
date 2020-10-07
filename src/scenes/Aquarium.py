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
    luna = w.get("luna")
    yoko = w.get("yoko")
    return w.scene("水槽の魚たち",
            w.change_stage("Aquarium"),
            luna.be("目の前の水槽を泳ぐメダカを眺めている"),
            yoko.come("そこにドアを開けて入ってくる生徒"),
            yoko.talk("$luna、またここにいる",
                "先生が探してたわよ"),
            luna.talk("$yoko",
                "一時間くらいサボったって死ぬことはないよ"),
            yoko.talk("そういう問題じゃないのよ",
                "将来のために今勉強しておくのは大事なのよ"),
            luna.do("委員長を務める彼女は真面目だからというよりも、本気で$Sのことを考えてくれている",
                "いつも迷惑をかけているのは分かっていたけれど、そうでもしないと、彼女を独占できない"),
            luna.do("彼女は忙しい人なのだ"),
            luna.talk("ねえ、$yokoはどう思う"),
            luna.do("前の前で泳ぐメダカは水質を見るための犠牲だ",
                "自分たちもこれと同じで、何も知らないまま社会の何かの実験につきあわされているだけかも知れない"),
            luna.think("いつも考える",
                "みんな何も考えてないと"),
            yoko.talk("そういう$lunaは今目の前にある一番の問題から逃げてるだけじゃないの？"),
            luna.talk("一番の問題って何？"),
            yoko.talk("学生の本分は勉強よ",
                "それから進路ね",
                "漫然と次のステップとしての大学、それも自分の学力で行けそうなところを選ぶのではなくて、",
                "その先まで見通して掴みに行くくらいの気概がないと"),
            luna.do("彼女はいつも自信に満ちている",
                "防護スーツ越しにも容姿や体型の良さが分かる"),
            luna.do("自分は全然ダメだ",
                "何をしてもダメ"),
            luna.do("先のことなんて考えられない"),
            luna.do("そんなフリをして彼女に心配してもらうのが、今の一番の関心事だとは彼女は理解できない"),
            luna.think("成績の良さとは関係ないのだと、中学の頃に知った"),
            luna.talk("$meたちなんてこのメダカと同じだよ",
                "用済みになったらまた別の新しいメダカと取り替えられるだけ",
                "社会なんてこの水槽みたいなもんじゃないかな"),
            yoko.talk("なら$meはその水槽がいらない社会を作ってみせるわ"),
            luna.talk("どうやって？"),
            yoko.do("$Sは自分の端末を見せる"),
            luna.do("そこには$Sが見たこともないような難しい電子書籍が並んでいた"),
            # TODO
            )


def black_out(w: World):
    luna = w.get("luna")
    return w.scene("停電",
            w.change_stage("Aquarium"),
            )


def out_suites(w: World):
    luna = w.get("luna")
    return w.scene("スーツを脱いで",
            w.change_stage("Aquarium"),
            )


def alone(w: World):
    luna = w.get("luna")
    return w.scene('空虚な水槽',
            w.change_stage("Aquarium"),
            )

