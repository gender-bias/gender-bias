
examples = dict(m="../example_letters/letterofRecM",
                f="../example_letters/letterofRec_W")

def test_can_read_examples():
    for file in examples.values():
        with open(file, 'r') as stream:
            assert stream.readable()
