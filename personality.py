class MBTIScorer:
    """Track scores for the four MBTI dichotomies."""

    def __init__(self):
        self.scores = {
            'E': 0,
            'I': 0,
            'S': 0,
            'N': 0,
            'T': 0,
            'F': 0,
            'J': 0,
            'P': 0,
        }

    def add(self, dimension: str, points: int = 1) -> None:
        if dimension not in self.scores:
            raise ValueError(f"Invalid MBTI dimension: {dimension}")
        self.scores[dimension] += points

    def result_code(self) -> str:
        """Return the four letter MBTI code based on the current scores."""
        code = ''
        code += 'E' if self.scores['E'] >= self.scores['I'] else 'I'
        code += 'S' if self.scores['S'] >= self.scores['N'] else 'N'
        code += 'T' if self.scores['T'] >= self.scores['F'] else 'F'
        code += 'J' if self.scores['J'] >= self.scores['P'] else 'P'
        return code

    def interpretation(self) -> dict:
        code = self.result_code()
        return MBTI_DESCRIPTIONS.get(code, {'en': 'Unknown', 'cn': '未知'})


class EnneagramScorer:
    """Track scores for the nine Enneagram types."""

    def __init__(self):
        self.scores = {i: 0 for i in range(1, 10)}

    def add(self, type_id: int, points: int = 1) -> None:
        if type_id not in self.scores:
            raise ValueError(f"Invalid Enneagram type: {type_id}")
        self.scores[type_id] += points

    def result_type(self) -> int:
        max_score = max(self.scores.values())
        best = [t for t, s in self.scores.items() if s == max_score]
        return min(best)

    def interpretation(self) -> dict:
        t = self.result_type()
        return ENNEAGRAM_DESCRIPTIONS[t]


class BigFiveScorer:
    """Optional scoring for the Big Five traits (OCEAN)."""

    def __init__(self):
        self.scores = {'O': 0, 'C': 0, 'E': 0, 'A': 0, 'N': 0}

    def add(self, trait: str, points: int = 1) -> None:
        if trait not in self.scores:
            raise ValueError(f"Invalid trait: {trait}")
        self.scores[trait] += points

    def result(self) -> dict:
        return dict(self.scores)

    def interpretation(self) -> dict:
        return {t: BIGFIVE_DESCRIPTIONS[t] for t in self.scores}


MBTI_DESCRIPTIONS = {
    'INTJ': {'en': 'Architect', 'cn': '建筑师'},
    'INTP': {'en': 'Logician', 'cn': '逻辑学家'},
    'ENTJ': {'en': 'Commander', 'cn': '指挥官'},
    'ENTP': {'en': 'Debater', 'cn': '辩论家'},
    'INFJ': {'en': 'Advocate', 'cn': '提倡者'},
    'INFP': {'en': 'Mediator', 'cn': '调停者'},
    'ENFJ': {'en': 'Protagonist', 'cn': '主人公'},
    'ENFP': {'en': 'Campaigner', 'cn': '竞选者'},
    'ISTJ': {'en': 'Logistician', 'cn': '物流师'},
    'ISFJ': {'en': 'Defender', 'cn': '守卫者'},
    'ESTJ': {'en': 'Executive', 'cn': '执政官'},
    'ESFJ': {'en': 'Consul', 'cn': '领事官'},
    'ISTP': {'en': 'Virtuoso', 'cn': '鉴赏家'},
    'ISFP': {'en': 'Adventurer', 'cn': '探险家'},
    'ESTP': {'en': 'Entrepreneur', 'cn': '企业家'},
    'ESFP': {'en': 'Entertainer', 'cn': '表演者'},
}

ENNEAGRAM_DESCRIPTIONS = {
    1: {'en': 'Reformer', 'cn': '改革者'},
    2: {'en': 'Helper', 'cn': '助人者'},
    3: {'en': 'Achiever', 'cn': '成就者'},
    4: {'en': 'Individualist', 'cn': '自我者'},
    5: {'en': 'Investigator', 'cn': '观察者'},
    6: {'en': 'Loyalist', 'cn': '忠诚者'},
    7: {'en': 'Enthusiast', 'cn': '热情者'},
    8: {'en': 'Challenger', 'cn': '挑战者'},
    9: {'en': 'Peacemaker', 'cn': '和平者'},
}

BIGFIVE_DESCRIPTIONS = {
    'O': {'en': 'Openness', 'cn': '开放性'},
    'C': {'en': 'Conscientiousness', 'cn': '尽责性'},
    'E': {'en': 'Extraversion', 'cn': '外向性'},
    'A': {'en': 'Agreeableness', 'cn': '宜人性'},
    'N': {'en': 'Neuroticism', 'cn': '情绪稳定性'},
}

