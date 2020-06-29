#!/usr/bin/env python
"""プレイヤーまとめクラス."""
from rock_paper_scissors import players
from rock_paper_scissors import cpu_player


def test_add_case_one():
    """プレイヤーの追加(1人)."""
    ps = players.Players()
    p = cpu_player.CpuPlayer()
    ps.add(p)
    assert ps.length() == 1


def test_add_case_two():
    """プレイヤーの追加(2人)."""
    ps = players.Players()
    add_count = 2
    for _ in range(add_count):
        p = cpu_player.CpuPlayer()
        ps.add(p)
    assert ps.length() == add_count


def test_clear_case_one():
    """プレイヤーデータのクリア."""
    ps = players.Players()
    p = cpu_player.CpuPlayer()
    ps.add(p)
    assert ps.length() == 1
    ps.clear()
    assert ps.length() == 0


def test_clear_case_two():
    """プレイヤーデータのクリア(2人)."""
    ps = players.Players()
    add_count = 2
    for _ in range(add_count):
        p = cpu_player.CpuPlayer()
        ps.add(p)
    assert ps.length() == add_count
    ps.clear()
    assert ps.length() == 0


def test_length_case_zero():
    """プレイヤーデータの取得(0)."""
    ps = players.Players()
    assert ps.length() == 0


def test_length_case_one():
    """プレイヤーデータの取得(1)."""
    ps = players.Players()
    p = cpu_player.CpuPlayer()
    ps.add(p)
    assert ps.length() == 1


def test_length_case_one_hundred():
    """プレイヤーデータの取得(100)."""
    ps = players.Players()
    add_count = 100
    for _ in range(add_count):
        p = cpu_player.CpuPlayer()
        ps.add(p)
    assert ps.length() == add_count
