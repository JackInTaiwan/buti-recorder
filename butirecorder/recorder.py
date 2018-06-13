import os
import uuid
import json
import cv2
import torch as tor




class Recorder :
    def __init__(self, mode, recorder_name, save_path=None, models=None, info="") :
        self.id = uuid.uuid1().hex
        self.mode = mode
        self.recorder_name = recorder_name
        self.save_path = save_path
        self.models = models
        self.model_names = list(models.keys()) if len(models.keys()) > 0 else None

        self.info = info
        self.data = dict()

        self.step = 0
        self.epoch = 0


    def __setattr__(self, key, value) :
        # checking types
        attr_types = {
            "mode": str,
            "save_path": str,
            "model_names": dict,
        }

        for attr in attr_types :
            if key == attr and not isinstance(value, attr_types[attr]) :
                raise TypeError("Recorder class attribute '{}' needs type {} but got {}.".format(attr_types[attr], type(value)))

        # checking opts
        if key == "mode" :
            mode_opts = ["torch", "keras", "tf", ]
            if value not in mode_opts :
                raise ValueError("Recorder class attribute '{}' requires one of {}, but got '{}'"
                                 .format(key, "/".join(mode_opts), value))

        super().__setattr__(key, value)


    def set(self, save_path, model_names) :
        self.save_path = save_path
        self.model_names = model_names


    def load_recorder(self, recorder_fp) :
        with open(recorder_fp) as f :
            data = json.load(f)
        data = json.loads(data)

        self.id = data["id"]
        self.info = data["info"]
        self.mode = data["mode"]
        self.model_names = data["model_names"]
        self.data = data["data"]
        self.step = data["step"]
        self.epoch = data["epoch"]

        split_index = 0
        while recorder_fp.index("/", split_index) != split_index :
            split_index = recorder_fp.index("/", split_index)

        save_path = recorder_fp[:split_index] if split_index != 0 else "./"
        recorder_name = recorder_fp[split_index:].strip(".json") if "/" in recorder_fp else recorder_fp.strip(".json")

        self.save_path = save_path
        self.recorder_name = recorder_name


    def load_models(self) :
        import torch as tor

        if len(self.model_names) > 0 :
            for model_name in self.model_names :
                model_fp = os.path.join(self.save_path, "{}.pkl".format(model_name))
                model_state = tor.load(model_fp)
                self.models[model_name] = model_state

        else :
            raise ValueError("Recorder attribute 'model_name' length must > 0, but got 0.\
             You may give a wrong json file, or you don't save the json file correctly.")


    def load(self, recorder_fp, models) :
        self.load_recorder(recorder_fp)
        self.load_models(models)

        return self.models


    def checkpoint(self, data) :
        step = self.step
        for key in data :
            if key not in self.data :
                self.data[key] = [(step, data[key])]
            else :
                if not self.check_step_duplicate(step, data[key]) :
                    self.data[key].append((step, data[key]))
                else :
                    self.data[key][-1] = (step, data[key])


    def check_step_duplicate(self, step, list) :
        step_list = [pair[0] for pair in list]
        if step in step_list :
            if len(step_list) > 1 and step_list.index(step) != len(step_list) -1 :
                raise ValueError("Method checkpoint requires no duplicate step as checkpoint.")
            else :
                return True

        else :
            return False


    def save_record(self) :
        save_fp = os.path.join(self.save_path, self.recorder_name)

        output = dict()
        output["id"] = self.id
        output["save_path"] = self.save_path
        output["mode"] = self.mode
        output["model_names"] = self.model_names
        output["info"] = self.info
        output["step"] = self.step
        output["epoch"] = self.epoch
        output["data"] = self.data

        output_json = json.dumps(output)

        with open(save_fp, "w") as f :
            json.dump(output_json, f)


    def save_parameters(self, parameters_dict) :
        if len(self.models) < 1 :
            raise ValueError("Method save_models requires Recorder.model_names \
            length > 0, but got {}.".format(len(self.models)))

        else :
            if not isinstance(parameters_dict, dict) and len(self.model_names) != 1 :
                raise ValueError("Method save_parameters requires that type of  \
                parameters_dict is dict, or length of Recorder.model_names is 1.")

            else :
                for key in parameters_dict :
                    model_save_fp = os.path.join(self.save_path, key)
                    tor.save(parameters_dict[key], model_save_fp)


    def step(self) :
        self.step += 1


    def epoch(self) :
        self.epoch += 1


