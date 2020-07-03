#!/usr/bin/env python
"""プレイヤーまとめクラス."""
from rock_paper_scissors import players
from rock_paper_scissors import cpu_player
from rock_paper_scissors import debug_player
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


def test_clone_one_player():
    """クローン(プレイヤー1人)."""
    ps = players.Players()
    add_count = 1
    for _ in range(add_count):
        p = debug_player.DebugPlayer()
        p.set(hand_constant.HandConstant.PAPER)
        ps.add(p)
    clone = players.Players()
    clone.clone(ps)
    assert clone.length() == add_count
    assert clone.get_hand(0) == hand_constant.HandConstant.PAPER


def test_clone_two_player():
    """クローン(プレイヤー2人)."""
    ps = players.Players()
    add_count = 2
    for i in range(add_count):
        p = debug_player.DebugPlayer()
        if i == 0:
            p.set(hand_constant.HandConstant.PAPER)
        if i == 1:
            p.set(hand_constant.HandConstant.ROCK)
        ps.add(p)
    clone = players.Players()
    clone.clone(ps)
    assert clone.length() == add_count
    assert clone.get_hand(0) == hand_constant.HandConstant.PAPER
    assert clone.get_hand(1) == hand_constant.HandConstant.ROCK


def test_clone_overwrite():
    """クローン(上書き)."""
    ps = players.Players()
    add_count = 5
    for i in range(add_count):
        p = debug_player.DebugPlayer()
        if i == 0:
            p.set(hand_constant.HandConstant.SCISSORS)
        if i == 1:
            p.set(hand_constant.HandConstant.PAPER)
        if i == 2:
            p.set(hand_constant.HandConstant.ROCK)
        if i == 3:
            p.set(hand_constant.HandConstant.PAPER)
        if i == 4:
            p.set(hand_constant.HandConstant.SCISSORS)
        ps.add(p)
    clone = players.Players()
    clone.add(debug_player.DebugPlayer())
    clone.clone(ps)
    assert clone.length() == add_count
    assert clone.get_hand(0) == hand_constant.HandConstant.SCISSORS
    assert clone.get_hand(1) == hand_constant.HandConstant.PAPER
    assert clone.get_hand(2) == hand_constant.HandConstant.ROCK
    assert clone.get_hand(3) == hand_constant.HandConstant.PAPER
    assert clone.get_hand(4) == hand_constant.HandConstant.SCISSORS


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


def test_get_index_zero():
    """プレイヤーの取得(indexが0)."""
    ps = players.Players()
    add_count = 1
    for _ in range(add_count):
        p = debug_player.DebugPlayer()
        p.set(hand_constant.HandConstant.SCISSORS)
        p.start_showdown()
        ps.add(p)
    p = ps.get(0)
    assert p.get() == hand_constant.HandConstant.SCISSORS


def test_get_three():
    """プレイヤーの取得(3人分)."""
    ps = players.Players()
    add_count = 3
    for i in range(add_count):
        p = debug_player.DebugPlayer()
        if i == 0:
            p.set(hand_constant.HandConstant.ROCK)
        if i == 1:
            p.set(hand_constant.HandConstant.PAPER)
        if i == 2:
            p.set(hand_constant.HandConstant.SCISSORS)
        p.start_showdown()
        ps.add(p)
    p = ps.get(0)
    assert p.get() == hand_constant.HandConstant.ROCK
    p = ps.get(1)
    assert p.get() == hand_constant.HandConstant.PAPER
    p = ps.get(2)
    assert p.get() == hand_constant.HandConstant.SCISSORS
