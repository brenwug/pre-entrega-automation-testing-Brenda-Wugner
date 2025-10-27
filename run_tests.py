import pytest

test_files = [
    "tests/test_login.py",
    "tests/test_catalogo.py",
    "tests/test_carrito.py"
]

pytest_args = test_files + ["--html=report.html","--self-contained-html","-v"]

pytest.main(pytest_args)