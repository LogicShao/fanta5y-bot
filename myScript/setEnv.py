Localfile = """[project]
name = "test"
version = "0.1.0"
description = "test"
readme = "README.md"
requires-python = ">=3.8, <4.0"

[tool.nonebot]
adapters = [
    { name = "OneBot V11", module_name = "nonebot.adapters.onebot.v11" },
    { name = "Console", module_name = "nonebot.adapters.console" }
]
plugins = ["plugins"]
plugin_dirs = ["plugins"]
builtin_plugins = ["echo"]
"""

UnLocalfile = """[project]
name = "test"
version = "0.1.0"
description = "test"
readme = "README.md"
requires-python = ">=3.8, <4.0"

[tool.nonebot]
adapters = [
    { name = "OneBot V11", module_name = "nonebot.adapters.onebot.v11" },
]
plugins = ["plugins"]
plugin_dirs = ["plugins"]
builtin_plugins = ["echo"]
"""

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
    with open("acmhelper.env", "w") as f:
        f.write(f"port={port}")

    print("done")
