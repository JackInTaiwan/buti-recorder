import json
import os
import numpy as np




class Extractor :
    def __init__(self, json_fp) :
        self.json_fp = json_fp
        self.data = self.load_json()
        self.save_path = self.data["save_path"]



    def load_json(self) :
        with open(self.json_fp, "r") as f :
            data = json.load(f)
            data = json.loads(data)

        return data



    def get_data(self, key) :
        pair_list = self.data[key]
        step_list = [pair[0] for pair in pair_list]
        value_list = [pair[1] for pair in pair_list]

        return step_list, value_list