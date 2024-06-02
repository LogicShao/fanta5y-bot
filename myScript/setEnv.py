with open('pyproject.toml', 'r') as f:
    pyproject: str = f.read()

consoleSet = '{ name = "Console", module_name = "nonebot.adapters.console" },\n'

if consoleSet in pyproject:
    Localfile = pyproject
    UnLocalfile = pyproject.replace(consoleSet, "")
else:
    UnLocalfile = pyproject
    Localfile = ''
    for line in pyproject.splitlines():
        if line.startswith('adapters'):
            Localfile += line + '\n'
            Localfile += "    " + consoleSet
        else:
            Localfile += line + '\n'

sureSet = set(
    ["y", "yes", "ok", "sure", "1"]
)

if __name__ == "__main__":
    print("This script is used to set the local environment of the project.")

    print("The local environment is set to the following configuration: ")
    s = input("do you want to set local? (y/n): ").lower()
    if s in sureSet:
        with open("pyproject.toml", "w") as f:
            f.write(Localfile)
    else:
        with open("pyproject.toml", "w") as f:
            f.write(UnLocalfile)

    print("now set your system proxy port")
    port = input("input your port: ")
    # 如果输入为空则不写入
    if port != "":
        with open("acmhelper.env", "w") as f:
            f.write(f"port={port}")

    print("done")
