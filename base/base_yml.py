import yaml


def yml_with_file(file):
    with open("../data/" + file + ".yml", 'rb') as f:
        return yaml.load(f)


# if __name__ == '__main__':
#     yml_with_file()
