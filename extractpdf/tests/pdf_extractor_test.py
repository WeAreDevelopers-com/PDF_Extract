# -*- coding: utf-8 -*-
import unittest

from extractpdf.pdf_extractor import PDFExtractor

class PDFExtracotTest(unittest.TestCase):
    def test_extractpdf_can_handle_empty_urls(self):
        pe = PDFExtractor()
        self.assertRaises(AssertionError, pe.get_content, "")

    def test_extractpdf_can_handle_broken_urls(self):
        pe = PDFExtractor()
        self.assertRaises(AssertionError, pe.get_content, "https://arxiv.org/pdf/")

    @classmethod
    def test_extractpdf_conversion(cls):
        pe = PDFExtractor()
        c = pe.get_content("https://arxiv.org/pdf/1708.03615.pdf")

        if not len(c) > 0:
            raise AssertionError("pdf extracted content is empty")
