#!/usr/bin/env python
"""ジャンケンの手パーテスト."""
from rock_paper_scissors import hand_paper
from rock_paper_scissors import hand_constant


def test_was_get_type_paper():
    """タイプの取得(paper)."""
    paper = hand_paper.HandPaper()
    assert paper.get_type() == hand_constant.HandConstant.PAPER


def test_was_get_type_not_rock():
    """タイプの取得(rockと不一致)."""
    paper = hand_paper.HandPaper()
    assert paper.get_type() != hand_constant.HandConstant.ROCK


def test_was_get_type_not_scissors():
    """タイプの取得(scissorsと不一致)."""
    paper = hand_paper.HandPaper()
    assert paper.get_type() != hand_constant.HandConstant.SCISSORS


def test_was_get_name_paper():
    """名前取得(paper)."""
    paper = hand_paper.HandPaper()
    type = hand_constant.HandConstant.PAPER
    assert paper.get_name() == hand_constant.HandConstant.get_name(type)
