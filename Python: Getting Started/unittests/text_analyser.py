import unittest
import os


def analyze_text(filename):
    lines = 0
    chars = 0

    with open(filename, 'r') as f:
        for line in f:
            lines += 1
            chars += len(line)

    return tuple([lines, chars])


class TextAnalysisTests(unittest.TestCase):

    def test_function_runs(self):
        analyze_text(self.filename)

    def test_line_count(self):
        self.assertEqual(analyze_text(self.filename)[0], 2)

    def test_character_count(self):
        self.assertEqual(analyze_text(self.filename)[1], 11)

    def test_no_such_file(self):
        with self.assertRaises(IOError):
            analyze_text('foobar')

    def test_no_deletion(self):
        analyze_text(self.filename)
        self.assertTrue(os.path.exists(self.filename))

    def setUp(self):
        self.filename = 'testfile.txt'
        with open(self.filename, "w") as f:
            f.write('Test\nasdasd')

    def tearDown(self):
        try:
            os.remove(self.filename)
        except:
            pass




if __name__ == "__main__":
    unittest.main()