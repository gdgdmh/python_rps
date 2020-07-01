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
    assert len(result) == 2


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
    assert len(result) == 2


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
    assert len(result) == 2


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
    assert len(result) == 2


def test_judge_rock_paper():
    """ジャンケンの判定(rock, paper)."""
    s = standard_judge.StandardJudge()
    p = players.Players()
    player_count = 2
    for i in range(player_count):
        pl = debug_player.DebugPlayer()
        if i == 0:
            pl.set(hand_constant.HandConstant.ROCK)
        if i == 1:
            pl.set(hand_constant.HandConstant.PAPER)
        p.add(pl)
    s.set(p)
    result = s.judge()
    assert result[0] == result_constant.ResultConstant.WIN
    assert result[1][0] == 1
    assert len(result) == 2


def test_judge_rock_scissors():
    """ジャンケンの判定(rock, scissors)."""
    s = standard_judge.StandardJudge()
    p = players.Players()
    player_count = 2
    for i in range(player_count):
        pl = debug_player.DebugPlayer()
        if i == 0:
            pl.set(hand_constant.HandConstant.ROCK)
        if i == 1:
            pl.set(hand_constant.HandConstant.SCISSORS)
        p.add(pl)
    s.set(p)
    result = s.judge()
    assert result[0] == result_constant.ResultConstant.WIN
    assert result[1][0] == 0
    assert len(result) == 2


def test_judge_paper_scissors():
    """ジャンケンの判定(paper, scissors)."""
    s = standard_judge.StandardJudge()
    p = players.Players()
    player_count = 2
    for i in range(player_count):
        pl = debug_player.DebugPlayer()
        if i == 0:
            pl.set(hand_constant.HandConstant.PAPER)
        if i == 1:
            pl.set(hand_constant.HandConstant.SCISSORS)
        p.add(pl)
    s.set(p)
    result = s.judge()
    assert result[0] == result_constant.ResultConstant.WIN
    assert result[1][0] == 1
    assert len(result) == 2


def test_judge_rock_multi_paper():
    """ジャンケンの判定(rock複数, paper)."""
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
            pl.set(hand_constant.HandConstant.ROCK)
        p.add(pl)
    s.set(p)
    result = s.judge()
    assert result[0] == result_constant.ResultConstant.WIN
    assert result[1][0] == 1
    assert len(result) == 2


def test_judge_rock_paper_multi():
    """ジャンケンの判定(rock, paper複数)."""
    s = standard_judge.StandardJudge()
    p = players.Players()
    player_count = 3
    for i in range(player_count):
        pl = debug_player.DebugPlayer()
        if i == 0:
            pl.set(hand_constant.HandConstant.PAPER)
        if i == 1:
            pl.set(hand_constant.HandConstant.PAPER)
        if i == 2:
            pl.set(hand_constant.HandConstant.ROCK)
        p.add(pl)
    s.set(p)
    result = s.judge()
    assert result[0] == result_constant.ResultConstant.WIN
    assert result[1][0] == 0
    assert result[1][1] == 1
    assert len(result) == 2
    assert len(result[1]) == 2


def test_judge_rock_multi_paper_multi():
    """ジャンケンの判定(rock複数, paper複数)."""
    s = standard_judge.StandardJudge()
    p = players.Players()
    player_count = 5
    for i in range(player_count):
        pl = debug_player.DebugPlayer()
        if i == 0:
            pl.set(hand_constant.HandConstant.PAPER)
        if i == 1:
            pl.set(hand_constant.HandConstant.ROCK)
        if i == 2:
            pl.set(hand_constant.HandConstant.ROCK)
        if i == 3:
            pl.set(hand_constant.HandConstant.PAPER)
        if i == 4:
            pl.set(hand_constant.HandConstant.ROCK)
        p.add(pl)
    s.set(p)
    result = s.judge()
    assert result[0] == result_constant.ResultConstant.WIN
    assert result[1][0] == 0
    assert result[1][1] == 3
    assert len(result) == 2
    assert len(result[1]) == 2


def test_judge_rock_multi_scissors():
    """ジャンケンの判定(rock複数, scissors)."""
    s = standard_judge.StandardJudge()
    p = players.Players()
    player_count = 3
    for i in range(player_count):
        pl = debug_player.DebugPlayer()
        if i == 0:
            pl.set(hand_constant.HandConstant.SCISSORS)
        if i == 1:
            pl.set(hand_constant.HandConstant.ROCK)
        if i == 2:
            pl.set(hand_constant.HandConstant.ROCK)
        p.add(pl)
    s.set(p)
    result = s.judge()
    assert result[0] == result_constant.ResultConstant.WIN
    assert result[1][0] == 1
    assert result[1][1] == 2
    assert len(result) == 2
    assert len(result[1]) == 2


