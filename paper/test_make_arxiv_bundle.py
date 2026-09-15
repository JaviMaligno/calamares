"""The source bundle must include nested TeX inputs and their figures."""

from pathlib import Path
import tempfile
import unittest

from make_arxiv_bundle import collect_sources


class BundleSourceTests(unittest.TestCase):
    def test_nested_inputs_and_shared_figure_are_included_once(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root/'main.tex').write_text(r'\input{part}\includegraphics{plot.png}')
            (root/'part.tex').write_text(r'\input{leaf}\includegraphics{plot.png}')
            (root/'leaf.tex').write_text('A proof.')
            (root/'plot.png').write_bytes(b'figure')
            self.assertEqual({arc for _, arc in collect_sources(root)},
                             {'main.tex', 'part.tex', 'leaf.tex', 'plot.png'})
            self.assertEqual(len(collect_sources(root)), 4)

    def test_missing_input_is_an_error(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root/'main.tex').write_text(r'\input{missing}')
            with self.assertRaises(FileNotFoundError):
                collect_sources(root)

    def test_input_cycles_terminate_and_comments_are_ignored(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root/'main.tex').write_text('\\input{part}\n% \\input{absent}')
            (root/'part.tex').write_text(r'\input{main}')
            self.assertEqual(len(collect_sources(root)), 2)

    def test_source_outside_paper_directory_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            root = base/'paper'
            root.mkdir()
            (base/'private.tex').write_text('Outside the bundle root.')
            (root/'main.tex').write_text(r'\input{../private}')
            with self.assertRaises(ValueError):
                collect_sources(root)


if __name__ == '__main__':
    unittest.main()
