import unittest
from PythonFlaskExercise import number, hello_world_var

class TestMyCode(unittest.TestCase):
    def test_character_count(self):
        result = number(hello_world_var)
        self.assertEqual(result, 13)

if __name__ == '__main__':
    unittest.main()
