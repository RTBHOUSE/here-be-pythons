import socket
import urllib.error

from find_broken_links import find_broken_links


class HTTPErrorStub(urllib.error.HTTPError):
    code = 404

    def __init__(self):
        pass


class URLErrorStub(urllib.error.URLError):
    def __init__(self):
        pass


class TestFindBrokenLinks:
    def test_exits_with_1_when_some_links_are_broken(self, mocker):
        def yield_http_errors():
            while True:
                yield HTTPErrorStub

        # GIVEN
        sys_exit_mock = mocker.patch('sys.exit')
        mocker.patch('urllib.request.urlopen', side_effect=yield_http_errors())

        # WHEN
        find_broken_links(files_glob_pattern='tests/files/*.rst')

        # THEN
        sys_exit_mock.assert_called_once_with(1)

    def test_exits_with_0_when_no_links_are_broken(self, mocker):
        # GIVEN
        sys_exit_mock = mocker.patch('sys.exit')
        mocker.patch('urllib.request.urlopen')

        # WHEN
        find_broken_links(files_glob_pattern='tests/files/*.rst')

        # THEN
        sys_exit_mock.assert_called_once_with(0)

    def test_prints_report(self, mocker, capsys):
        # GIVEN
        mocker.patch('sys.exit')
        mocker.patch(
            target='urllib.request.urlopen',
            side_effect=[
                'OK 1',
                'OK 2',
                'OK 3',
                'OK 4',
                HTTPErrorStub,  # Should result in a Broken URL
                URLErrorStub,  # Should be ignored
                socket.timeout,  # Should result in a Timed-Out URL
            ]
        )

        # WHEN
        find_broken_links(files_glob_pattern='tests/files/*.rst')

        # THEN
        expected_prints = """
            url:       http://www.pirate-url5.com
            returns:   404
            file:      tests/files/foo.rst:3
            
            url:       http://www.pirate-url6.com
            returns:   666
            file:      tests/files/foo.rst:5
            
            Timeout on: https://pirateipsum.me
            
            Broken Links Report
            ===================
            OK:          4 URLs
            Broken:      2 URLs
            Timed-out:   1 URL
            
            --------------------------
            Timeout set for 5 seconds.
        """.split('\n')

        captured = capsys.readouterr()
        for expected_print in expected_prints:
            assert expected_print.strip() in captured.out

        expected_lines_num = len(expected_prints)
        actual_lines_num = len(captured.out.split('\n'))
        assert expected_lines_num == actual_lines_num
