import personality


def test_mbti_scorer_basic():
    scorer = personality.MBTIScorer()
    for d in ['E', 'S', 'T', 'J']:
        scorer.add(d, 2)
    for d in ['I', 'N', 'F', 'P']:
        scorer.add(d, 1)
    assert scorer.result_code() == 'ESTJ'
    info = scorer.interpretation()
    assert info['en'] == 'Executive'
    assert info['cn'] == '执政官'


def test_enneagram_scorer():
    scorer = personality.EnneagramScorer()
    scorer.add(3, 5)
    scorer.add(1, 2)
    assert scorer.result_type() == 3
    info = scorer.interpretation()
    assert info['en'] == 'Achiever'
    assert info['cn'] == '成就者'


def test_bigfive_scorer():
    scorer = personality.BigFiveScorer()
    scorer.add('O', 3)
    scorer.add('C', 2)
    scorer.add('E', 1)
    res = scorer.result()
    assert res['O'] == 3
    assert res['C'] == 2
    assert res['E'] == 1
    desc = scorer.interpretation()
    assert desc['O']['cn'] == '开放性'

