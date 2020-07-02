#!/usr/bin/env python
"""人間プレイヤークラス."""
from rock_paper_scissors import player
from rock_paper_scissors import hand_constant
from rock_paper_scissors import input_keyboard


class ManPlayer(player.Player):
    """人間プレイヤークラス."""

    def __init__(self):
        """コンストラクタ."""
        self.__hand = hand_constant.HandConstant.ROCK
        self.__input = input_keyboard.InputKeyboard()

    def start_showdown(self):
        """手の公開の前に呼ばれる."""
        loop = True
        while (loop):
            print("rock か paper か scissors を入力して下さい >>", end="")
            input_data = self.__input.input_string()
            if input_data == "rock":
                self.__hand = hand_constant.HandConstant.ROCK
                return
            if input_data == "paper":
                self.__hand = hand_constant.HandConstant.PAPER
                return
            if input_data == "scissors":
                self.__hand = hand_constant.HandConstant.SCISSORS
                return

    def get(self) -> int:
        """手の公開."""
        return self.__hand
