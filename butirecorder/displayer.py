import os
import json
import numpy as np




def show_info_table(dir_path, keys=None, avg_nums=[1, 10]) :
    if keys == None :
        key_words = ["acc", "loss"]

        table = []

        for fn in os.listdir(dir_path) :
            if ".json" in fn :
                json_fp = os.path.join(dir_path, fn)

                with open(json_fp, "r") as f :
                    record = json.load(f)
                    record = json.loads(record)

                try :
                    if "id" in record and "data" in record :
                        datum = dict()
                        datum["recorder_name"] = record["recorder_name"]
                        for key in sorted(list(record["data"].keys())) :
                            for key_word in key_words :
                                if key_word in key.lower() :
                                    datum[key] = []
                                    for num in avg_nums :
                                        value_list = [pair[1] for pair in record["data"][key]]
                                        datum[key].append((num, _cal_average(value_list, num)))

                        if len(list(datum.keys())) > 1 :
                            table.append(datum)

                except :
                    pass
        _print_info_table(table)

    else :
        table = []

        for fn in os.listdir(dir_path) :
            if ".json" in fn :
                json_fp = os.path.join(dir_path, fn)

                with open(json_fp, "r") as f :
                    record = json.load(f)
                    record = json.loads(record)

                try :
                    if "id" in record and "data" in record :
                        datum = dict()
                        datum["recorder_name"] = record["recorder_name"]
                        for key in sorted(list(record["data"].keys())) :
                            if key.lower() in [k.lower() for k in keys] :
                                datum[key] = []
                                for num in avg_nums :
                                    value_list = [pair[1] for pair in record["data"][key]]
                                    datum[key].append((num, _cal_average(value_list, num)))

                        if len(list(datum.keys())) > 1 :
                            table.append(datum)

                except :
                    pass
        _print_info_table(table)



def _print_info_table(table) :
    for datum in table :
        print ("|{:<10}".format(datum["recorder_name"]), end="")
        for key in datum :
            if key != "recorder_name" :
                value_list = datum[key]
                for (num, avg) in value_list :
                    print ("|{:<23}".format("{} ({}): {}".format(key, num,str(avg)[:7])), end="")
        print("")



def _cal_average(l, last_num) :
    if len(l) < last_num :
        return None

    else :
        avg = np.array(l[-last_num:]).mean()
        return avg