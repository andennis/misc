from typing import List


def _servers_interacted_count(srvs_map: List[List[int]]) -> int:
    num = 0
    for xy in range(len(srvs_map)):
        num_x = 0
        for x in range(len(srvs_map[xy])):
            if srvs_map[xy][x]:
                num_x += 1

        num_y = 0
        for y in range(len(srvs_map)):
            if srvs_map[y][xy]:
                num_y += 1

        if num_x > 1:
            num += num_x
        if num_y > 1:
            num += num_y

        if srvs_map[xy][xy] and num_y > 1 and num_x > 1:
            num -= 1

    return num


def servers_interacted_count(srvs_map: List[List[int]]) -> int:
    num = 0
    for y in range(len(srvs_map)):
        num_x = 0
        for x in range(len(srvs_map[y])):
            num_x += srvs_map[y][x]
        if num_x == 1:
            ind_x = next(i for i, v in enumerate(srvs_map[y]) if v == 1)
            num_y = 0
            for y2 in range(len(srvs_map)):
                num_y += srvs_map[y2][ind_x]
            if num_y > 1:
                num += 1
        else:
            num += num_x

    return num
