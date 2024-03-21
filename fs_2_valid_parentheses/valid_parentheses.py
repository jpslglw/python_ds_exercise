def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """

    stack = []
    mapping = {")": "("}

    for char in parens:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack:
                return False
            if stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:
            return False

    return not stack