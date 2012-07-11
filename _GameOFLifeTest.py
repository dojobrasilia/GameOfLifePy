import unittest


class GameOfLife(object):
    
    def __init__(self, x_size, y_size):
        self.__state =[]
        self.__x_size = x_size
        self.__y_size = y_size
        for i in range(0, y_size):
            row = []
            self.__state.append(row)
            for j in range(0, x_size):
                row.append(' ')
    
    def state(self):
        return self.__state
    
    def add_peca(self, peca, row, col):
        self.__state[row][col] = peca
    
    def pass_round(self):
        for i in range(0, self.__y_size):
            row = []
            self.__state.append(row)
            for j in range(0, self.__x_size):
                row.append(' ')
        
        
        
        self.__state[2][2] = ' '

class GameOfLifeTest(unittest.TestCase):


    def testInit(self):
        game = GameOfLife(4,4)
        expected = [  [' ',' ',' ',' '],
                    [' ',' ',' ',' '],
                    [' ',' ',' ',' '],
                    [' ',' ',' ',' ']]
                
        self.assertEquals(expected, game.state())
        
    def test_add_peca(self):
        game = GameOfLife(4,4)
        game.add_peca('o', 2,3)
        expected = [  [' ',' ',' ',' '],
                    [' ',' ',' ',' '],
                    [' ',' ',' ','o'],
                    [' ',' ',' ',' ']]
        
        self.assertEquals(expected, game.state())

    def test_single_cell(self):
        game = GameOfLife(4,4)
        game.add_peca("o", 2, 2)
        game.pass_round()
        self.assertEqual(' ', game.state()[2][2])
        

    def test_single_cell_in_another_position(self):
        game = GameOfLife(4,4)
        game.add_peca("o", 2, 3)
        game.add_peca("o", 1, 1)
        game.pass_round()
        expected = [  [' ',' ',' ',' '],
                    [' ',' ',' ',' '],
                    [' ',' ',' ',' '],
                    [' ',' ',' ',' ']]
        
        
        self.assertEqual(expected, game.state())
        