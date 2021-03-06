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
    ana = w.get("woman")
    return w.scene('ドローンの泳ぐ空',
            w.change_camera("luna"),
            w.change_stage("Street"),
            w.change_time("morning"),
            w.change_date(10,1, 2040),
            luna.come("#歩いている"),
            luna.do("スプレー缶が破裂した後みたいな濃淡の雲が空に蓋をしていた",
                "そこを一匹のメタリックな光が飛んでいく",
                "スカイフィッシュと呼ばれている観測用ドローンだ",
                "本当の名前は何度か委員長の$ln_yokoさんから聞いたけれど誰もその名で呼んでいるのを耳にしたことはない"),
            luna.do("今はそれがグリーンのライトを灯しているから安全なはずだ",
                "それでも$Mの前を歩く誰一人として白銀色の防護スーツを脱いだりはしない",
                "頭部はバイクに乗る時のヘルメットみたいにフルフェイスで誰がどんな髪の色でどういう髪型をしていてリボンやゴムは付けているのかとか、",
                "全然分からない",
                "体の方も雨合羽みたいに銀色が覆っていて体型どころか男なのか女なのかすら見分けがつかない"),
            luna.think("でも誰もそんなことを気にしない",
                "駅に向かって歩いている",
                "そう",
                "これが$Mたちが生まれてから目の前に存在している日常だからだ"),
            ana.be(),
            ana.talk("午後からは濃霧注意報が出ていますので可能な限り外出は控え、屋内から出ないようにして下さい",
                "繰り返します、本日午後から――"),
            luna.do("別のスカイフィッシュが注意喚起のアナウンスを行っている",
                "前を歩いていた同じ高校の生徒が二人肩を寄せ合い「それじゃ今日も学校午前だけ？」「ラッキーだね。帰りどこ寄る？」楽しげな声を漏らしていた",
                "$Mは端末を取り出して何のメッセージも着ていないことを確認すると、足早に駅の入り口に向かった"),
            )

