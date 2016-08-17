def ui(part):
    commands = {}
    for interaction, action in part.items():
        result = input(action)
        commands.update({interaction: result})
    return commands


def splash():
    print("<{0} MSGENERATOR {0}>".format("-"*25))
    row = "|{0}|\n".format("\t"*8)
    print(row*5)
