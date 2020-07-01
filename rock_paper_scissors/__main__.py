#!/usr/bin/env python
"""エントリーポイント."""

from rock_paper_scissors import standard_judge
from rock_paper_scissors import debug_player
from rock_paper_scissors import players
from rock_paper_scissors import hand_constant


def main():
    """エントリーポイント."""
    print('main')
    s = standard_judge.StandardJudge()
    p = players.Players()
    player_count = 3
    for i in range(player_count):
        pl = debug_player.DebugPlayer()
        if i == 0:
            pl.set(hand_constant.HandConstant.ROCK)
        if i == 1:
            pl.set(hand_constant.HandConstant.SCISSORS)
        if i == 2:
            pl.set(hand_constant.HandConstant.ROCK)
        p.add(pl)
    s.set(p)
    result = s.judge()
    print(result)


if __name__ == '__main__':
    main()
