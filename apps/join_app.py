__author__ = 'sunary'


from base_apps.pipe_app import PipeApp
from deploy.chain_processor import CONTENT_KEY


class JoinApp(PipeApp):
    '''
    Join messages from previous processor
    '''
    def init_app(self, batch_size=None):
        self.batch_size = batch_size
        self.stored_messages = {CONTENT_KEY: []}

    def start(self):
        self.logger.info('Start {}'.format(self.__class__.__name__))

    def process(self, message=None):
        return message