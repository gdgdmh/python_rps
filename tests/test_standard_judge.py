#!/usr/bin/env python
"""シーンクラステスト."""
from rock_paper_scissors import standard_judge
from rock_paper_scissors import debug_player
from rock_paper_scissors import players
from rock_paper_scissors import hand_constant
from rock_paper_scissors import result_constant


def test_set_call():
    """判定のためにプレイヤーを設定."""
    s = standard_judge.StandardJudge()
    p = players.Players()
    player_count = 1
    for _ in range(player_count):
        pl = debug_player.DebugPlayer()
        pl.set(hand_constant.HandConstant.ROCK)
        p.add(pl)
    s.set(p)


def test_set_type_error():
    """判定のためにプレイヤーを設定(ValueError)."""
    s = standard_judge.StandardJudge()
    dummy = [1]
    try:
        s.set(dummy)
    except ValueError:
        pass
    else:
        assert False


def test_judge_rock_two():
    """ジャンケン判定(rockあいこ)."""
    s = standard_judge.StandardJudge()
    p = players.Players()
    player_count = 2
    for _ in range(player_count):
        pl = debug_player.DebugPlayer()
        pl.set(hand_constant.HandConstant.ROCK)
        p.add(pl)
    s.set(p)
    result = s.judge()
    assert result[0] == result_constant.ResultConstant.DRAW
    assert result[1] == 0


def test_judge_paper_two():
    """ジャンケン判定(paperあいこ)."""
    s = standard_judge.StandardJudge()
    p = players.Players()
    player_count = 2
    for _ in range(player_count):
        pl = debug_player.DebugPlayer()
        pl.set(hand_constant.HandConstant.PAPER)
        p.add(pl)
    s.set(p)
    result = s.judge()
    assert result[0] == result_constant.ResultConstant.DRAW
    assert result[1] == 0


def test_judge_scissors_two():
    """ジャンケン判定(scissorsあいこ)."""
    s = standard_judge.StandardJudge()
    p = players.Players()
    player_count = 2
    for _ in range(player_count):
        pl = debug_player.DebugPlayer()
        pl.set(hand_constant.HandConstant.SCISSORS)
        p.add(pl)
    s.set(p)
    result = s.judge()
    assert result[0] == result_constant.ResultConstant.DRAW
    assert result[1] == 0


def test_judge_all_type():
    """ジャンケン判定(全ての種類であいこ)."""
    s = standard_judge.StandardJudge()
    p = players.Players()
    player_count = 3
    for i in range(player_count):
        pl = debug_player.DebugPlayer()
        if i == 0:
            pl.set(hand_constant.HandConstant.ROCK)
        if i == 1:
            pl.set(hand_constant.HandConstant.PAPER)
        if i == 2:
            pl.set(hand_constant.HandConstant.SCISSORS)
        p.add(pl)
    s.set(p)
    result = s.judge()
    assert result[0] == result_constant.ResultConstant.DRAW
    assert result[1] == 0
