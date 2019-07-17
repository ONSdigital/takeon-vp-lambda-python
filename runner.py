import json

class Runner:
    def __init__(self, input_data):
        self.input_data = input_data
        self.loaded_data = None
        self.data_to_return = {}
    
    def load_data(self):
        if isinstance(self.input_data, str):
            self.loaded_data = json.loads(self.input_data)
        else:
            self.loaded_data = self.input_data

    def run_rule(self):
        print(self.loaded_data)
        if self.loaded_data["primaryValue"] != "":
            self.data_to_return["triggered"] = True
            self.data_to_return["valueFormula"] = "{} != \"\"".format(self.loaded_data["primaryValue"])
        else:
            self.data_to_return["triggered"] = False
            self.data_to_return["valueFormula"] = "{} = \"\"".format(self.loaded_data["primaryValue"])
        self.data_to_return["questionCode"] = self.loaded_data["questionCode"]
        print("Value to return: {}".format(self.data_to_return))
        return self.data_to_return
