from genderbias.detector import Report

report_name = "Text Analyzer"

def test_report_str_no_flags():
    r = Report(report_name)
    assert str(r) == report_name
