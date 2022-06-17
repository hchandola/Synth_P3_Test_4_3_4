from typing import List

def sat194(valids: List[str], filenames=['cat.txt', '!jog.dll', '31F9.html', 'Is this okay?.txt', '.exe', '']):
    assert len(valids) == len(filenames)
    for v, f in zip(valids, filenames):
        n_digits = sum(c.isdigit() for c in f)
        if v == "Yes":
            prefix, ext = f.split(".")
            assert ext in ["txt", "dll", "exe"] and prefix[0].isalpha() and n_digits < 4
        else:
            assert v == "No"
            assert f.split(".")[1:] not in [['txt'], ['dll'], ['exe']] or not f[0].isalpha() or n_digits > 3
    return True
def sol194(filenames=['cat.txt', '!jog.dll', '31F9.html', 'Is this okay?.txt', '.exe', '']):
    """Return a list of Yes/No strings that determine whether candidate filename is valid. A valid filename
    should end in .txt, .exe, or .dll, and should have at most three digits, no additional periods

    ["train.jpg", "doc10234.txt", "3eadme.txt"] = ["No", "No", "Yes"]
    """
    return ["Yes" if
            f.split(".")[1:] in [['txt'], ['dll'], ['exe']] and f[0].isalpha() and sum(c.isdigit() for c in f) < 4
            else "No"
            for f in filenames]
# assert sat194(sol194())
