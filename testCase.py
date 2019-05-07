import unittest
import connect_four_starter


class TestConnectFour(unittest.TestCase):

    def test_Create_board(self):
        board = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        print(connect_four_starter.game_state)
        assert connect_four_starter.game_state == board

    def test_Is_horizontal_win(self):
        connect_four_starter.game_state = \
            [[0, 1, 1, 1, 1, 0, 0], [0, 2, 2, 2, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        assert connect_four_starter.is_horizontal_win() is True

    def test_Is_vertical_win(self):
        connect_four_starter.game_state = \
            [[0, 0, 0, 1, 2, 0, 0], [0, 0, 0, 1, 2, 0, 0], [0, 0, 0, 1, 2, 0, 0],
             [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        assert connect_four_starter.is_vertical_win() is True

    def test_Is_diagonal_win(self):
        connect_four_starter.game_state = \
            [[0, 0, 1, 2, 2, 2, 0], [0, 0, 0, 1, 1, 1, 0], [0, 0, 0, 2, 1, 2, 0],
             [0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        assert connect_four_starter.is_diagonal_win() is True

        connect_four_starter.game_state = \
            [[0, 2, 2, 2, 1, 0, 0], [0, 1, 1, 1, 0, 0, 0], [0, 2, 1, 2, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        assert connect_four_starter.is_diagonal_win() is True

    def test_Board_full(self):
        connect_four_starter.game_state = \
            [[1, 2, 1, 1, 2, 2, 1], [2, 1, 2, 1, 2, 1, 2], [1, 2, 2, 2, 1, 1, 2],
             [1, 1, 1, 2, 1, 2, 2], [1, 2, 2, 1, 2, 1, 1], [2, 1, 2, 1, 2, 3, 1]]
        assert connect_four_starter.board_full() is True
        connect_four_starter.game_state = \
            [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]


if __name__ == '__main__':
    unittest.main()
