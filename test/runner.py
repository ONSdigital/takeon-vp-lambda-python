import json

class Runner:
    def __init__(self, input_data):
        self.input_data = input_data
        self.loaded_data = None
    
    def load_data(self):
        if isinstance(self.input_data, str):
            self.loaded_data = json.loads(self.input_data)
        else:
            self.loaded_data = self.input_data

    def run_rule(self):
        for question in self.loaded_data["input"]:
            if question["response"] != "":
                question["triggered"] = True
            else:
                question["triggered"] = False
        return self.loaded_data