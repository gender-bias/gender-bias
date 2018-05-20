from subprocess import Popen, PIPE
from pytest import fixture

script = ["genderbias"]
examples = ["example_letters/letterofRecM", "example_letters/letterofRecW"]

@fixture(params = examples)
def example(request):
    return request.param

@fixture(params = ["-f", "--file"])
def file_flag(request):
    return request.param

def output_with_options(options):
    popen = Popen(script + options, stdout=PIPE, universal_newlines=True)
    return popen.communicate()[0]


def test_script_help():
    help_text = 'usage: genderbias [-h] [--file FILE]\n\nCLI for gender-bias detection\n\noptional arguments:\n  -h, --help            show this help message and exit\n  --file FILE, -f FILE  The file to check\n'
    assert output_with_options(["-h"]) == help_text

def test_script_file_flags(example, file_flag):
    output = output_with_options([file_flag, example])
    for line in output.split("\n"):
        if line:
            assert line[0] == "["
