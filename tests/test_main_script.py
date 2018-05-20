from subprocess import Popen, PIPE

script = ["genderbias"]

def test_script_help():
    popen = Popen(script + ["-h"], stdout=PIPE, universal_newlines=True)
    output = popen.communicate()[0]
    help_text = 'usage: genderbias [-h] [--file FILE]\n\nCLI for gender-bias detection\n\noptional arguments:\n  -h, --help            show this help message and exit\n  --file FILE, -f FILE  The file to check\n'
    assert output == help_text
