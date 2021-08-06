import torch

import yaml
import ast


print(torch.__version__)
cd /content/
curl -L "https://www.dropbox.com/s/0da6paqyt6jg0x1/video2.zip?dl=0" > video2.zip; unzip video2.zip; 
curl -L "https://www.dropbox.com/s/ywxpemusw6wk92s/best.zip?dl=0" > best.zip; unzip best.zip; 
curl -L "https://www.dropbox.com/s/8lm217rrekc08yt/best_60_weights.zip?dl=0" > best_60_weights.zip; unzip best_60_weights.zip; 
curl -L "https://www.dropbox.com/s/oovmwed5zotp554/yaml8.zip?dl=0" > yaml8.zip; unzip yaml8.zip; rm yaml8.zip
cd /content/yolor
bash scripts/get_pretrain.sh

with open("/content/data.yaml", 'r') as stream:
    names = str(yaml.safe_load(stream)['names'])

namesFile = open("../data.names", "w+")
names = ast.literal_eval(names)
for name in names:
  namesFile.write(name +'\n')
namesFile.close()
from IPython.display import YouTubeVideo, display
video = YouTubeVideo("pGgM3c1e8vQ", width=500)
display(video)
python detect.py --weights "/content/best.pt" --conf 0.3 --source /content/yolor/video4.mp4 --names ../data.names --save-txt  
