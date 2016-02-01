# -*- coding: utf-8 -*-

# Scrapy settings for zhihu_crawl project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhihu_crawl'

SPIDER_MODULES = ['zhihu_crawl.spiders']
NEWSPIDER_MODULE = 'zhihu_crawl.spiders'

LOG_FILE = 'zhihu.log'
LOG_LEVEL= 'INFO'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhihu_crawl (+http://www.yourdomain.com)'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS=50
CONCURRENT_ITEMS = 100
# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY=0.5
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN=16
CONCURRENT_REQUESTS_PER_IP=5

# Disable cookies (enabled by default)
COOKIES_ENABLED=False
COOKIES_DEBUG =True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED=False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    #'zhihu_crawl.middleware.middleware.CustomHttpProxyMiddleware': 80,
    'scrapy.contrib.downloadermiddleware.cookies.CookiesMiddleware':80,
 }

# Enable or disable downloader middlewares
#See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
     #'zhihu_crawl.middleware.middleware.CustomHttpProxyMiddleware': 80,
    'scrapy.contrib.downloadermiddleware.cookies.CookiesMiddleware':80,
    'zhihu_crawl.middleware.middleware.MyMiddleware':81,
 }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'zhihu_crawl.pipeline.pipeline.ZhihuUserMongoPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
#AUTOTHROTTLE_ENABLED=True
# The initial download delay
#AUTOTHROTTLE_START_DELAY=5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY=60
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG=False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED=True
#HTTPCACHE_EXPIRATION_SECS=0
#HTTPCACHE_DIR='httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES=[]
#HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage'


COOKIES = {
    '__utma':r'51854390.1567494124.1433823624.1453444514.1453444514.1',
    '__utmb':r'51854390.9.9.1453444528002',
    '__utmc':r'51854390',
    '__utmt':r'1',
    '__utmv':r'51854390.100-1|2=registration_date=20130525=1^3=entry_date=20130525=1',
    '__utmz':r'51854390.1453444514.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
    '__ga'  :r'GA1.2.1567494124.1433823624',
    '_xsrf' :r'0166e4a684652803204359a203d61e77',
    '_za'   :r'92e45523-abde-4b21-b984-f1418a7721bd',
    'cap_id':r'"MWYxNDE0YzE0YTIwNDE3NGE2NzFjMjc0ODcxYTVmNmI=|1453444820|e662c5a521ed0cdcfd854bb48048f5b32bc771a4"',
    'q_c1'  :r'0304c5e6ff1446bea9b248fd0e17ca3d|1451267956000|1426775382000',
    'unlock_ticket':'"QUFDQVFaVWJBQUFYQUFBQVlRSlZUWmZYb1ZhTVMtOVlOdXlTVllvMTAwNFBrUnB2M3NqM0J3PT0=|1453445263|485e91c672fbe81eda1b97579e9e500375afe885"',
    'z_co'  : r'"QUFDQVFaVWJBQUFYQUFBQVlRSlZUWTlkeVZiZ1M5ZkRsM21JWVIzWndNOXI1QnhkdHU3NkR3PT0=|1453445263|f78ac40c6ee48cf0d80c32823b40a4a376e454ea"'
}

HEADER = {
    "Host": "www.zhihu.com",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36",
    "Accept-Encoding": "gzip,deflate,sdch",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-TW;q=0.2",
    'Cookie':u''
}

MONGO = {
    'host':'localhost',
    'port':27017,
    'db':'zhihu',
    'collection':'user',
}

ZHIHU_ACCOUNT = {
    'username':"username",
    'password':"********",
}