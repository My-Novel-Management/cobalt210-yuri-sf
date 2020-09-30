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
            outline="description")


def ch_main(w: World):
    return w.chapter('main',
            )

# Notes
def writer_note(w: World):
    return w.writer_note("覚書",
            )

def plot_note(w: World):
    return w.writer_note("プロットメモ",
            )

def chara_note(w: World):
    return w.writer_note("人物メモ",
            )

def stage_note(w: World):
    return w.writer_note("舞台メモ",
            )

def theme_note(w: World):
    return w.writer_note("テーマメモ",
            )

def motif_note(w: World):
    return w.writer_note("モチーフ",
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

