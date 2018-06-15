# buti-recorder
A python module providing clear and beautified methods to make recording and saving trained model systematic and clarified.




<br><br><br>
## Release
**Latest**
v0.0




<br><br><br>
## Requirements
**numpy**
<br>**json**
<br>**pytorch (optional)**
<br>**keras (optional)**
<br>**tensorflow (optional)**




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
* **Saving information and models**<br>
[butirecorder.Recorder](#Recorder)
<br>[butirecorder.Recorder.steps](#Recorder.steps)
<br>[butirecorder.Recorder.epochs](#Recorder.epochs)
<br>[butirecorder.Recorder.set_models()](#Recorder.set_models)
<br>[butirecorder.Recorder.step()](#Recorder.step)
<br>[butirecorder.Recorder.epoch()](#Recorder.epoch)
<br>[butirecorder.Recorder.checkpoint()](#Recorder.checkpoint)
<br>[butirecorder.Recorder.save_checkpoints()](#Recorder.save_checkpoints)
<br>[butirecorder.Recorder.save_models()](#Recorder.save_models)
<br>[butirecorder.Recorder.load()](#Recorder.load)

* **Dumping saved information**
Unfinished.


<br><h3 id="Recorder"> butirecorder.Recorder(mode, save_mode, save_path=None, recorder_name=None, models={}, desp="")</h3>

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


<br><h3 id="Recorder.steps"> butirecorder.Recorder.steps </h3>

* **Type**
<br>int

* **Notes**
<br>Obtain training steps.
<br>Must call `butirecorder.Recorder.step()` to update `butirecorder.Recorder.steps` after one step.


<br><h3 id="Recorder.epochs"> butirecorder.Recorder.epochs </h3>

* **Type**: int

* **Notes**
<br>Obtain training epochs.
<br>Must call `butirecorder.Recorder.epoch()` to update `butirecorder.Recorder.epochs` after one epoch.
 

<br><h3 id="Recorder.set_models"> butirecorder.Recorder.set_models(models)</h3>

* **Type**
<br>function

* **Parameters** 
<br>***models*** [dict]
Set a dict parameter for Recorder.models.

* **Descriptions**
***models***
<br>Example
```python
models = {
    "gan_generator": model_gn,
    "gan_discriminator": model_dn,
}

Recorder.set_models(models)
```

* **Notes** 
<br>Note that it is required before call `butirecorder.Recorder.save()` if you don't load any models
by calling `butirecorder.Recorder.save()`


<br><h3 id="Recorder.step"> butirecorder.Recorder.step() </h3>

* **Type**
<br>function

* **Notes**
<br>Update butirecorder.Recorder.steps.
<br>Class Recorder would save training process information with corresponding step. Must call this function after one step in
your training process to save correct process information.
<br>Note that Recorder and .json file will save the current step, so you can retrieve the saved step next time when you
resume training.


<br><h3 id="Recorder.epoch"> butirecorder.Recorder.epoch() </h3>

* **Type**
<br>function

* **Notes**
<br>Update butirecorder.Recorder.epochs.
<br> Note that Recorder and .json file will save the current step, so you can retrieve the saved step next time when you
resume training.


<br><h3 id="Recorder.checkpoint"> butirecorder.Recorder.checkpoint(data) </h3>

* **Type**
<br>function

* **Parameters**
<br>***data*** [dict]

* **Descriptions**
***data***
<br>Save the training process information customized by you with corresponding step.
Must call `butirecorder.Recorder.save_checkpoints()` to save the record into .json file.
<br>Example (for Pytorch)
```python
from butirecorder import Recorder
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
```

Then, the saved .json file would contain these data like this:
```
{
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
```
 
 
<br><h3 id="Recorder.save_checkpoints"> butirecorder.Recorder.save_checkpoints() </h3>

* **Type**
<br>function

* **Notes**
<br>Save/update training process information `Recorder.data` into .json.
<br>`Recorder.recorder_name` and `Recorder.save_path` is required before saving .json file.
<br>Note that you must call this function to write/update `Recorder.data` into .json file, `butirecorder.Recorder.checkpoint()`
only save them (on RAM) but not write them into .json.
<br>You may raise the question why we split saving task into two functions. The reason is that you may call `butirecorder.Recorder.checkpoint()`
frequently, but if we write every updated `Recorder.data` into .json file, it may cause writing crash/problem due to extremely high frequency.
So, do not call `butirecorder.Recorder.save_checkpoints()` too frequently (recommend <1~50 1/s depending on your computer)


<br><h3 id="Recorder.save_models"> butirecorder.Recorder.save_models() </h3>

* **Type**
<br>function

* **Notes**
<br>Save the models in `Recorder.models`.
<br>`Recorder.recorder_name`, `Recorder.save_path`, `Recorder.save_mode` and `Recorder.models` are required
before saving state_dicts/models.
<br>Note that the saving method would depend on parameter `Recorder.save_mode` which is described above.
<br>The save model files' names would be the "Recorder.recorder_name" + model_name.
<br>Example
```python
recorder = Recorder({
    ...,
    recorder_name: "trainQQ",
    save_path: "./test/",
    models: {
        "CNN": cnn,
        "Lstm": lstm,
    }
})

...

recorder.save_models()
```

Then, it will save models like this
```console
$ ls ./test/
trainQQ_CNN.pkl   trainQQ_Lstm.pkl   trainQQ.json
```


<br><h3 id="Recorder.load"> butirecorder.Recorder.load(json_fp) </h3>

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




<br><br><br>
## Examples
### Initial and save (on Pytorch)
```python
import pytorch
from butirecorder import Recorder
from my_model import gan_gn, gan_dn

gn = gan_gn()
dn = gan_dn()

### init Recorder
recorder = Recorder(
    mode="torch",
    recorder_name="gan",
    save_mode="state_dict",
    save_path="./",
    models={
        "gn": gn,
        "dn": dn,
    }
)

### your training
for i in range(1000) :      # train 1000 steps
    print ("training step:", recorder.steps)
    # your training in one step
    ...
    ...
    acc = ...
    real_loss = ...
    fake_loss = ...
    ...
    ...
    
    recorder.checkpoint({
        "acc": acc,
        "real_loss": real_loss,
        "fake_loss": fake_loss,
    })
    
    recorder.step()     # required, to add 1 to step
    
    if recorder.steps % 10 == 0 :
        recorder.save_checkpoints()
    
    if recorder.steps % 50 == 0 :
        recorder.epoch()
    
    if recorder.steps % 100 == 0 :
        recorder.save_models()
</code></pre>
Then, it will create files in your dir path:
<pre><code>$ ls ./
gan.json   gan_gn.pkl   gan_dn.pkl 
```

<br><br>
### Initial and load (on Pytorch)
```python
import pytorch
from butirecorder import Recorder
from my_model import gan_gn, gan_dn
gn = gan_gn()
dn = gan_dn()

### init Recorder
recorder = Recorder(
    mode="torch",
    save_mode="state_dict",     # how you save, how you load
    models={
        "gn": gn,
        "dn": dn,
    },
    #save_path="./xxx/yyy/",    #optional, if you want to set one new save_path 
)

### load Recorder and models
json_fp = "./gan.json"
models = recorder.load(json_fp)

gn = models["gn"]
dn = models["dn"]

### your training
for i in range(100) :       # resume training from the step stored last time
    print ("training step:", recorder.steps)
    # your training in one step
    ...
    ...
    acc = ...
    real_loss = ...
    fake_loss = ...
    ...
    ...
    
    recorder.checkpoint({
        "acc": acc,
        "real_loss": real_loss,
        "fake_loss": fake_loss,
    })
    
    recorder.step()     # required, to add 1 to step
    
    if recorder.steps % 10 == 0 :
        recorder.save_checkpoints()
    
    if recorder.steps % 50 == 0 :
        recorder.epoch()
    
    if recorder.steps % 100 == 0 :
        recorder.save_models()
```