import program_12_2
import unittest

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_result = {}

    @classmethod
    def tearDownClass(cls):
        formatted_result = {place: name for place, name in cls.all_result.items()}
        print(formatted_result)


    def setUp(self):
        self.runner1 = program_12_2.Runner('Usain', speed=10)
        self.runner2 = program_12_2.Runner('Andry', speed=9)
        self.runner3 = program_12_2.Runner('Nick', speed=3)



    def test_run1(self):
        championship1 = program_12_2.Tournament(90, self.runner1, self.runner3)
        result = championship1.start()
        for key, value in result.items():
            self.all_result[key] = value
        self.assertEqual(result[2], 'Andry')




if __name__ == '__main__':
    unittest.main()



