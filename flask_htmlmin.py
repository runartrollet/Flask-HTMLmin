from htmlmin import minify

__author__ = 'Hamid FzM'


class HTMLMIN(object):
    def __init__(self, app=None, **kwargs):
        self.app = app
        if app is not None:
            self.init_app(app)

        self.default_options = {
            'remove_comments': True,
            'reduce_empty_attributes': True,
            'remove_optional_attribute_quotes': False
        }
        self.default_options.update(kwargs)

    def init_app(self, app):
        app.config.setdefault('MINIFY_PAGE', False)

        if app.config['MINIFY_PAGE']:
            app.after_request(self.response_minify)

    def response_minify(self, response):
        """
        minify response html to decrease traffic
        """
        if response.content_type == u'text/html; charset=utf-8':
            response.direct_passthrough = False
            response.set_data(
                minify(
                    response.get_data(as_text=True),
                    **self.default_options
                )
            )

            return response
        return response
