# Reproduce the main numbers quoted in README/METHOD from the data in this repository.
import os, sys, unittest, subprocess
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'src'))
import vk

PAGES = ['p033', 'p525', 'p526', 'p539', 'p561', 'p562', 'p563', 'p565', 'p570']


def decode(page):
    key = {k: v for k, (v, s) in vk.TOKENS.items()}
    rows = vk.load(os.path.join(ROOT, 'data', 'transcription', page + '.txt'))
    return dict(vk.decode(rows, key))


class TestKey(unittest.TestCase):
    def test_all_tokens_known(self):
        # every token in the final transcriptions is in the key (or a plain group / unreadable mark)
        key = {k for k in vk.TOKENS}
        for p in PAGES:
            for lid, toks in vk.load(os.path.join(ROOT, 'data', 'transcription', p + '.txt')):
                for t in toks:
                    t2 = t[:-1] if t.endswith('?') and len(t) > 1 else t
                    self.assertTrue(t2 in key or t2 in ('|', '?') or t.startswith('{'), f'{p} {lid} {t}')

    def test_decoded_files_match(self):
        for p in PAGES:
            got = decode(p)
            for ln in open(os.path.join(ROOT, 'data', 'decoded', p + '.txt'), encoding='utf-8'):
                lid, _, s = ln.rstrip('\n').partition('\t')
                self.assertEqual(got[lid], s, f'{p} {lid}')

    def test_sample_readings(self):
        self.assertIn('neuouDraauouerdIrecteMentceFaitdeuant', decode('p525')['525.04'])
        self.assertIn('les espagnOlz', decode('p539')['539.05'])
        self.assertIn('lemarQuizdeuareMb', decode('p565')['565.05'])
        self.assertIn('pa[ss]e outre', decode('p033')['33.08'])


class TestIndependentSecond(unittest.TestCase):
    def test_agreement_total(self):
        out = subprocess.run([sys.executable, os.path.join(ROOT, 'src', 'xcompare.py')] + PAGES,
                             env=dict(os.environ, PASS='pass2', FIRST='', FIRST_DIR=os.path.join('data', 'transcription')),
                             capture_output=True, text=True, cwd=ROOT).stdout
        self.assertIn('TOTAL: 4017/4637', out)

    def test_agreement_pass3(self):
        for ps, total in [('pass3a', '4402/4637'), ('pass3b', '4380/4637'), ('pass3c', '4392/4637')]:
            out = subprocess.run([sys.executable, os.path.join(ROOT, 'src', 'xcompare.py')] + PAGES,
                                 env=dict(os.environ, PASS=ps, FIRST='', FIRST_DIR=os.path.join('data', 'transcription')),
                                 capture_output=True, text=True, cwd=ROOT).stdout
            self.assertIn('TOTAL: ' + total, out, ps)


class TestCalibration(unittest.TestCase):
    def test_p258(self):
        out = subprocess.run([sys.executable, os.path.join(ROOT, 'src', 'calib.py'),
                              os.path.join(ROOT, 'calib', 'p258_decode.tsv'), os.path.join(ROOT, 'calib', 'p258_margin_adj_text.txt')],
                             capture_output=True, text=True).stdout
        self.assertIn('scored letters 412, agree 333 (80.8%)', out)


if __name__ == '__main__':
    unittest.main()
