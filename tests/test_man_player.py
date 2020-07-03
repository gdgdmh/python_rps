#!/usr/bin/env python
"""人間プレイヤーテストクラス."""
from rock_paper_scissors import man_player
from rock_paper_scissors import hand_constant
from rock_paper_scissors import input_keyboard


def test_start_showdown_rock(capsys, monkeypatch):
    """手の公開(rock)."""
    mp = man_player.ManPlayer()
    # input関数を置き換えて対応
    method_name = 'input_string'
    p = 'rock'
    monkeypatch.setattr(input_keyboard.InputKeyboard, method_name, lambda x: p)
    mp.start_showdown()
    h = mp.get()
    assert h == hand_constant.HandConstant.ROCK


def test_start_showdown_paper(capsys, monkeypatch):
    """手の公開(paper)."""
    mp = man_player.ManPlayer()
    # input関数を置き換えて対応
    method_name = 'input_string'
    p = 'paper'
    monkeypatch.setattr(input_keyboard.InputKeyboard, method_name, lambda x: p)
    mp.start_showdown()
    h = mp.get()
    assert h == hand_constant.HandConstant.PAPER


def test_start_showdown_scissors(capsys, monkeypatch):
    """手の公開(scissors)."""
    mp = man_player.ManPlayer()
    # input関数を置き換えて対応
    method_name = 'input_string'
    p = 'scissors'
    monkeypatch.setattr(input_keyboard.InputKeyboard, method_name, lambda x: p)
    mp.start_showdown()
    h = mp.get()
    assert h == hand_constant.HandConstant.SCISSORS


def test_get_rock(capsys, monkeypatch):
    """手の取得(rock)."""
    mp = man_player.ManPlayer()
    # input関数を置き換えて対応
    method_name = 'input_string'
    p = 'rock'
    monkeypatch.setattr(input_keyboard.InputKeyboard, method_name, lambda x: p)
    mp.start_showdown()
    h = mp.get()
    assert h == hand_constant.HandConstant.ROCK


def test_get_paper(capsys, monkeypatch):
    """手の取得(paper)."""
    mp = man_player.ManPlayer()
    # input関数を置き換えて対応
    method_name = 'input_string'
    p = 'paper'
    monkeypatch.setattr(input_keyboard.InputKeyboard, method_name, lambda x: p)
    mp.start_showdown()
    h = mp.get()
    assert h == hand_constant.HandConstant.PAPER


def test_get_scissors(capsys, monkeypatch):
    """手の取得(scissors)."""
    mp = man_player.ManPlayer()
    # input関数を置き換えて対応
    method_name = 'input_string'
    p = 'scissors'
    monkeypatch.setattr(input_keyboard.InputKeyboard, method_name, lambda x: p)
    mp.start_showdown()
    h = mp.get()
    assert h == hand_constant.HandConstant.SCISSORS
