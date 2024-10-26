import pickle
from unittest.mock import mock_open, patch

import pytest
from sklearn.base import BaseEstimator
from sklearn.linear_model import LogisticRegression

from fast_deploy.loaders.sklearn_loader import SklearnModelLoader


@patch('builtins.open', new_callable=mock_open)
@patch('os.path.exists', return_value=True)
def test_success(mock_exists, mock_open_file):
    expected_model = LogisticRegression()
    model_bytes = pickle.dumps(expected_model)
    mock_open_file.return_value.read.return_value = model_bytes

    loader = SklearnModelLoader()
    model = loader.load_model('fake_model_path.pkl')

    assert isinstance(model, BaseEstimator)


@patch('os.path.exists', return_value=False)
def test_file_not_found(mock_exists):
    loader = SklearnModelLoader()

    with pytest.raises(FileNotFoundError):
        loader.load_model('non-existent-model-path.pkl')
