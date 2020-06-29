#!/usr/bin/env python
"""CPUプレイヤークラス."""
from rock_paper_scissors import player
from rock_paper_scissors import hand_constant
from rock_paper_scissors import system_random_int


class CpuPlayer(player.Player):
    """CPUプレイヤークラス."""

    def start_showdown(self):
        """手の公開の前に呼ばれる."""
        pass

    def showdown(self) -> int:
        """手の公開."""
        r = system_random_int.SystemRandomInt()
        hands = [
            hand_constant.HandConstant.ROCK,
            hand_constant.HandConstant.PAPER,
            hand_constant.HandConstant.SCISSORS
        ]
        index = r.get_range(0, len(hands) - 1)
        return hands[index]
