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
            luna.be("#自室で勉強している"),
            luna.do("シャワーを浴び終えて自室に戻る",
                "どうせならこの格好のまま外を出歩きたいと思うけれど、そんなことは絶対に許してもらえない",
                "ベッドの上に倒れ込み、レモングリーンのカーテンを引いた",
                "はめ殺しの窓からは夜の街並みが見えたけれどマンションの明かりよりも赤い警告灯を光らせた警戒用ドローンのそれの方がずっと多くて、",
                "あまり心地良いものじゃない"),
            luna.do("$Mは寝返りを打って床に脱ぎ散らかしたままの防護スーツを見た",
                "転がったヘルメットの下でくしゃくしゃになっている白銀のスーツは自分の抜け殻のようで、それを退かせばもう一人の$Mが溶けたまま寝そべっているんじゃないかと思える"),
            luna.do("$Mはそれから視線を逸らし、膝を引きつけて丸まった",
                "&"),
            luna.do("赤いラインのハーフパンツと花の模様の付いた白のキャミソールがいつもの部屋着で、",
                "急いでいるときはこの上にそのまま防護スーツを着てしまう",
                "あんな薄い人工皮一枚で一体何が守られるというのだろう"),
            luna.do("学習机からノートを手に取ると、続きのページを開く",
                "そこには現代では全く見られなくなったフリルの付いた服や装飾の多いドレス姿の女性が何人も描かれている",
                "全部昔の写真や映像を見て写したものだ",
                "リアルに描いてあるものも一部あったけれど大半はアニメ調だった"),
            luna.do("漫画、という文化だと父からは教わっている"),
            luna.do("でも今は誰もこんな古い表現手段で創作をしていない",
                "全てがデジタルでプログラムで、鉛筆を手にすることも大半の人間には経験がない",
                "そんな時代だ",
                "けれど$Mはカリカリと黒鉛が削れてそれが真っ白な紙の上に新しい生命を形作っていく瞬間が好きだった",
                "$Mの端末の中には$ln_yokoさんとは違い、中古で購入した昔の漫画が大量に並んでいる",
                "中には今から五十年も昔の作品もあって、でも全然色あせてなんて見えなくて、",
                "$Mにとっては教科書と同義だった"),
            luna.do("$Mはノートに服装だけ描いてあった途中の作品に、頭部を軽く描く",
                "卵型に目鼻の位置のアテの線を引き、そこに彼女の素顔を想像して少しずつ線を加えていく",
                "けれど学生証の写真だけではいまいち感じが掴みづらい",
                "書いては消し、また書いては消す"),
            luna.talk("やっぱ、実際に見てみたいな"),
            luna.do("鉛筆の芯の先をじっと見つめ、$Mはそれをノートの上の古い学生の制服に当てる",
                "斜めに寝かせて塗りつぶしていく",
                "本物の制服を彼女が着たならどんなに似合うだろう",
                "そんな思いばかりが鉛筆を走らせた"),
            )

