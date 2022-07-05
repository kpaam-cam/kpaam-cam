from clld.web.maps import Map


class LanguagesMap(Map):

    def get_options(self):
        return {'max_zoom': 15}


def includeme(config):
    config.register_map('languages', LanguagesMap)

