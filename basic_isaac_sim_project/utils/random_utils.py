import random

def seeded_random(seed: int = 42) -> random.Random:
    rng = random.Random(seed)
    return rng
