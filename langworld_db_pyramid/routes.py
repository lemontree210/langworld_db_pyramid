def includeme(config):
    config.add_static_view('css', 'static/css', cache_max_age=3600)
    config.add_static_view('img', 'static/images', cache_max_age=3600)
    config.add_static_view('scripts', 'static/js', cache_max_age=3600)
    config.add_static_view('pdf', 'static/pdf_volumes', cache_max_age=3600)
    config.add_route('all_doculects', '/')
    config.add_route('doculect_profile', '/doculect/{doculect_man_id}')
    config.add_route('doculect_man_ids_containing_substring', '/{locale}/json_api/doculect_by_name/{query}')
