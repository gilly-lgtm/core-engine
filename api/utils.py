import logging
import os
from typing import Any, Dict, List

def setup_logger(logger_name: str, log_file: str) -> logging.Logger:
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger

def load_config(config_file: str) -> Dict[str, Any]:
    import json
    with open(config_file, 'r') as f:
        return json.load(f)

def write_config(config: Dict[str, Any], config_file: str) -> None:
    import json
    with open(config_file, 'w') as f:
        json.dump(config, f, indent=4)

def get_environment_variables() -> Dict[str, str]:
    return dict(os.environ)

def validate_input(input_data: Any) -> bool:
    if input_data is None:
        return False
    if isinstance(input_data, (str, int, float, list, dict)):
        return True
    return False

def flatten_list(nested_list: List[Any]) -> List[Any]:
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list

def merge_dicts(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

# example usage
if __name__ == '__main__':
    logger = setup_logger('core-engine', 'core-engine.log')
    config = load_config('config.json')
    logger.debug(config)
    write_config(config, 'config.json')