import unittest
import counting_game as cg

class TestToDoList(unittest.TestCase):
    game_logic : cg.Game_logic = cg.Game_logic()

    def test_init_rect_exists(self):
        self.assertEqual(self.game_logic.tk_rect.number, 0)

    def test_init_plus_exists(self):
        self.assertEqual(self.game_logic.tk_plus.plus_size, 20)
    
    def test_init_test_collision(self):
        number = self.game_logic.tk_rect.number
        plus_x, plus_y = self.game_logic.tk_plus.plus_x, self.game_logic.tk_plus.plus_y
        steps_right, steps_down = plus_x // 10, plus_y // 10
        for i in range(steps_right):
            self.game_logic.tk_rect.tk_move_right(self.game_logic.tk_frame)

        for j in range(steps_down):
            self.game_logic.tk_rect.tk_move_down(self.game_logic.tk_frame)

        self.assertEqual(self.game_logic.tk_rect.number, number)

if __name__ == '__main__':
    unittest.main()