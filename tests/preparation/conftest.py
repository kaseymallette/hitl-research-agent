import importlib.util
import sys
from pathlib import Path
from types import ModuleType

import pytest

SCRIPT = Path(__file__).resolve().parents[2] / "scripts" / "prepare_sources.py"


@pytest.fixture(scope="session")
def prep() -> ModuleType:
    spec = importlib.util.spec_from_file_location("prepare_sources", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules["prepare_sources"] = module
    spec.loader.exec_module(module)
    return module
