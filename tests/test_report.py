from genderbias.detector import Report, Issue, Flag

from pytest import fixture

report_name = "Text Analyzer"
summary = "[summary]"
flag = Flag(0, 10, Issue(report_name, "A", "B"))
positive_flag = Flag(20, 30, Issue(report_name, "C", "D", bias = Issue.positive_result))

no_summary_text = " SUMMARY: [None available]"
flag_text = " [0-10]: " + report_name + ": A (B)"

@fixture
def report():
    return Report(report_name)


def test_report_str_no_flags(report):
    assert str(report) == "\n".join([report_name, no_summary_text])

def test_report_str_with_one_flag(report):
    report.add_flag(flag)
    assert str(report) == "\n".join([report_name, flag_text, no_summary_text])

def test_report_str_no_flags_with_summary(report):
    report.set_summary(summary)
    assert str(report) == "\n".join([report_name, " SUMMARY: " + summary])


def test_report_to_dict_no_flags(report):
    expected = {'name': report_name, 'summary': "", 'flags': []}
    assert report.to_dict() == expected

def test_report_to_dict_with_one_flag(report):
    report.add_flag(flag)
    expected = {'name': report_name, 'summary': "",
                'flags': [(0, 10, report_name, "A", "B")]
    }
    assert report.to_dict() == expected

def test_report_to_dict_with_summary(report):
    report.set_summary(summary)
    expected = {'name': report_name, 'summary': summary, 'flags': []}
    assert report.to_dict() == expected


def test_report_with_positive_flags(report):
    report.add_flag(positive_flag)
    assert str(report) == "\n".join([report_name, no_summary_text])
    report.add_flag(positive_flag)
    assert str(report) == "\n".join([report_name, no_summary_text])

def test_report_with_mixed_flags(report):
    report.add_flag(positive_flag)
    report.add_flag(flag)
    assert str(report) == "\n".join([report_name, flag_text, no_summary_text])
