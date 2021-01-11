import json


def buildImgJson(point_list, label, image_path, group_id=none):
    shapes = {
        'label': label,
        'points': point_list,
        'group_id': group_id,
    }

    json = {
        'shapes':shapes,

    }
