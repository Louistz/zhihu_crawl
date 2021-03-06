import random

from zhihu_crawl.middleware.proxy import PROXIES
from zhihu_crawl.middleware.agents import AGENTS
import logging


class CustomHttpProxyMiddleware(object):

    def process_request(self, request, spider):
        if self.use_proxy(request):
            proxy =random.choice(PROXIES)
            logging.info('Using proxy ' + proxy['ip_port'])
            request.meta['proxy'] = 'http://' + proxy['ip_port']

    def use_proxy(self, request):
        if 'proxy' in request.meta:
            logging.info('Proxy has already been used')
            return

        if "depth" in request.meta and int(request.meta['depth']) <= 2:
            return False

        return random.randint(0, 99) >=30


class CustomUserAgentMiddleware(object):

    def process_request(self, request, spider):
        agent = random.choice(AGENTS)
        request.headers['User-Agent'] = agent


class MyMiddleware(object):

    def process_request(self,request,spider):
        #print request.headers
        #print request.meta
        pass

    def process_response(self, request, response, spider):
        #print response.headers
        return response

