import torch
from tqdm import tqdm
import torch.nn as nn
import torch.optim as optim
import torchvision.transforms as transforms
from torch.utils.tensorboard import SummaryWriter
import pandas as pd
from get_loader_zh_tw import get_loader_zh_tw
from get_loader_en import get_loader_en
from model import CNNtoLSTM
import torch
import torchvision.transforms as transforms
from PIL import Image
import time
import transform
import os

class test_image_captioning():
    def __init__(self, model_name,text_data_name,test_data_name,open_img,lang):
        self.model_name = model_name
        self.model = torch.load('the_best_model/'+self.model_name)
        self.text_data_name = text_data_name
        self.test_data_name = test_data_name
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.open_img = open_img
        self.lang = lang
        self.test_loader = None
        self.dataset = None
        self.test_df = None

    
    def prepare(self):
        if os.path.splitext(self.text_data_name)[1] == '.xlsx':
            df = pd.read_excel(self.text_data_name)
            csv_name = os.path.splitext(self.text_data_name)[0]+'.csv'
            df.to_csv(csv_name)
            self.text_data_name = csv_name
            print('自動將excel轉csv')
        elif os.path.splitext(self.text_data_name)[1] == '.csv':
            pass
        else:
            print('資料不符合格式')

        if self.lang == 'zh_tw':
            self.test_loader, self.dataset = get_loader_zh_tw(
                root_folder="./",
                annotation_file=self.text_data_name,
                transform=transform,
                num_workers=8,
                batch_size = 128,
            )
        elif self.lang =='en':
            self.test_loader, self.dataset = get_loader_en(
                root_folder="./",
                annotation_file=self.text_data_name,
                transform=transform,
                num_workers=8,
                batch_size = 128,
            )

        if os.path.splitext(self.test_data_name)[1] == '.xlsx':
            df = pd.read_excel(self.test_data_name)
            csv_name = os.path.splitext(self.test_data_name)[0]+'.csv'
            df.to_csv(csv_name)
            self.test_data_name = csv_name
            print('自動將excel轉csv')
            self.test_df = pd.read_csv(csv_name)
        elif os.path.splitext(self.test_data_name)[1] == '.csv':
            self.test_df = pd.read_csv(self.test_data_name)
        else:
            print('資料不符合格式')
            
        
    def test_model_text(self):
        torch.backends.cudnn.enabled = False
        change = transform.transform()
        img = change(Image.open(self.test_df['image'][self.open_img-1]).convert("RGB")).unsqueeze(0)
        pre = self.model.caption_image(img.to(self.device), self.dataset.vocab)
        return pre