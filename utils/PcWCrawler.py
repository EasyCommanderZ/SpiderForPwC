# coding : utf-8
import sys
sys.path.append('./utils/') # noqa
from UrlCrawler import UrlCrawler # noqa
from PDFDownloader import PDFDownloader # noqa
from detailInfoCrawler import detailInfoCrawler # noqa
from tqdm import tqdm # noqa


class PcWCrawler:
    def __init__(self):
        self.urlCrawler = UrlCrawler()
        self.pdfDownloader = PDFDownloader()
        self.detailInfoCrawler = detailInfoCrawler()

    def run(self):
        self.urlCrawler.crawlAll()
        self.detailInfoCrawler.crawlAllInfo()
        self.pdfDownloader.downloadAll()
        print("All crawlers finished.")


if __name__ == '__main__':
    pcWCrawler = PcWCrawler()
    pcWCrawler.run()
