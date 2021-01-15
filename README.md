### PaperWithCode

PaperWithCode爬虫基于requests和beautifulsoup进行开发，能够爬取[Paper With Code](https://paperswithcode.com)上的论文资料，包括论文的标题、作者、摘要、发表时间、发表地址和官方代码地址，并且能够下载论文对应的PDF文件。

#### 代码目录结构：

```
./SpiderForPwC
├── README.md
├── progress
├── requirements.txt
├── run.py
└── utils
    ├── ClashControl.py
    ├── PDFDownloader.py
    ├── PcWCrawler.py
    ├── UrlCrawler.py
    ├── __init__.py
    ├── config.py
    ├── detailInfoCrawler.py
    └── progress
```

#### 工作模式：

1. 从https://portal.paperswithcode.com/ 可以得知，paperwithcode中的论文主要分为六类，分别是：Machine Learning, Computer Science, Physics, Mathematics, Astronomy, Statistics，他们各自有对应的二级域名，并且以url参数`/?page=x`来进行翻页操作，其中每页有10篇论文；
2. 对第一步中的论文列表页进行解析，获取每篇文章的paper页面，并获取其Abstract地址，可以获得一个指向[arxiv.org](https://arxiv.org/) 域名下的页面，其上包括了该篇论文的所有详情；
3. 解析第二部中所获得的详情页，即可获得目标论文的基本信息。将获取的基本信息构建成一个dict，写入到MongoDB数据库中，并将论文PDF下载到本地；
4. 该爬虫由两个爬取部分构成，其逻辑是分离的，分别是爬取paperwithcode上的论文链接，以及爬取论文的详情。此外，PDF的下载与这二者分离，三者只在使用数据上有所关联；
5. 爬虫各部分均实现增量式下载和爬取。其中爬取paperwithcode上的论文链接通过读写progress记录文件实现，爬取论文详情以及PDF下载通过检查数据表中的`visit`字段实现。因此爬虫每次运行时都会继续之前未完成的进度；
6. 网站使用的IP池方法详情见IP池文档。

#### 运行方法

爬虫可通过目录下的`run.py`文件运行：

```bash
cd SpiderForPwC
python run.py
```

#### 依赖

爬虫基于`Python 3`开发，库依赖见`requirements.txt`。

#### 分工：

- 张峄天：完成paperwithcode爬虫开发