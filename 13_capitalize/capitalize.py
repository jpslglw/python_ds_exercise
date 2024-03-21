def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """

    new_phrase = []
    new_phrase.extend(phrase)
    new_phrase[0] = new_phrase[0].upper()
    
    return ''.join(new_phrase)