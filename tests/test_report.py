from genderbias.detector import Report, Issue, Flag

from pytest import fixture

report_name = "Text Analyzer"
summary = "[summary]"
flag = Flag(0, 10, Issue(report_name, "A" "B"))


@fixture
def report():
    return Report(report_name)


def test_report_str_no_flags(report):
    assert str(report) == report_name + "\n" + " SUMMARY: " + "[None available]"

def test_report_str_with_one_flag(report):
    report.add_flag(flag)
    expected = (report_name + "\n [0-10]: " + report_name + ": AB" + "\n" +
                " SUMMARY: " + "[None available]")
    assert str(report) == expected

def test_report_str_no_flags_with_summary(report):
    report.set_summary(summary)
    assert str(report) == report_name + "\n" + " SUMMARY: " + summary

def test_report_to_dict_no_flags(report):
    expected = {'name': report_name, 'summary': "", 'flags': []}
    assert report.to_dict() == expected

def test_report_to_dict_with_one_flag(report):
    report.add_flag(flag)
    expected = {'name': report_name, 'summary': "",
                'flags': [(0, 10, report_name, "AB", "")]
    }
    assert report.to_dict() == expected

def test_report_to_dict_with_summary(report):
    report.set_summary(summary)
    expected = {'name': report_name, 'summary': summary, 'flags': []}
    assert report.to_dict() == expected
