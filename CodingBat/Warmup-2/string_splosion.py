def string_splosion(str):
    non_emptystr = ''
    for i in range(0, len(str)+1):
        non_emptystr += str[:i]
    return non_emptystr
