#!/usr/bin/env python
"""ジャンケンの手グーテスト."""
from rock_paper_scissors import hand_rock
from rock_paper_scissors import hand_constant


def test_was_get_type_rock():
    """タイプの取得(rock)."""
    rock = hand_rock.HandRock()
    assert rock.get_type() == hand_constant.HandConstant.ROCK


def test_was_get_type_not_paper():
    """タイプの取得(paperと不一致)."""
    rock = hand_rock.HandRock()
    assert rock.get_type() != hand_constant.HandConstant.PAPER


def test_was_get_type_not_scissors():
    """タイプの取得(scissorsと不一致)."""
    rock = hand_rock.HandRock()
    assert rock.get_type() != hand_constant.HandConstant.SCISSORS


def test_was_get_name_rock():
    """名前取得(rock)."""
    rock = hand_rock.HandRock()
    type = hand_constant.HandConstant.ROCK
    assert rock.get_name() == hand_constant.HandConstant.get_name(type)
