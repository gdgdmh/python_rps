#!/usr/bin/env python
"""ジャンケンの手チョキテスト."""
from rock_paper_scissors import hand_scissors
from rock_paper_scissors import hand_constant


def test_was_get_type_scissors():
    """タイプの取得(rock)."""
    scissors = hand_scissors.HandScissors()
    assert scissors.get_type() == hand_constant.HandConstant.SCISSORS


def test_was_get_type_not_rock():
    """タイプの取得(rockと不一致)."""
    scissors = hand_scissors.HandScissors()
    assert scissors.get_type() != hand_constant.HandConstant.ROCK


def test_was_get_type_not_paper():
    """タイプの取得(paperと不一致)."""
    scissors = hand_scissors.HandScissors()
    assert scissors.get_type() != hand_constant.HandConstant.PAPER


def test_was_get_name_scissors():
    """名前取得(scissors)."""
    scissors = hand_scissors.HandScissors()
    type = hand_constant.HandConstant.SCISSORS
    assert scissors.get_name() == hand_constant.HandConstant.get_name(type)
