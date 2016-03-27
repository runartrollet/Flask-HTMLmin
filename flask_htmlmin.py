from htmlmin import Minifier

__author__ = 'Hamid FzM'


class HTMLMIN(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('MINIFY_PAGE', False)

        if app.config['MINIFY_PAGE']:
            app.after_request(self.response_minify)

    @staticmethod
    def response_minify(response):
        """
        minify response html to decrease traffic
        """
        html_minify = Minifier(
            remove_comments=True,
            reduce_empty_attributes=True,
            remove_optional_attribute_quotes=False)

        if response.content_type == u'text/html; charset=utf-8':
            response.set_data(
                html_minify.minify(response.get_data(as_text=True))
            )

            return response
        return response
