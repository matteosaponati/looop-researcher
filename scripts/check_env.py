"""Quick smoke test for the local research environment."""

from __future__ import annotations

import importlib.metadata

import numpy as np
import torch


def main() -> None:
    print(f"numpy {np.__version__}")
    print(f"torch {torch.__version__}")
    print(f"torch device: {'mps' if torch.backends.mps.is_available() else 'cpu'}")
    print(f"ollama python client {importlib.metadata.version('ollama')}")


if __name__ == "__main__":
    main()
