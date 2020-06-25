#!/usr/bin/env python
"""ジャンケン手定数クラス."""
from rock_paper_scissors import hand_constant


def test_was_get_name_case_rock():
    """名前取得のrockのケース."""
    type = hand_constant.HandConstant.ROCK
    assert hand_constant.HandConstant.get_name(type) == "rock"


def test_was_get_name_case_paper():
    """名前取得のrockのケース."""
    type = hand_constant.HandConstant.PAPER
    assert hand_constant.HandConstant.get_name(type) == "paper"


def test_was_get_name_case_scissors():
    """名前取得のrockのケース."""
    type = hand_constant.HandConstant.SCISSORS
    assert hand_constant.HandConstant.get_name(type) == "scissors"
