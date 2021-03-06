from .recorders import (
    recorder_torch,
    recorder_keras,
    recorder_tf,
)




class Recorder :
    def __init__(self, *args, **kwargs) :
        if kwargs["mode"] == "torch" :
            self.recorder = recorder_torch(*args, **kwargs)

        elif kwargs["mode"] == "keras" :
            #self.recorder = recorder_keras(*args, **kwargs)
            raise KeyError(
                "Recorder doesn't support {} yet. Please wait for the coming release.".format(kwargs["mode"])
            )

        elif kwargs["mode"] == "tf" :
            # self.recorder = recorder_tf(*args, **kwargs)
            raise KeyError(
                "Recorder doesn't support {} yet. Please wait for the coming release.".format(kwargs["mode"])
            )

        else :
            raise KeyError(
                "Recorder only support 'torch', 'keras' and 'tf' modes, but got {}.".format(kwargs["mode"])
            )

        self.set_models = self.recorder.set_models
        self.step = self.recorder.step
        self.epoch = self.recorder.epoch
        self.get_steps = self.recorder.get_steps
        self.get_epochs = self.recorder.get_epochs
        self.models = self.recorder.models
        self.checkpoint = self.recorder.checkpoint
        self.save_checkpoints = self.recorder.save_checkpoints
        self.save_models = self.recorder.save_models
        self.load = self.recorder.load