class Resource(object):

    @staticmethod
    def get(request, **kwargs):
        return NotImplemented()

    @staticmethod
    def post(request, **kwargs):
        return NotImplemented()

    @staticmethod
    def delete(self, request, **kwargs):
        return NotImplemented()

    @staticmethod
    def put(request, **kwargs):
        return NotImplemented()

    def __call__(self, request, **kwargs):
        handler = getattr(self, request.method)
        return handler(request, **kwargs)