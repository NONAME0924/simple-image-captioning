# simple image captioning


[繁體中文](Zh_README.md)。

## Installation

1. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Download the necessary model:
    ```bash
    python -m spacy download en_core_web_md
    ```

## Training

1. Navigate to the `src` directory:
    ```bash
    cd src
    ```

2. Run the training script:
    ```bash
    python main.py
    ```

## Configuration

- To modify the training parameters, edit the `.yaml` files inside the `config` directory.
  
## Testing

1. For testing, use the following script:
    ```bash
    python test_main.py
    ```

## License

Include any licensing information here, if applicable.
