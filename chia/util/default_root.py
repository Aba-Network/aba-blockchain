from __future__ import annotations

import os
from pathlib import Path

DEFAULT_ROOT_PATH = Path(os.path.expanduser(os.getenv("CHIA_ROOT", "~/.aba/mainnet"))).resolve()

DEFAULT_KEYS_ROOT_PATH = Path(os.path.expanduser(os.getenv("CHIA_KEYS_ROOT", "~/.aba_keys"))).resolve()

SIMULATOR_ROOT_PATH = Path(os.path.expanduser(os.getenv("CHIA_SIMULATOR_ROOT", "~/.aba/simulator"))).resolve()
