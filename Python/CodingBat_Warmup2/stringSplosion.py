def string_splosion(str):
    output = ""
    for i in range(len(str) + 1):
        output += str[0:i]
    return output
