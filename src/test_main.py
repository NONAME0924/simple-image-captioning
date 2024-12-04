from test_model_text import test_image_captioning
from PIL import Image
import yaml

def test_main():
    # 執行測試過程
    with open('../config/test_config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    test = test_image_captioning(config['model_name'],config['text_data_name'],config['test_data_name'],config['open_img'],config['lang'])
    test.prepare()
    print('=====================================================predict==================================================')
    print(test.test_model_text())
    print('==============================================================================================================')
# 如果直接執行此檔案，則執行 test_main()
if __name__ == "__main__":
    test_main()
