def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """

    phrase = phrase.lower()
    new_str = phrase.split(' ')

    for l in range(len(new_str)):
        new_str[l] = new_str[l].replace(new_str[l][0], new_str[l][0].upper())
    return ' '.join(new_str)