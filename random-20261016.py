# small utilities, no deps

def clamp(value, low, high):
    return max(low, min(value, high))

def most_common(xs):
    return max(set(xs), key=xs.count) if xs else None

def load_lines(path):
    with open(path, encoding="utf-8") as f:
        return [ln.strip() for ln in f if ln.strip()]

# cleanup later
