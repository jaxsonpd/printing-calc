from configuration import Config

theme = Config.load_json("./src/theme.json")

print(theme.colours.equation)