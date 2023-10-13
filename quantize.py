"""
README:

This Python script is designed to quantize a GPT model using the Hugging Face 'transformers' library.
You can run this script in two ways:
1. By setting hardcoded values for the parameters at the top of this script under 'Hardcoded default values'.
2. By providing command-line arguments to override the hardcoded values.

Parameters:

- model_id: The identifier of the pre-trained GPT model. Example: 'gpt2', 'gpt2-medium', etc.
- bits: The number of bits to use for quantization. Example: 8, 16, etc.
- dataset: The name of the dataset to use. Example: 'wikitext2', 'wikitext103', etc.
- group_size: The size of the group for quantization. Usually a power of 2.
- device_map: Device mapping configuration for loading the model. Example: 'auto', 'cpu', 'cuda:0', etc.

Usage:

1. To use hardcoded values:
    - Edit the values of MODEL_ID, BITS, DATASET, GROUP_SIZE, and DEVICE_MAP at the top of this script.
    - Run the script.

2. To use command-line arguments:
    - Use the following syntax:
        python script_name.py --model_id 'gpt2' --bits 8 --dataset 'wikitext2' --group_size 32 --device_map 'auto'

Note: Command-line arguments will take precedence over hardcoded values.
"""

import argparse
import auto_gptq
from transformers import GPTQConfig, AutoModelForCausalLM, AutoTokenizer

# Hardcoded default values
MODEL_ID = "teknium/OpenHermes-2-Mistral-7B"
BITS = 4
DATASET = "wikitext2"
GROUP_SIZE = 128
DEVICE_MAP = "auto"

def main(model_id, bits, dataset, group_size, device_map):
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    gptq_config = GPTQConfig(bits=bits, dataset=dataset, tokenizer=tokenizer, group_size=group_size)
    model = AutoModelForCausalLM.from_pretrained(model_id, quantization_config=gptq_config, device_map=device_map)
    model.to("cpu")
    model.save_pretrained(f"{model_id}_{bits}bit")
    tokenizer.save_pretrained(f"{model_id}_{bits}bit")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Quantize a GPT model. Run with --help for more info.")
    parser.add_argument("--model_id", type=str, help="The pretrained model ID.")
    parser.add_argument("--bits", type=int, help="Number of bits for quantization.")
    parser.add_argument("--dataset", type=str, help="The dataset to use.")
    parser.add_argument("--group_size", type=int, help="Group size for quantization.")
    parser.add_argument("--device_map", type=str, help="Device map for loading the model.")
    parser.add_argument("--help", action="store_true", help="Show this help message and exit.")

    args = parser.parse_args()

    if args.help:
        parser.print_help()
        exit(0)

    # Use command-line arguments if provided, otherwise use hardcoded values
    model_id = args.model_id if args.model_id else MODEL_ID
    bits = args.bits if args.bits else BITS
    dataset = args.dataset if args.dataset else DATASET
    group_size = args.group_size if args.group_size else GROUP_SIZE
    device_map = args.device_map if args.device_map else DEVICE_MAP

    if not all([model_id, bits, dataset, group_size, device_map]):
        print("Error: Not all settings are provided. Use --help for more information.")
        exit(1)

    main(model_id=model_id, bits=bits, dataset=dataset, group_size=group_size, device_map=device_map)