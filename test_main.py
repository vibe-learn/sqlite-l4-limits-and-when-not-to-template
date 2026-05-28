"""Tests for the `l4_limits_and_when_not_to` homework scaffold.

SQLite встроена — тесты бегут на :memory:-базе, ничего поднимать не нужно.
"""

import main


def test_database_path_default(monkeypatch):
    """database_path() возвращает ":memory:" по умолчанию."""
    monkeypatch.delenv("DATABASE_PATH", raising=False)
    assert main.database_path() == ":memory:"


def test_database_path_env_override(monkeypatch):
    """env DATABASE_PATH перекрывает дефолт."""
    monkeypatch.setenv("DATABASE_PATH", "/tmp/app.db")
    assert main.database_path() == "/tmp/app.db"


def test_connect_in_memory():
    """connect(":memory:") открывает рабочее соединение sqlite3."""
    with main.connect(":memory:") as conn:
        cur = conn.execute("SELECT 1")
        assert cur.fetchone()[0] == 1
    # TODO: вызови свои реализованные функции на :memory:-conn и проверь
    # поведение урока «Лимиты и когда НЕ стоит».