def test_judge_rock_scissors_multi():
    """ジャンケンの判定(rock, scissors複数)."""
    s = standard_judge.StandardJudge()
    p = players.Players()
    player_count = 4
    for i in range(player_count):
        pl = debug_player.DebugPlayer()
        if i == 0:
            pl.set(hand_constant.HandConstant.SCISSORS)
        if i == 1:
            pl.set(hand_constant.HandConstant.SCISSORS)
        if i == 2:
            pl.set(hand_constant.HandConstant.SCISSORS)
        if i == 3:
            pl.set(hand_constant.HandConstant.ROCK)
        p.add(pl)
    s.set(p)
    result = s.judge()
    assert result[0] == result_constant.ResultConstant.WIN
    assert result[1][0] == 3
    assert len(result) == 2


def test_judge_rock_multi_scissors_multi():
    """ジャンケンの判定(rock複数, scissors複数)."""
    s = standard_judge.StandardJudge()
    p = players.Players()
    player_count = 6
    for i in range(player_count):
        pl = debug_player.DebugPlayer()
        if i == 0:
            pl.set(hand_constant.HandConstant.SCISSORS)
        if i == 1:
            pl.set(hand_constant.HandConstant.ROCK)
        if i == 2:
            pl.set(hand_constant.HandConstant.ROCK)
        if i == 3:
            pl.set(hand_constant.HandConstant.SCISSORS)
        if i == 4:
            pl.set(hand_constant.HandConstant.SCISSORS)
        if i == 5:
            pl.set(hand_constant.HandConstant.ROCK)
        p.add(pl)
    s.set(p)
    result = s.judge()
    assert result[0] == result_constant.ResultConstant.WIN
    assert result[1][0] == 1
    assert result[1][1] == 2
    assert result[1][2] == 5
    assert len(result) == 2
    assert len(result[1]) == 3


def test_judge_paper_multi_scissors():
    """ジャンケンの判定(papaer複数, scissors)."""
    s = standard_judge.StandardJudge()
    p = players.Players()
    player_count = 5
    for i in range(player_count):
        pl = debug_player.DebugPlayer()
        if i == 0:
            pl.set(hand_constant.HandConstant.PAPER)
        if i == 1:
            pl.set(hand_constant.HandConstant.PAPER)
        if i == 2:
            pl.set(hand_constant.HandConstant.SCISSORS)
        if i == 3:
            pl.set(hand_constant.HandConstant.PAPER)
        if i == 4:
            pl.set(hand_constant.HandConstant.PAPER)
        p.add(pl)
    s.set(p)
    result = s.judge()
    assert result[0] == result_constant.ResultConstant.WIN
    assert result[1][0] == 2
    assert len(result) == 2
    assert len(result[1]) == 1


def test_judge_paper_scissors_multi():
    """ジャンケンの判定(papaer, scissors複数)."""
    s = standard_judge.StandardJudge()
    p = players.Players()
    player_count = 5
    for i in range(player_count):
        pl = debug_player.DebugPlayer()
        if i == 0:
            pl.set(hand_constant.HandConstant.SCISSORS)
        if i == 1:
            pl.set(hand_constant.HandConstant.PAPER)
        if i == 2:
            pl.set(hand_constant.HandConstant.SCISSORS)
        if i == 3:
            pl.set(hand_constant.HandConstant.SCISSORS)
        if i == 4:
            pl.set(hand_constant.HandConstant.SCISSORS)
        p.add(pl)
    s.set(p)
    result = s.judge()
    assert result[0] == result_constant.ResultConstant.WIN
    assert result[1][0] == 0
    assert result[1][1] == 2
    assert result[1][2] == 3
    assert result[1][3] == 4
    assert len(result) == 2
    assert len(result[1]) == 4


def test_judge_paper_multi_scissors_multi():
    """ジャンケンの判定(papaer複数, scissors複数)."""
    s = standard_judge.StandardJudge()
    p = players.Players()
    player_count = 7
    for i in range(player_count):
        pl = debug_player.DebugPlayer()
        if i == 0:
            pl.set(hand_constant.HandConstant.SCISSORS)
        if i == 1:
            pl.set(hand_constant.HandConstant.PAPER)
        if i == 2:
            pl.set(hand_constant.HandConstant.PAPER)
        if i == 3:
            pl.set(hand_constant.HandConstant.SCISSORS)
        if i == 4:
            pl.set(hand_constant.HandConstant.PAPER)
        if i == 5:
            pl.set(hand_constant.HandConstant.SCISSORS)
        if i == 6:
            pl.set(hand_constant.HandConstant.PAPER)
        p.add(pl)
    s.set(p)
    result = s.judge()
    assert result[0] == result_constant.ResultConstant.WIN
    assert result[1][0] == 0
    assert result[1][1] == 3
    assert result[1][2] == 5
    assert len(result) == 2
    assert len(result[1]) == 3
