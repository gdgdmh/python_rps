#!/usr/bin/env python
"""シーンクラス."""


class Scene():
    """シーンクラス."""

    INITIALIZE = 0  # 初期化
    START_SHOUT = 1  # 最初の掛け声
    INITIALIZE_SHOWDOWN = 2  # 手の公開の初期化
    SHOWDOWN = 3  # 手の公開
    JUDGE = 4  # 判定
    DRAW_SHOUT = 5  # あいこの掛け声
    END = 6  # ゲーム終了

    def __init__(self):
        """コンストラクタ."""
        self.__scene = Scene.INITIALIZE

    def get(self):
        """現在のシーン取得."""
        return self.__scene

    def initialize_game(self):
        """ゲームの初期化."""
        self.__scene = Scene.INITIALIZE

    def next(self) -> int:
        """次のシーンに進む."""
        if self.__scene < Scene.END:
            self.__scene = self.__scene + 1

    def set(self, value: int):
        """シーンを設定."""
        self.__scene = value
