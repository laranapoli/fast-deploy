import os
import pickle

from sklearn.base import BaseEstimator

from fast_deploy.model_loader import ModelLoader


class SklearnModelLoader(ModelLoader):
    def load_model(self, model_path: str) -> BaseEstimator:
        """Carrega um modelo treinado com Scikit-learn"""
        if not os.path.exists(model_path):
            raise FileNotFoundError(
                f'O arquivo {model_path} não foi encontrado.'
            )
        try:
            with open(model_path, 'rb') as model_file:
                model = pickle.load(model_file)
                if not isinstance(model, BaseEstimator):
                    raise TypeError(
                        f'O arquivo {model_path} não contém um modelo sklearn válido!'
                    )
            return model
        except Exception as e:
            raise RuntimeError(f'Erro ao carregar o modelo: {str(e)}')
