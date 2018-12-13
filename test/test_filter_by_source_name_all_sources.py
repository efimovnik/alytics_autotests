# -*- coding: utf-8 -*-


def test_filter_autosources(app):
    app.project.open_project_page(project_id=6195)
    app.project.filter_source_contains(source_name=u"Google a")
    sources = app.project.get_sources_list()
    sources_filtered = [source for source in sources if source.find(u"Google") != -1]
    assert len(sources) == len(sources_filtered)