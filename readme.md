# transformers-gptq-quant

A Python-based utility for quantizing GPT models using the Hugging Face 'transformers' library.

## Description

This repository provides a Python script to quantize models with the Hugging Face 'transformers' and AutoGPTQ for 4 or 8 bit. Quantization can reduce the memory requirements of models, which may be beneficial for deployment on resource-constrained devices.

## Features

- Supports quantizing various GPTQ precisions (8bit and 4bit).
- Allows for command-line or direct script useage.
- Compatible with a range of models and datasets.

## Prerequisites

To utilize this utility, ensure that you've installed the dependencies listed in the `requirements.txt` file. You can install these using pip:

```bash
pip install -r requirements.txt
```

## Usage
You can run the script in two ways:

1. By setting hardcoded values for the parameters at the top of the script under 'Hardcoded default values'.
2. By providing command-line arguments to override the hardcoded values.

# Parameters:
- model_id: The huggingface repository or local directory containing a HF model. Example: 'teknium/openhermes', './hermes2', etc. It can be a folder or a huggingface directory.
- bits: The number of bits to use for quantization. Options: 4 and 8 - Default: `4`
- dataset: The name of the dataset to use. Example: 'wikitext2', 'c4', etc. - Default: `wikitext2`
- group_size: The size of the group for quantization. Usually a power of 2. - Default: `128`
- device_map: Device mapping configuration for loading the model. Example: 'auto', 'cpu', 'cuda:0', etc. - Default `"auto"`

## Running the script

1. **Using hardcoded values**:
    - Edit the values of `MODEL_ID`, `BITS`, `DATASET`, `GROUP_SIZE`, and `DEVICE_MAP` at the top of the script.
    - Run the script without additional command-line arguments.

2. **Using command-line arguments**:
    - Use the following syntax:
    ```bash
    python quantize.py --model_id 'teknium/openhermes' --bits 8 --dataset 'wikitext2' --group_size 32 --device_map 'auto'
    ```

    **Note**: Command-line arguments will take precedence over hardcoded values.

## Requirements

Ensure you have the necessary dependencies by checking the `requirements.txt` in this repo. Install them via:

```bash
pip install -r requirements.txt
```

## Contributing

Feel free to contribute to this project by creating issues or submitting pull requests. Ensure that your contributions are in line with the project's aim and structure.

## License

This project is open source, under the MIT license.
