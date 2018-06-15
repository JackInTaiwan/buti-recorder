import os
import uuid
import json
import cv2
import torch as tor




class Recorder :
    def __init__(self, mode, save_mode, save_path, recorder_name=None, models={}, desp="") :
        self.id = uuid.uuid1().hex
        self.mode = mode
        self.recorder_name = recorder_name
        self.save_mode = save_mode
        self.save_path = save_path
        self.models = models
        self.model_names = list(models.keys()) if len(models.keys()) > 0 else None

        self.desp = desp
        self.data = dict()

        self.steps = 0
        self.epochs = 0

        if not os.path.exists(os.path.join(self.save_path, "{}.json".format(self.recorder_name))) :
            self.save_checkpoints()


    def __setattr__(self, key, value) :
        # checking types
        attr_types = {
            "recorder_name": (str, type(None),),
            "mode": str,
            "save_path": (str, type(None),),
            "models": (dict, type(None),),
        }

        for attr in attr_types :
            if key == attr and not isinstance(value, attr_types[attr]) :
                raise TypeError("Recorder class parameter '{}' needs type {} but got {}.".format(key, attr_types[attr], type(value)))

        # checking opts
        if key == "mode" :
            opts = ["torch", "keras", "tf", ]
            if value not in opts :
                raise ValueError("Recorder class parameter '{}' requires one of {}, but got '{}'"
                                 .format(key, "/".join(opts), value))

        if key == "save_mode" :
            opts = ["state_dict", "model"]
            if value not in opts :
                raise ValueError("Recorder class parameter '{}' requires one of {}, but got '{}'"
                                 .format(key, "/".join(opts), value))

        super().__setattr__(key, value)


    def set_models(self, models) :
        self.models = models
        self.model_names = list(models.keys()) if len(list(models.keys())) > 0 else None


    def load_recorder(self, recorder_fp) :
        with open(recorder_fp) as f :
            data = json.load(f)
        data = json.loads(data)
        self.id = data["id"]
        self.recorder_name = data["recorder_name"]
        self.desp = data["desp"]
        self.mode = data["mode"]
        self.model_names = data["model_names"]
        self.save_path = data["save_path"] if not self.save_path else self.save_path
        self.data = data["data"]
        self.steps = data["steps"]
        self.epochs = data["epochs"]

        self.save_checkpoints()


    def load_models(self) :
        import torch as tor

        if len(self.models) > 0 :
            for name in self.models :
                model_fp = os.path.join(self.save_path, "{}.pkl".format(name))
                if self.save_mode == "state_dict" :
                    model_state_dict = tor.load(model_fp)
                    self.models[name].load_state_dict(model_state_dict)

        else :
            raise ValueError("Recorder parameter 'model_name' length must > 0, but got 0.\
             You may give a wrong json file, or you don't save the json file correctly.")


    def load(self, recorder_fp) :
        self.load_recorder(recorder_fp)
        self.load_models()

        return self.models


    def checkpoint(self, data) :
        steps = self.steps
        print (self.data)
        for key in data :
            if key not in self.data :
                self.data[key] = [(steps, data[key])]
            else :
                if not self.check_step_duplicate(steps, self.data[key]) :
                    self.data[key].append((steps, data[key]))
                else :
                    self.data[key][-1] = (steps, data[key])


    def check_step_duplicate(self, steps, list) :
        step_list = [pair[0] for pair in list]
        if steps in step_list :
            if len(step_list) > 1 and step_list.index(steps) != len(step_list) -1 :
                raise ValueError("Method checkpoint requires no duplicate step as checkpoint.")
            else :
                return True

        else :
            return False


    def save_checkpoints(self) :
        save_fp = "{}.json".format(os.path.join(self.save_path, self.recorder_name))

        output = dict()
        output["id"] = self.id
        output["recorder_name"] = self.recorder_name
        output["save_path"] = self.save_path
        output["mode"] = self.mode
        output["model_names"] = self.model_names
        output["desp"] = self.desp
        output["steps"] = self.steps
        output["epochs"] = self.epochs
        output["data"] = self.data
        output_json = json.dumps(output)

        with open(save_fp, "w") as f :
            json.dump(output_json, f)


    def save_models(self) :
        if self.save_mode == "state_dict" :
            self.save_state_dict()

        elif self.save_mode == "model" :
            # to be finished
            pass


    def save_state_dict(self) :
        if len(self.models) < 1 :
            raise ValueError("Method save_state_dict requires Recorder.model_names length > 0, but got {}.".format(len(self.models)))

        else :
            if not isinstance(self.models, dict) and len(self.model_names) != 1 :
                raise ValueError("Method save_state_dict requires that type of Recorder.models is dict, or length of Recorder.model_names is 1.")

            else :
                for key in self.models :
                    model_save_fp = "{}.pkl".format(os.path.join(self.save_path, key))
                    tor.save(self.models[key].state_dict(), model_save_fp)

                self.save_mode = "state_dict"


    def step(self) :
        self.steps += 1


    def epoch(self) :
        self.epochs += 1