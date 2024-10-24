import os
import pickle
from typing import Any


def load_model(model_path: str) -> Any:
    """
    Carrega um modelo a partir do arquivo de objeto serializado.

    Parameters:
        model_path: Caminho para o arquivo de objeto serializado
    """
    if not os.path.exists(model_path):
        raise FileNotFoundError(f'O arquivo {model_path} não foi encontrado.')
    try:
        with open(model_path, 'rb') as model_file:
            model = pickle.load(model_file)
        return model
    except Exception as e:
        raise RuntimeError(f'Erro ao carregar o modelo: {str(e)}')
