#!/usr/bin/env python
"""ジャンケンクラス."""
from rock_paper_scissors import hand_constant
from rock_paper_scissors import scene
from rock_paper_scissors import players
from rock_paper_scissors import standard_judge
from rock_paper_scissors import result_constant


class RockPaperScissors():
    """ジャンケンクラス."""

    def __init__(self):
        """コンストラクタ."""
        self.__players = players.Players()
        self.__scene = scene.Scene()

    def initialize_game(self, players: players.Players):
        """ゲームの初期化."""
        self.__players.clone(players)
        self.__scene.initialize_game()

    def task(self):
        """実行."""
        s = self.__scene.get()
        if s == scene.Scene.INITIALIZE:
            self.task_initialize()
            return
        if s == scene.Scene.START_SHOUT:
            self.task_start_shout()
            return
        if s == scene.Scene.INITIALIZE_SHOWDOWN:
            self.task_initialize_showdown()
            return
        if s == scene.Scene.SHOWDOWN:
            self.task_showdown()
            return
        if s == scene.Scene.JUDGE:
            self.task_judge()
            return
        if s == scene.Scene.DRAW_SHOUT:
            self.task_draw_shout()
            return
        if s == scene.Scene.END:
            self.task_end()
            return

    def is_finished(self):
        """ジャンケンが終了したか."""
        return self.__scene.get() == scene.Scene.END

    def task_initialize(self):
        """初期化."""
        self.__scene.next()

    def task_start_shout(self):
        """最初の掛け声."""
        print("最初はグー。ジャンケンポン")
        self.__scene.next()

    def task_initialize_showdown(self):
        """手の公開の初期化."""
        for i in range(self.__players.length()):
            self.__players.get(i).start_showdown()
        self.__scene.next()

    def task_showdown(self):
        """手の公開."""
        for i in range(self.__players.length()):
            h = self.__players.get_hand(i)
            name = "[" + str(i) + "] " + hand_constant.HandConstant.get_name(h)
            print(name)
        self.__scene.next()

    def task_judge(self):
        """判定."""
        j = standard_judge.StandardJudge()
        j.set(self.__players)
        result = j.judge()
        if result[0] == result_constant.ResultConstant.DRAW:
            self.__scene.next()
        if result[0] == result_constant.ResultConstant.WIN:
            s = ""
            for i in range(len(result) - 1):
                s = s + str(result[1][i]) + " "
            print("")
            print("勝ちプレイヤー")
            print(s)
            print("")
            self.__scene.set(scene.Scene.END)

    def task_draw_shout(self):
        """あいこの掛け声."""
        print("")
        print("あいこでしょ")
        print("")
        self.__scene.set(scene.Scene.INITIALIZE_SHOWDOWN)
        pass

    def task_end(self):
        """終了."""
        pass
