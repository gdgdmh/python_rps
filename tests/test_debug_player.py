#!/usr/bin/env python
"""デバッグ用プレイヤーテスト."""
from rock_paper_scissors import debug_player
from rock_paper_scissors import hand_constant


def test_start_showdown():
    """手の公開開始(何もしないのでcallできることだけ確認)."""
    p = debug_player.DebugPlayer()
    p.start_showdown()


def test_get_range():
    """手の公開の範囲チェック(rock,paper,scissorsのいずれかが出る)."""
    p = debug_player.DebugPlayer()
    p.start_showdown()
    result = p.get()
    assert (result == hand_constant.HandConstant.ROCK
            or result == hand_constant.HandConstant.PAPER
            or result == hand_constant.HandConstant.SCISSORS)


def test_set_rock():
    """手の設定(rock)."""
    p = debug_player.DebugPlayer()
    p.set(hand_constant.HandConstant.ROCK)
    assert p.get() == hand_constant.HandConstant.ROCK


def test_set_paper():
    """手の設定(paper)."""
    p = debug_player.DebugPlayer()
    p.set(hand_constant.HandConstant.PAPER)
    assert p.get() == hand_constant.HandConstant.PAPER


def test_set_scissors():
    """手の設定(scissors)."""
    p = debug_player.DebugPlayer()
    p.set(hand_constant.HandConstant.SCISSORS)
    assert p.get() == hand_constant.HandConstant.SCISSORS
