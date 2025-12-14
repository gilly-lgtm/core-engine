import logging
import os
from typing import Any, Dict, List, Tuple

def setup_logger(logger_name: str, log_file: str) -> logging.Logger:
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger

def load_config(file_path: str) -> Dict[str, Any]:
    import json
    with open(file_path, 'r') as file:
        return json.load(file)

def get_environment_variable(var_name: str) -> str:
    return os.environ.get(var_name)

def split_list(input_list: List[Any], chunk_size: int) -> List[List[Any]]:
    return [input_list[i:i + chunk_size] for i in range(0, len(input_list), chunk_size)]

def merge_dicts(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    return {**dict1, **dict2}

def get_file_extension(file_path: str) -> str:
    return os.path.splitext(file_path)[1]

def get_file_name(file_path: str) -> str:
    return os.path.basename(file_path)

def create_directory(dir_path: str) -> None:
    os.makedirs(dir_path, exist_ok=True)

def is_file_exists(file_path: str) -> bool:
    return os.path.isfile(file_path)

def is_directory_exists(dir_path: str) -> bool:
    return os.path.isdir(dir_path)

def get_file_size(file_path: str) -> int:
    return os.path.getsize(file_path)

def get_directory_size(dir_path: str) -> int:
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def tuple_to_list(input_tuple: Tuple[Any]) -> List[Any]:
    return list(input_tuple)

def list_to_tuple(input_list: List[Any]) -> Tuple[Any]:
    return tuple(input_list)