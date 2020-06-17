from Naive468 import Solution as naive
import socket
from ipaddress import ip_address, IPv6Address

testcase = [
    ('172.16.254.1', 'IPv4'),
    ('2001:0db8:85a3:0:0:8A2E:0370:7334', 'IPv6'),
    ('2001:db8:85a3:0:0:8A2E:0370:7334', 'IPv6'),
    ('2001:0db8:85a3:0000:0000:8a2e:0370:7334', 'IPv6'),
    ('02001:0db8:85a3:0000:0000:8a2e:0370:733', 'Neither'),
    ('2001:0db8:85a3:00000:0:8A2E:0370:7334', 'Neither'),
    ('256.256.256.256', 'Neither'),
    ('2001:0db8:85a3::8A2E:0370:733', 'Neither'),
    ('haha.hehe.hihi.hoho', 'Neither'),
    ('zzzz:0:0:0000:0000:0:yyy:a0aa', 'Neither')
]


def test_naive():
    _test_with_answer(naive)
    # _test_with_socket(naive)
    # _test_with_ipaddress(naive)


def _test_with_answer(solution):
    for IP, ans in testcase:
        assert solution().validIPAddress(IP) == ans, IP


def _test_with_socket(solution):
    # https://stackoverflow.com/questions/319279/how-to-validate-ip-address-in-python
    for IP, _ in testcase:
        answer = 'Neither'
        try:
            socket.inet_pton(socket.AF_INET6, IP)
            answer = 'IPv6'
        except:
            pass

        try:
            socket.inet_pton(socket.AF_INET, IP)
            answer = 'IPv4'
        except:
            pass

        if answer == 'IPv6':
            if '' in IP.split(':'):
                # LeetCode don't replace a consecutive group of zero value with a single empty group two consecutive colons (::) to pursue simplicity
                answer = 'Neither'

        assert solution().validIPAddress(IP) == answer, IP


def _test_with_ipaddress(solution):
    # https://leetcode.com/problems/validate-ip-address/solution/
    for IP, _ in testcase:
        try:
            answer = 'IPv6' if type(ip_address(IP)) is IPv6Address else 'IPv4'
        except:
            answer = 'Neither'

        if answer == 'IPv6':
            if '' in IP.split(':'):
                # LeetCode don't replace a consecutive group of zero value with a single empty group two consecutive colons (::) to pursue simplicity
                answer = 'Neither'

        assert solution().validIPAddress(IP) == answer, IP
