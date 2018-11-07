import logging

server_logger = logging.getLogger(__name__)
server_logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

handler.setFormatter(formatter)
server_logger.addHandler(handler)
