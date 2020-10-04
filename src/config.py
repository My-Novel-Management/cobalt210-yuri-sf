# -*- coding: utf-8 -*-
'''
Story Config
============
'''

ASSET = {
        "PERSONS": (
            # (tag / name / full / age (birth) / job / call / info)
            ("luna", "ルナ", "", 17,(1,1), "female", "高校生", "me:私"),
            ("yoko", "ヨウコ", "", 17,(1,1), "female", "高校生", "me:わたし"),
            ),
        "STAGES": (
            # (tag / name / parent / (geometry) / info)
            ("Chiba", "千葉県", "Japan"),
            ("School", "高校", "Chiba"),
            ("Classroom", "教室", "School"),
            ("Home", "ルナの自宅", "Chiba"),
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

