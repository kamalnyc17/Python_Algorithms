# We need to traverse through string and check if every open [{( has a corresponding )}] in correct order

sample_string = "[{()}]"

# user defined function to perform the traversing and comparing


def check_string(input_string):
    openers_and_closers = {
        '(': ')',
        '{': '}',
        '[': ']',
    }
    openers = set(openers_and_closers.keys())
    closers = set(openers_and_closers.values())

    openers_stack = []
    for char in input_string:
        if char in openers:
            openers_stack.append(char)
        elif char in closers:
            if not openers_stack:
                return False
            else:
                # identifying the most recent "open" bracket
                last_unclosed_opener = openers_stack.pop()
                # if the current closer doesn't correspond to the above opener, short-circuit & return False
                if openers_and_closers[last_unclosed_opener] != char:
                    return False

    return openers_stack == []


print(check_string(sample_string))
