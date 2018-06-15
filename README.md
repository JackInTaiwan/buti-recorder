# buti-recorder
A python module providing clear and beautified methods to make recording and saving trained model systematic and clarified.




<br><br><br>
## Introduction
We provide a systematic package tool to make recording and saving models much easier and clear when you're 
training models for deep learning.
<br><br>We're scheduled to support three frameworks :
* Pytorch
* Keras (Not support yet)
* Tensorflow (Not support yet)

<br>You can use butirecorder to record the information while training on one of the three frameworks.




<br><br><br>
## Installation
Here are two main methods provided to allow you access butirecorder 
package :

#### 1. Install through pip/pip3 (Recommended)
You can use pip/pip3 to install the package. Please run the following in your terminal
<br>`pip3 install git+https://github.com/JackInTaiwan/buti-recorder.git`
<br>As done, you can import the package in your codes.

#### 2. Install through setup.py
You can use setpy.py to install the package. Please run the following in your terminal
<br>`python3 setup.py install`
<br>Note that `python3` is to run your python according to your python version.
<br>As done, you can import the package in your codes.




<br><br><br>
## Documentation
Beautirecorder support tow main functions :
* Saving information and models
* Dumping saved information


<h3 id="test"> butirecorder.Recorder(mode, save_mode, save_path=None, recorder_name=None, models={}, desp="")</h3>

* **Type**
<br>class

* **Parameters**
<br>***mode*** [str] [options: ("torch", "keras", "tf")]
<br>***recorder_name*** [str]
<br>***save_mode*** [str] [options: ("state_dict", "model")]
<br>***save_path*** [str]
<br>***models*** [dict]
<br>***desp*** [str]

* **Descriptions**
<br>***mode***
<br>The framework you use to train models. Only "torch" (pytorch) can be accessed now.
<br>***recorder_name***
<br> The recorder's name. Recorder would save the training information in a .json file with recorder_name.
<br>Examples would be given below to show the format naming rules.
<br>***save_mode*** 
<br> The way you save your trained models. Here are two usual ways to save model in Pytorch.
<br>1. saving whole model `torch.save(model)`
<br>2. saving model's state_dict `tor.save(model.state_dict())`
<br>If you're used to carrying out method 1, set save_mode = "model"; otherwise, set save_mode = "state_dict". Then Recorder would
save and load in the corresponding way.
<br>***save_path***
<br> The dir path where you want models and .json file to be stored. Note that we store models and .json in
the same dir path, don't split them into two dir path manually, or you will get finding dir error. 
<br>***models***
<br> We provide storing not only one model, so the format dict for models :
<br>```models={
"model1_name": model1, "model2_name":model2,...}```
<br>Examples would be given below.span>
<br>***desp*** 
<br>Any extra description you want to mark, e.g. training data, training mood, model version, model skills , and so on.
<br>The descriptoin would be stored in .json also, then you can access in future if needed.


### *butirecorder.Recorder.steps*
* **Type**
<br>int

* **Notes**
<br>Obtain training steps.
<br>Must call `butirecorder.Recorder.step()` to update `butirecorder.Recorder.steps` after one step.


### *butirecorder.Recorder.epochs*
* **Type**: int

* **Notes**
<br>Obtain training epochs.
<br>Must call `butirecorder.Recorder.epoch()` to update `butirecorder.Recorder.epochs` after one epoch.
 

### *butirecorder.Recorder.set_models(models)*
* **Type**
<br>function

* **Parameters** 
<br>***models*** [dict]
Set a dict parameter for Recorder.models.

* **Descriptions**
***models***
<br>Example,
<pre><code>models = {
    "gan_generator": model_gn,
    "gan_discriminator": model_dn,
}

Recorder.set_models(models)
</code></pre>

* **Notes** 
<br>Note that it is required before call `butirecorder.Recorder.save()` if you don't load any models
by calling `butirecorder.Recorder.save()`


### butirecorder.Recorder.step()
* **Type**
<br>function

* **Notes**
<br>Update butirecorder.Recorder.steps.
<br>Class Recorder would save training process information with corresponding step. Must call this function after one step in
your training process to save correct process information.
<br>Note that Recorder and .json file will save the current step, so you can retrieve the saved step next time when you
resume training.


### butirecorder.Recorder.epoch()
* **Type**
<br>function

* **Notes**
<br>Update butirecorder.Recorder.epochs.
<br> Note that Recorder and .json file will save the current step, so you can retrieve the saved step next time when you
resume training.


### butirecorder.Recorder.checkpoint(data)
* **Type**
<br>function

* **Parameters**
<br>***data*** [dict]

* **Descriptions**
***data***
<br>Save the training process information customized by you with corresponding step.
Must call `butirecorder.Recorder.save_checkpoints()` to save the record into .json file.
<br>Example (for Pytorch)
<pre><code>from butirecorder import Recorder
from your_model import your_model

model_1 = your_model()
model_2 = your_model()
recorder = Recorder(
    mode="torch",
    ...,    # parameters
)

recorder.set_models({
    "CNN_1": model_1, 
    "CNN_2": model_2,   
})
 
for i in range(10) :
     recorder.checkpoint({
        "accuracy": 0.1 * i,
        "loss": 0.01,
        "QQ": True,
        "whatever you want to save": True
     })
     recorder.step()

recorder.save_checkpoints()
</code></pre>

Then, the saved .json file would contain these data like this:
<pre><code>{
    "recorder_name": ...,
    ...,
    "data": {
        "accuracy": [(1, 0.0), (2, 0.1), (3, 0.2), ...],
        "loss": [(1, 0.01), (2, 0.01), (3, 0.01), ...],
        "QQ": [(1, True), (2, True), (3, True), ...],
        "whatever you want to save": [(1, True), (2, True), (3, True), ...],
    },
    ...
}
</code></pre>
 
 
### butirecorder.Recorder.save_checkpoints()
* **Type**
<br>function

* **Notes**
<br>Save/update training process information `Recorder.data` into .json.
<br>Note that you must call this function to write `Recorder.data` into .json file, `butirecorder.Recorder.checkpoint()`
only save them (on RAM) but not write into .json.
<br>You may raise the question why we split saving task into two functions. The reason is that you may call `butirecorder.Recorder.checkpoint()`
frequently, but if we write every updated `Recorder.data` into .json file, it may cause writing crash/problem due to extremely high frequency.
So, do not call `butirecorder.Recorder.save_checkpoints()` too frequently (recommend <1~50 1/s depending on your computer)


### butirecorder.Recorder.save_models()
* **Type**
<br>function
<br>Save the models in `Recorder.models`.
<br>Note that the saving method would depend on parameter `Recorder.save_mode` which is described above.


### butirecorder.Recorder.load(json_fp)
* **Type**
<br>function

* **Parameters**
<br>***return*** [dict]
<br>

* **Descriptions**
<br>***return***
<br>return a dict with loaded models,
<br>Example (on Pytorch)
<pre><code>{
    "CNN_1": cnn_1,
    "CNN_2": cnn_2, 
}
# cnn_1 and cnn_2 is torch.module
</code></pre>

* **Notes**
<br> Loading models and Recorder.data from .json file.
<br> Parameters `Recorder.models`, `Recorder.mode` and `Recorder.save_mode` are required before loading.
<br> Note that if you set parameter `Recorder.save_path` before loading, then `Recorder` would change the dir path of `Recorder.save_path`
instead of dir path saved in previous json file. If you don't want to change the dir path saved in .json, then you just don't set parameter
`Recorder.save_path`.

[aaa](#test)