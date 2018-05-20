from genderbias.detector import Report, Issue, Flag

report_name = "Text Analyzer"
summary = "[summary]"

def test_report_str_no_flags():
    r = Report(report_name)
    assert str(r) == report_name

f = Flag(0, 10, Issue(report_name, "A" "B"))

def test_report_str_with_one_flag():
    r = Report(report_name)
    r.add_flag(f)
    expected = report_name + "\n [0-10]: " + report_name + ": AB"
    assert str(r) == expected

def test_report_str_no_flags_with_summary():
    r = Report(report_name)
    r.set_summary(summary)
    assert str(r) == report_name + "\n" + " SUMMARY: " + summary
