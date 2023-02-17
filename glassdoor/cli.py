import os

import click
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from linkedin import linkedin_spider


@click.command()
def main():
    os.environ["SCRAPY_SETTINGS_MODULE"] = "linkedin.settings"
    process = CrawlerProcess(settings=get_project_settings())
    process.crawl(linkedin_spider.LinkedinSpider)
    process.start()


if __name__ == "__main__":  # pragma: no cover
    main()  # pylint: disable=no-value-for-parameter
