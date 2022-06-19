"""LTV Challenge."""

def calc_ltv(ltv, fr, br):
    """Caculate overlap of two rectangles."""
    if ltv < .85:
        return "Approved"
    else:
        if fr < .25 and br < .25:
            return "Approved"
        else:
            return "Denied"

def calc_front(unk):
    return None

def calc_back(unk):
    return None


ltv = calc_ltv(1, 1, 1)

front = calc_front(1)

back = calc_back(1)

# patching
ltv = .83
front = .24
back = .34





result = calc_ltv(ltv, front, back)
print(result)
