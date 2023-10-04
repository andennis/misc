def intersect_rects(rect1: tuple, rect2: tuple) -> tuple:
    l1, t1, r1, b1 = rect1
    l2, t2, r2, b2 = rect2
    v_ln = intersect_lines((l1, r1), (l2, r2))
    h_ln = intersect_lines((b1, t1), (b2, t2))
    return (v_ln[0], h_ln[1], v_ln[1], h_ln[0]) if v_ln and h_ln else ()


def intersect_lines(ln1: tuple[int, int], ln2: tuple[int, int]) -> tuple[int, int]:
    x11, x12 = ln1
    x21, x22 = ln2
    x31 = max(x11, x21)
    x32 = min(x12, x22)
    return (x31, x32) if x31 <= x32 else ()
