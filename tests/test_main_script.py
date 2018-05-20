from subprocess import Popen, PIPE
import os
from pytest import fixture

script = ["genderbias"]
examples = ["example_letters/letterofRecM", "example_letters/letterofRecW"]

@fixture(params = examples)
def example(request):
    return request.param

@fixture(params = ["-f", "--file"])
def file_flag(request):
    return request.param

def output_with_options(options, feed_in=""):
    popen = Popen(script + options, stdin=PIPE, stdout=PIPE, universal_newlines=True)
    return popen.communicate(feed_in)[0]


def test_meta_ensure_examples_exist(example):
    assert os.path.isfile(example)

def test_script_help():
    help_text = 'usage: genderbias [-h] [--file FILE]\n\nCLI for gender-bias detection\n\noptional arguments:\n  -h, --help            show this help message and exit\n  --file FILE, -f FILE  The file to check\n'
    assert output_with_options(["-h"]) == help_text

def test_script_file_flags(example, file_flag):
    output = output_with_options([file_flag, example])
    for line in output.split("\n"):
        if line:
            assert line[0] == "["

def test_script_input_from_stdin(example):
    with open(example) as stream:
        text = stream.read()
    output = output_with_options([], feed_in=text)
    for line in output.split("\n"):
        if line:
            assert line[0] == "["
