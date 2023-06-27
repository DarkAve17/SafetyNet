# SafetyNet
SafetyNet is an implementation of Bi-LSTM RNN to process live feed from webcam to detect violence. <br>
It is aimed to be implemented with police bodycams to help prevent accidental loss of lives due to misinterpretation of actions by law enforcement officials. <br>
There is also a deployment version of SafetyNet on Huggingface Spaces, which can be used as a simple Threat Detection System over pre-recorded mp4/avi/webm videos. Visit the Space [here](https://huggingface.co/spaces/jeonananya/threat_detection).

## Set Up
1. Download the Real Life Violence Situations Dataset from Kaggle. Download link given in [requirements.txt](https://github.com/ananyaraju/SafetyNet/blob/main/assets/requirements.txt).
2. Unzip the dataset and move it to ASSETS folder.
3. Open [RLVDetection_Model.ipynb](https://github.com/ananyaraju/SafetyNet/blob/main/RLVDetection_Model.ipynb) notebook to train and save the model.
4. To load and test the model with real-time footage, use [SafetyNet.ipynb](https://github.com/ananyaraju/SafetyNet/blob/main/SafetyNet.ipynb).
