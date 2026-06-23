import numpy as np
import torch


def test_numpy_and_torch_import() -> None:
    values = np.array([1.0, 2.0, 3.0])
    tensor = torch.tensor(values)

    assert tensor.shape == (3,)
    assert float(tensor.sum()) == 6.0
