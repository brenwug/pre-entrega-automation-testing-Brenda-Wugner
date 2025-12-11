import pytest

test_files = [
    "tests/test_login.py",
    "tests/test_catalogo.py",
    "tests/test_carrito.py",
    "tests/test_api_jsonplaceholder.py",
    "tests/test_checkout.py"
]

pytest_args = test_files + ["--html=reports/report.html","--self-contained-html","-v"]

pytest.main(pytest_args)