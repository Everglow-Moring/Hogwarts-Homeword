import yaml


def get_datas():
    with open("calculator_data.yml") as f:
        datas = yaml.safe_load(f)
        return datas
