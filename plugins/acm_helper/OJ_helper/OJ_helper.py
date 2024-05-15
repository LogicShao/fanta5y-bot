class OJHelper:
    def __init__(self, url: str='127.0.0.1', port: int=7890):
        # set the url and port for the proxy
        if url is None:
            self.proxies: dict = None
        else:
            self.proxies: dict = {
                'http': 'http://{url}:{port}'.format(url=url, port=port),
                'https': 'http://{url}:{port}'.format(url=url, port=port),
            }
