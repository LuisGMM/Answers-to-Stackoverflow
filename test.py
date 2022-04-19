

a = {'A':'',
     'B':'234923',
     'C': 'adkasd',
     'D':'kajskdad'}

b = {'A':'',
     'B':'dfdsf',
     'C': 'adkasd',
     'D':''}


def has_less_void(a: dict, b: dict) -> dict:
    """R

    Args:
        a (dict): _description_
        b (dict): _description_

    Returns:
        dict: _description_
    """
    void_a = void_b = 0

    for ai, bi in zip(a.values(), b.values()):

        if not ai:
            void_a += 1

        if not bi:
            void_b += 1

    return a if void_a < void_b else b
