#!/usr/bin/env python
"""シーンクラステスト."""
from rock_paper_scissors import scene


def test_get_default():
    """生成後のシーン取得."""
    s = scene.Scene()
    assert s.get() == scene.Scene.INITIALIZE


def test_initialize_game_check():
    """ゲームの初期化後にINITIALIZE."""
    s = scene.Scene()
    s.initialize_game()
    assert s.get() == scene.Scene.INITIALIZE


def test_next_case_initialize():
    """次のシーン(INITIALIZE)."""
    s = scene.Scene()
    s.set(scene.Scene.INITIALIZE)
    s.next()
    assert s.get() == scene.Scene.START_SHOUT


def test_next_case_start_shout():
    """次のシーン(START_SHOUT)."""
    s = scene.Scene()
    s.set(scene.Scene.START_SHOUT)
    s.next()
    assert s.get() == scene.Scene.INITIALIZE_SHOWDOWN


def test_next_case_initialize_showdown():
    """次のシーン(INITIALIZE_SHOWDOWN)."""
    s = scene.Scene()
    s.set(scene.Scene.INITIALIZE_SHOWDOWN)
    s.next()
    assert s.get() == scene.Scene.SHOWDOWN


def test_next_case_showdown():
    """次のシーン(SHOWDOWN)."""
    s = scene.Scene()
    s.set(scene.Scene.SHOWDOWN)
    s.next()
    assert s.get() == scene.Scene.JUDGE


def test_next_case_judge():
    """次のシーン(JUDGE)."""
    s = scene.Scene()
    s.set(scene.Scene.JUDGE)
    s.next()
    assert s.get() == scene.Scene.DRAW_SHOUT


def test_next_case_draw_shout():
    """次のシーン(DRAW_SHOUT)."""
    s = scene.Scene()
    s.set(scene.Scene.DRAW_SHOUT)
    s.next()
    assert s.get() == scene.Scene.END


def test_next_case_end():
    """次のシーン(END)."""
    s = scene.Scene()
    s.set(scene.Scene.END)
    s.next()
    assert s.get() == scene.Scene.END


def test_set_case_initialize():
    """シーン設定(INITIALIZE)."""
    s = scene.Scene()
    s.set(scene.Scene.INITIALIZE)
    assert s.get() == scene.Scene.INITIALIZE


def test_set_case_start_shout():
    """シーン設定(START_SHOUT)."""
    s = scene.Scene()
    s.set(scene.Scene.START_SHOUT)
    assert s.get() == scene.Scene.START_SHOUT


def test_set_case_initialize_showdown():
    """シーン設定(INITIALIZE_SHOWDOWN)."""
    s = scene.Scene()
    s.set(scene.Scene.INITIALIZE_SHOWDOWN)
    assert s.get() == scene.Scene.INITIALIZE_SHOWDOWN


def test_set_case_showdown():
    """シーン設定(SHOWDOWN)."""
    s = scene.Scene()
    s.set(scene.Scene.SHOWDOWN)
    assert s.get() == scene.Scene.SHOWDOWN


def test_set_case_judge():
    """シーン設定(JUDGE)."""
    s = scene.Scene()
    s.set(scene.Scene.JUDGE)
    assert s.get() == scene.Scene.JUDGE


def test_set_case_draw_shout():
    """シーン設定(DRAW_SHOUT)."""
    s = scene.Scene()
    s.set(scene.Scene.DRAW_SHOUT)
    assert s.get() == scene.Scene.DRAW_SHOUT


def test_set_case_end():
    """シーン設定(END)."""
    s = scene.Scene()
    s.set(scene.Scene.END)
    assert s.get() == scene.Scene.END
