from pages.home_scan_page import HomeScan
from unittest import TestCase
import pytest


class TestScan:

    hs = HomeScan()
    # test_case = TestCase()

    def test_scan_by_album(self):
        r = self.hs.scan_by_album()
        TestCase().assertEqual(r, '扫描成功')

    # def test_scan_by_album_camera(self):
    #     r = self.hs.scan_by_album_camera()
    #     TestCase().assertEqual(r, '扫描成功')
    #
    # def test_scan_by_camera(self):
    #     r = self.hs.scan_by_camera()
    #     TestCase().assertEqual(r, '扫描成功')
