import json
import os
import numpy as np




class Extractor :
    def __init__(self, json_fp) :
        self.json_fp = json_fp
        self.data = self.load_json()



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



    def show_info_table(self, save_path, keys=None) :
        if keys == None :
            key_words = ["acc", "loss"]
            avg_nums = [1, 10, 50]

            table = []

            for fn in os.listdir(save_path) :
                if ".json" in fn :
                    json_fp = os.path.join(save_path, fn)

                    with open(json_fp, "r") as f :
                        record = json.load(f)
                        record = json.loads(record)

                    try :
                        if "id" in record.keys() and "data" in record :
                            for key in sorted(list(record["data"].keys())) :
                                for key_word in key_words :
                                    if key_word in key.lower() :
                                        datum = dict()
                                        datum[key] = []
                                        datum["recorder_name"] = record["recorder_name"]
                                        for num in avg_nums :
                                            value_list = [pair[1] for pair in record["data"][key]]
                                            datum.append((num, self._cal_average(value_list, num)))

                                        table.append(datum)

                    except :
                        pass
            self._print_info_table(table)



    def _print_info_table(self, table) :
        for datum in table :
            print ("|{:<10}".format(datum["recorder_name"]), end="")
            for key in datum :
                value_list = datum[key]
                for num, avg in value_list :
                    print ("|{:<10} ({:<3}): {:<12}".format(key, num, str(avg)[:8]), end="")
            print("")



    def _cal_average(self, l, last_num) :
        if len(l) == 0 :
            return None

        else :
            avg = np.array(l[-last_num:]).mean()
            return avg


