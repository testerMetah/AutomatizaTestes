import re
from datetime import datetime

import pytest

from automatiza.config import ROOT, Settings
from automatiza.database import SqlServer


def pytest_addoption(parser):
    parser.addoption("--real", action="store_true", help="Permite testes reais de banco e desktop")
    parser.addoption("--conectar-apenas", action="store_true",
                     help="Não abre aplicações; exige que o módulo já esteja aberto")


def pytest_collection_modifyitems(config, items):
    if config.getoption("--real"):
        return
    for item in items:
        if item.get_closest_marker("banco") or item.get_closest_marker("desktop"):
            item.add_marker(pytest.mark.skip(reason="Use --real após configurar o .env."))


@pytest.fixture
def settings():
    return Settings.load()


@pytest.fixture
def db(settings):
    return SqlServer(settings)


@pytest.fixture
def desktop(settings, request):
    from automatiza.desktop import DesktopApp
    try:
        app = DesktopApp(settings)
        return app.connect() if request.config.getoption("--conectar-apenas") else app.start()
    except RuntimeError as exc:
        pytest.fail(str(exc), pytrace=False)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    app = item.funcargs.get("desktop")
    if report.failed and app is not None and app.window is not None:
        name = re.sub(r"[^a-zA-Z0-9_-]", "_", item.nodeid)
        path = ROOT / "artifacts" / f"{name}-{datetime.now():%Y%m%d-%H%M%S-%f}.png"
        try:
            app.screenshot(path)
            report.sections.append(("Evidência", str(path)))
        except Exception as exc:
            report.sections.append(("Evidência", f"Falha ao capturar janela: {type(exc).__name__}"))
