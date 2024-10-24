import pickle
from unittest import mock

import pytest

from fast_deploy.model_loader import load_model


def test_load_model():
    fake_model = {'name': 'Example Model'}

    with mock.patch(
        'os.path.exists', return_value=True
    ):  # Mocka os.path.exists para retornar True
        with mock.patch(
            'builtins.open', mock.mock_open(read_data=pickle.dumps(fake_model))
        ) as mock_file:
            result = load_model('model.pkl')
            assert result == fake_model
            mock_file.assert_called_once_with('model.pkl', 'rb')


def test_load_model_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_model('non_existent_model.pkl')
