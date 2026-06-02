def cmp_version(v1, v2) -> int:
    t1 = tuple(int(x) for x in v1.split("."))
    t2 = tuple(int(x) for x in v2.split("."))
    if t1 > t2:
        return 1
    elif t1 < t2:
        return -1
    return 0
