#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Story: "title"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.assets import basic
from storybuilder.assets import common_rubi
from config import ASSET
# import scenes
# from scenes import xxx


################################################################
#
#   1. Initialize
#   2. Story memo
#   3. Structure    - 1/8：1K
#   4. Spec
#   5. Plot         - 1/4：2K
#   6. Scenes
#   7. Conte        - 1/2：5K
#   8. Layout
#   9. Draft        - 1/1：10K
#
################################################################

# Constant
TITLE = "ハダカの気持ちに触れたくて"
MAJOR, MINOR, MICRO = 0, 1, 0
COPY = "すべてを取り払った本当のあなたに触れたい"
ONELINE = "空気が汚れて防護スーツなしには出歩けなくなった近未来。一度も触れたことのない同級生の肌に触れたくなり、ある決断をする"
OUTLINE = "約一万字のSF短編。空気が汚れて出歩くのに防護スーツ必須となった時代。そこで学生たちは互いに触れ合うことなく暮らしていた。ある日、同級生と二人きりになり、スーツを脱いでみないかと提案する"
THEME = "常識を疑うこと"
GENRE = "SF／百合"
TARGET = "10-20years"
SIZE = "原稿25-30枚（8K〜10K）"
CONTEST_INFO = "コバルト短編小説新人賞"
CAUTION = ""
NOTE = ""
SITES = ["エブリスタ", "小説家になろう", "ノベルアッププラス", "カクヨム"]
TAGS = ["SF", "学生", "百合"]
RELEASED = (10, 10, 2020)


# Episodes
def ep_xxx(w: World):
    return w.episode('episode_title',
            )


def ch_main(w: World):
    return w.chapter('main',
            )

# Notes
def writer_note(w: World):
    return w.writer_note("覚書",
            )

def plot_note(w: World):
    return w.writer_note("プロットメモ",
            "世界設定：ウイルス汚染が進み、保護スーツなしでは外出できない世界",
            "そこで暮らす学生",
            "みんな何も疑問に持たず、その生活に馴染んでいた",
            "けれど彼女だけは何故？を常に心に持っていた",
            "潔癖症の親友は今の生活を気に入っているようだった",
            "ある日、電源が落ちて二人きりで閉じ込められる",
            "非常電源に切り替わる",
            "彼女も自分に興味があったと知り、ある提案をした",
            "二人ともスーツを脱いで、触れ合う",
            "はじめて触れる他人の、素肌",
            "別の日、二人で外に出かける",
            "そこでスーツを脱ごうと言い出す",
            "生きられないんじゃないか、という思いとは裏腹に、あの感覚を味わいたかった",
            "砂浜で、二人はスーツを脱ぐ",
            "太陽、風、潮の香り",
            "なにもかもが刺激的で、体が生きているを実感する",
            "大丈夫だと思ったのに、その翌日、親友だけが入院した",
            )

def chara_note(w: World):
    return w.writer_note("人物メモ",
            "＊女子高生１：主人公で友人に触れてみたいという思いに苦しんでいる",
            "＊女子高生２：同級生。とても綺麗なことが自慢。潔癖症",
            )

def stage_note(w: World):
    return w.writer_note("舞台メモ",
            "学校",
            "近未来の高校が舞台",
            )

def theme_note(w: World):
    return w.writer_note("テーマメモ",
            "世間の常識",
            "それは本当にそうなのか？　と疑うことで、常識の檻から抜け出せる",
            "常識とは誰かが押し付けた「その人の考え」でしかないこと",
            "常識なんてものは存在しない",
            "イメージはやなぎなぎさんあたり",
            "優しくて綺麗を装っていて、毒々しい",
            )

def motif_note(w: World):
    return w.writer_note("モチーフ",
            "汚染",
            "汚れ",
            "思春期",
            "触れたい",
            )


# Main
def main(): # pragma: no cover
    w = World.create_world(f"{TITLE}")
    w.config.set_version(MAJOR, MINOR, MICRO)
    w.db.set_from_asset(basic.ASSET)
    w.db.set_from_asset(common_rubi.ASSET)
    w.db.set_from_asset(ASSET)
    # spec
    w.config.set_copy(f"{COPY}")
    w.config.set_oneline(f"{ONELINE}")
    w.config.set_outline(f"{OUTLINE}")
    w.config.set_theme(f"{THEME}")
    w.config.set_genre(f"{GENRE}")
    w.config.set_target(f"{TARGET}")
    w.config.set_size(f"{SIZE}")
    w.config.set_contest_info(f"{CONTEST_INFO}")
    w.config.set_caution(f"{CAUTION}")
    w.config.set_note(f"{NOTE}")
    w.config.set_sites(*SITES)
    w.config.set_taginfos(*TAGS)
    w.config.set_released(*RELEASED)
    return w.run(
            writer_note(w),
            plot_note(w),
            chara_note(w),
            stage_note(w),
            theme_note(w),
            motif_note(w),
            ch_main(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

