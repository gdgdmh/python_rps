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
    player_count = 1
    for _ in range(player_count):
        pl = debug_player.DebugPlayer()
        pl.set(hand_constant.HandConstant.ROCK)
        p.add(pl)
    s.set(p)



if __name__ == '__main__':
    main()
