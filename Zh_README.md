# 簡單實做image captioning
[English](.README.md)

## 安裝

1. 安裝所需的依賴套件：
    ```bash
    pip install -r requirements.txt
    ```

2. 下載必要的模型：
    ```bash
    python -m spacy download en_core_web_md
    ```

## 訓練

1. 進入 `src` 目錄：
    ```bash
    cd src
    ```

2. 執行訓練腳本：
    ```bash
    python main.py
    ```

## 設定

- 若要修改訓練參數，請編輯與 `src` 同層級的 `config.yaml` 檔案。

## 測試

1. 測試請使用以下腳本：
    ```bash
    python test-main.py
    ```

## 授權

在此加入相關的授權資訊（若有）。
