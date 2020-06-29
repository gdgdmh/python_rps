#!/usr/bin/env python
"""プレイヤーまとめクラス."""
from rock_paper_scissors import players
from rock_paper_scissors import cpu_player
from rock_paper_scissors import hand_constant


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
    """プレイヤーデータ数の取得(0)."""
    ps = players.Players()
    assert ps.length() == 0


def test_length_case_one():
    """プレイヤーデータ数の取得(1)."""
    ps = players.Players()
    p = cpu_player.CpuPlayer()
    ps.add(p)
    assert ps.length() == 1


def test_length_case_one_hundred():
    """プレイヤーデータ数の取得(100)."""
    ps = players.Players()
    add_count = 100
    for _ in range(add_count):
        p = cpu_player.CpuPlayer()
        ps.add(p)
    assert ps.length() == add_count


def test_get_hand_rock_or_paper_or_scissors():
    """プレイヤーの手の取得."""
    ps = players.Players()
    p = cpu_player.CpuPlayer()
    p.start_showdown()
    ps.add(p)
    h = ps.get_hand(0)
    assert (h == hand_constant.HandConstant.ROCK
            or h == hand_constant.HandConstant.PAPER
            or h == hand_constant.HandConstant.SCISSORS)


def test_get_hand_index_one():
    """プレイヤーの手の取得(indexが1)."""
    ps = players.Players()
    add_count = 2
    for _ in range(add_count):
        p = cpu_player.CpuPlayer()
        p.start_showdown()
        ps.add(p)

    h = ps.get_hand(1)
    assert (h == hand_constant.HandConstant.ROCK
            or h == hand_constant.HandConstant.PAPER
            or h == hand_constant.HandConstant.SCISSORS)
