# setup
```
sudo apt-get install python3.10
python3.10 -m venv venv
. venv/bin/activate
pip install nvidia-pyindex
pip install onnx-graphsurgeon
pip install -r requirements.txt
```

# model generation
Edit the parameters in main.py, then run:
```
. venv/bin/activate
python main.py
```
