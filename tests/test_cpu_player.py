#!/usr/bin/env python
"""CPUプレイヤーテスト."""
from rock_paper_scissors import cpu_player
from rock_paper_scissors import hand_constant


def test_start_showdown_rock():
    """手の公開(ランダムなので複数回実施してrockが出ることを確認)."""
    c = cpu_player.CpuPlayer()
    try_count = 100
    find_rock = False
    for _ in range(try_count):
        c.start_showdown()
        result = c.get()
        if result == hand_constant.HandConstant.ROCK:
            find_rock = True
            break
    assert find_rock


def test_start_showdown_paper():
    """手の公開(ランダムなので複数回実施してpaperが出ることを確認)."""
    c = cpu_player.CpuPlayer()
    try_count = 100
    find_paper = False
    for _ in range(try_count):
        c.start_showdown()
        result = c.get()
        if result == hand_constant.HandConstant.PAPER:
            find_paper = True
            break
    assert find_paper


def test_start_showdown_scissors():
    """手の公開(ランダムなので複数回実施してscissorsが出ることを確認)."""
    c = cpu_player.CpuPlayer()
    try_count = 100
    find_scissors = False
    for _ in range(try_count):
        c.start_showdown()
        result = c.get()
        if result == hand_constant.HandConstant.SCISSORS:
            find_scissors = True
            break
    assert find_scissors


def test_get_range():
    """手の公開の範囲チェック(rock,paper,scissorsのいずれかが出る)."""
    c = cpu_player.CpuPlayer()
    c.start_showdown()
    result = c.get()
    assert (result == hand_constant.HandConstant.ROCK
            or result == hand_constant.HandConstant.PAPER
            or result == hand_constant.HandConstant.SCISSORS)
