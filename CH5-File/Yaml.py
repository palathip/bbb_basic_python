# Loader = yaml.FullLoader

def readYaml():
    import yaml
    with open("myyaml.yaml") as f:
        profile = yaml.load(f)
        print  profile["bob"]
        print  profile["alice"]["color"]
# readYaml()