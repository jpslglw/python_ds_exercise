def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    lst = []
    lst.extend(phrase)

    for l in range(len(lst)):
        if lst[l].lower() == to_swap.lower():
            if lst[l].isupper() and to_swap.isupper():
                lst[l] = to_swap.lower()
            elif lst[l].islower() and to_swap.isupper():
                lst[l] = to_swap
            elif lst[l].isupper() and to_swap.islower():
                lst[l] = to_swap
            elif lst[l].islower() and to_swap.islower():
                lst[l] = to_swap.upper()
    return ''.join(lst)