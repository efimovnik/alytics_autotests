# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def test_column_settings_all_sources(app):
    app.project.open_project_page(project_id=6195)
    shows = app.wd.find_elements_by_class_name("rt-th-header")[0].text.encode('utf-8')
    rus = [].append('Показы')
    application = [].append(shows)
    str(shows)
    print (shows)
    assert application == rus
    old_columns = app.project.get_column_count()
    app.project.choose_parameter_in_traffic_columns()
    new_colums = app.project.get_column_count()
    print (old_columns)
    print (new_colums)
    assert old_columns - 1 == new_colums
    app.project.choose_parameter_in_traffic_columns()

