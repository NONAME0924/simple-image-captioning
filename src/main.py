import yaml
import create_datasets  # 确保用实际模块名替换 your_module
import setting_and_training
import warnings
import os
import pandas as pd
import torch


def main():
    # 读取配置文件
    
    print('=========================================Start execution=======================================================')
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print('device:',device)
    model_use = setting_and_training.ViTLSTM()
    
    with open('../config/create_config.yaml', 'r') as file:
        config = yaml.safe_load(file)
        
    if config['self_data_name']:
        if os.path.splitext(config['self_data_name'])[1] == '.xlsx':
            df = pd.read_excel(config['self_data_name'])
            csv_name = os.path.splitext(config['self_data_name'])[0]+'.csv'
            df.to_csv(csv_name)
            train_loader, dataset = model_use.get_datasets(csv_name)
        else:
            train_loader, dataset = model_use.get_datasets(config['self_data_name'])
        print('==========================================================================================================')
        print("load datasets are completed.")
        print('==========================================================================================================')
        
    else:
        dataset_creator = create_datasets.Create_datasets(
            excel_name=config['excel_name'],
            csv_name=config['csv_name'],
            datasets_name=config['datasets_name'],
            lang=config['lang'],
        )
    
        dataset_creator.creat_excel()
        df = dataset_creator.creat_datasets(total=config['total'])
        dataset_creator.continue_translate_xlsx(df)
        train_loader, dataset = model_use.get_datasets(dataset_creator.csv_name)
        print('==========================================================================================================')
        print("create datasets are completed.")
        print('==========================================================================================================')

    
    print('==========================================================================================================')
    print('start training.')
    print('==========================================================================================================')
    model = model_use.setting_and_training(train_loader, dataset)

    print('==========================================================================================================')
    print('training endding.')
    print('==========================================================================================================')
    model_use.save(model)


    print('==========================================================================================================')
    print('All task are completed.')
    print('==========================================================================================================')

if __name__ == "__main__":
    main()
