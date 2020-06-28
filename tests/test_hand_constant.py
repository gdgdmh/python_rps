#!/usr/bin/env python
"""ジャンケン手定数クラス."""
from rock_paper_scissors import hand_constant


def test_get_name_case_rock():
    """名前取得のrockのケース."""
    type = hand_constant.HandConstant.ROCK
    assert hand_constant.HandConstant.get_name(type) == "rock"


def test_get_name_case_paper():
    """名前取得のrockのケース."""
    type = hand_constant.HandConstant.PAPER
    assert hand_constant.HandConstant.get_name(type) == "paper"


def test_get_name_case_scissors():
    """名前取得のrockのケース."""
    type = hand_constant.HandConstant.SCISSORS
    assert hand_constant.HandConstant.get_name(type) == "scissors"


def test_check_hand_case_rock():
    """手のチェック(rock)."""
    h = hand_constant.HandConstant.ROCK
    assert hand_constant.HandConstant.check_hand(h)


def test_check_hand_case_paper():
    """手のチェック(paper)."""
    h = hand_constant.HandConstant.PAPER
    assert hand_constant.HandConstant.check_hand(h)


def test_check_hand_case_scissors():
    """手のチェック(scissors)."""
    h = hand_constant.HandConstant.SCISSORS
    assert hand_constant.HandConstant.check_hand(h)


def test_check_hand_case_str():
    """手のチェック(str値)."""
    h = "foo bar"
    assert not hand_constant.HandConstant.check_hand(h)
