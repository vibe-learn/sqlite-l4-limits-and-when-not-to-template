"""Homework scaffold — sqlite lesson `l4_limits_and_when_not_to` (Vibe Learn).

Задача: советник по выбору СУБД recommend(profile) (чистая функция) + эмпирическая демонстрация single-writer лимита.

Реализуй функции ниже — сигнатуры и тестовая поверхность фиксированы;
CI (.github/workflows/ci.yml) ставит зависимости и гоняет `pytest`.
Подробности и критерии приёмки — в README.md.

SQLite встроена в Python через stdlib `sqlite3` — никакого драйвера ставить
не нужно, сервера нет. БД это файл (DATABASE_PATH) или ":memory:" в тестах.
"""

import os
import sqlite3


def database_path() -> str:
    """Путь к файлу БД из env. Дефолт ":memory:" — БД живёт в процессе."""
    return os.environ.get("DATABASE_PATH", ":memory:")


def connect(path: str | None = None) -> sqlite3.Connection:
    """Открыть соединение sqlite3 (по умолчанию из database_path())."""
    return sqlite3.connect(path if path is not None else database_path())


# ----- TODO #1: recommend -----
def recommend(profile: dict) -> tuple[str, str]:
    """чистая функция: по признакам нагрузки (concurrent_writers, multi_machine, need_roles, heavy_analytic_joins, read_heavy_single_server) вернуть ('postgresql'|'sqlite', обоснование)"""
    raise NotImplementedError("recommend: реализуй меня")


# ----- TODO #2: demo_write_contention -----
def demo_write_contention(path: str, writers: int, iters: int) -> int:
    """запустить writers потоков-писателей без busy_timeout, вернуть число ошибок 'database is locked'"""
    raise NotImplementedError("demo_write_contention: реализуй меня")



def main() -> None:
    """Точка входа: подключиться и напомнить, что реализовать.

    Замени тело на демонстрацию реализованных функций.
    """
    print("Vibe Learn — sqlite lesson scaffold up")
    print(f"DATABASE_PATH: {database_path()} (stdlib sqlite3, no server)")
    print("Реализуй TODO-функции, затем `pytest`. README.md содержит задачу.")


if __name__ == "__main__":
    main()
