# -*- coding: utf-8 -*-
'''
Story Config
============
'''

ASSET = {
        "PERSONS": (
            # (tag / name / full / age (birth) / job / call / info)
            ("luna", "ルナ", "イチミヤ,ルナ", 17,(1,1), "female", "高校生", "me:私"),
            ("yoko", "ヨウコ", "サエキ,ヨウコ", 17,(1,1), "female", "高校生", "me:わたし"),
            ("kita", "キタガワ", "", 37,(1,1), "female", "教師", "me:私"),
            ),
        "STAGES": (
            # (tag / name / parent / (geometry) / info)
            ("Chiba", "千葉県", "Japan"),
            ("School", "高校", "Chiba"),
            ("Corridor", "廊下", "School"),
            ("Classroom", "教室", "School"),
            ("Library", "図書室", "School"),
            ("Aquarium", "水質管理質", "School"),
            ("ManagementBlock", "管理棟", "School"),
            ("Gymnasium", "体育館", "School"),
            ("DressRoom", "更衣室", "School"),
            ("Home", "ルナの自宅", "Chiba"),
            ("Room", "ルナの自室", "Home"),
            ("Park", "海浜公園", "Chiba"),
            ("Street", "路地", "Chiba"),
            ),
        "DAYS": (
            # (tag / name / month / day / year)
            ),
        "TIMES": (
            # (tag / name / hour / minute)
            ),
        "ITEMS": (
            # (tag / name / cate / info)
            ),
        "WORDS": (
            # (tag / name / cate / info)
            ),
        "RUBIS": (
            # (origin / rubi / exclusions / always)
            ),
        }

