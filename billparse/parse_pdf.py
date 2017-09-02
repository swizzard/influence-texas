from io import BytesIO

from pdfminer import high_level
import requests


def parse_pdf(pdf_fp, decode='utf8'):
    """
    Read a PDF into a python (byte)string
    :param pdf_fp: file-like object containing PDF
    :param decode: decoding to use
    """
    return pdf_fp.decode(decode)

