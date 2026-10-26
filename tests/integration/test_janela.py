import pytest


@pytest.mark.desktop
def test_janela_principal_disponivel(desktop):
    assert desktop.window.is_visible()
    assert desktop.window.is_enabled()
