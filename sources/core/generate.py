from core.ui import ui
def generate():
    print("-"*25)
    print("Action generate")
    print("-"*25)
    ui_repo = {"type": "type <github|gitlab> = ", "url": "url = ",}
    ui_auth = {"token": "token = ", "header": "header = "}
    ui_project = {"name": "name = ", "description": "description = " }
    repo = {} 
    repo.update(ui(ui_repo))
    auth = {}
    auth.update(ui(ui_auth))
    project = {}
    project.update(ui(ui_project))
    save(repo, auth, project)


def write(output, item, tabspace=4):
    for interaction, action in item.items():
        tabultation = " "*tabspace
        output.write("{0}{1}: {2}\n".format(tabultation, interaction, action))


def save(repo, auth, project):
    filename = input("Specify projectfile name : ")
    with open("{0}.yaml".format(filename), 'w+') as output:
        output.write("repo:\n")
        write(output, repo)
        output.write("    auth:\n")
        write(output, auth, tabspace=8)
        output.write("project:\n")
        write(output, project)
