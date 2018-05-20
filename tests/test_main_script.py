from subprocess import Popen, PIPE
from pytest import fixture

script = ["genderbias"]
examples = ["example_letters/letterofRecM", "example_letters/letterofRecW"]

@fixture(params = examples)
def example(request):
    return request.param

def test_script_help():
    popen = Popen(script + ["-h"], stdout=PIPE, universal_newlines=True)
    output = popen.communicate()[0]
    help_text = 'usage: genderbias [-h] [--file FILE]\n\nCLI for gender-bias detection\n\noptional arguments:\n  -h, --help            show this help message and exit\n  --file FILE, -f FILE  The file to check\n'
    assert output == help_text

def test_script_file_flags(example):
    popen = Popen(script + ["-f", example], stdout=PIPE, universal_newlines=True)
    output = popen.communicate()[0]
    for line in output.split("\n"):
        if line:
            assert line[0] == "["
