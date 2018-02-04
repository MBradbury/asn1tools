EXPECTED = {'ModuleTagsExplicit': {'extensibility-implied': False,
                        'imports': {},
                        'object-classes': {},
                        'object-sets': {},
                        'types': {'AE': {'tag': {'number': 3},
                                         'type': 'INTEGER'},
                                  'AI': {'tag': {'kind': 'IMPLICIT',
                                                 'number': 3},
                                         'type': 'INTEGER'},
                                  'BEAE': {'tag': {'number': 4}, 'type': 'AE'},
                                  'BIAE': {'tag': {'kind': 'IMPLICIT',
                                                   'number': 4},
                                           'type': 'AE'},
                                  'BIAI': {'tag': {'kind': 'IMPLICIT',
                                                   'number': 4},
                                           'type': 'AI'},
                                  'C1': {'members': [{'members': [{'name': 'a',
                                                                   'tag': {'number': 0},
                                                                   'type': 'INTEGER'}],
                                                      'name': 'a',
                                                      'tag': {'number': 0},
                                                      'type': 'CHOICE'}],
                                         'type': 'CHOICE'},
                                  'CEBEAE': {'tag': {'number': 5},
                                             'type': 'BEAE'},
                                  'CEBIAI': {'tag': {'number': 5},
                                             'type': 'BIAI'},
                                  'CIBIAE': {'tag': {'kind': 'IMPLICIT',
                                                     'number': 5},
                                             'type': 'BIAE'},
                                  'CIBIAI': {'tag': {'kind': 'IMPLICIT',
                                                     'number': 5},
                                             'type': 'BIAI'},
                                  'S1': {'members': [{'name': 'a',
                                                      'type': 'INTEGER'},
                                                     {'name': 'b',
                                                      'optional': True,
                                                      'type': 'BOOLEAN'}],
                                         'type': 'SEQUENCE'},
                                  'S2': {'members': [{'name': 'a',
                                                      'type': 'INTEGER'},
                                                     {'name': 'b',
                                                      'tag': {'number': 2},
                                                      'type': 'S1'},
                                                     {'members': [{'name': 'a',
                                                                   'type': 'BOOLEAN'}],
                                                      'name': 'c',
                                                      'type': 'CHOICE'}],
                                         'type': 'SEQUENCE'},
                                  'S3': {'members': [{'name': 'a',
                                                      'type': 'INTEGER'},
                                                     {'name': 'b',
                                                      'tag': {'number': 2},
                                                      'type': 'S1'},
                                                     {'members': [{'name': 'a',
                                                                   'type': 'BOOLEAN'}],
                                                      'name': 'c',
                                                      'tag': {'kind': 'EXPLICIT',
                                                              'number': 3},
                                                      'type': 'CHOICE'}],
                                         'type': 'SEQUENCE'},
                                  'S4': {'members': [{'name': 'a',
                                                      'type': 'INTEGER'},
                                                     {'name': 'b',
                                                      'tag': {'number': 1},
                                                      'type': 'C1'},
                                                     {'name': 'c',
                                                      'tag': {'number': 2},
                                                      'type': 'S1'},
                                                     {'members': [{'name': 'a',
                                                                   'type': 'BOOLEAN'}],
                                                      'name': 'd',
                                                      'type': 'CHOICE'}],
                                         'type': 'SEQUENCE'},
                                  'S5': {'members': [{'name': 'a',
                                                      'type': 'INTEGER'},
                                                     {'name': 'b',
                                                      'type': 'S1'},
                                                     {'members': [{'name': 'a',
                                                                   'type': 'BOOLEAN'}],
                                                      'name': 'c',
                                                      'type': 'CHOICE'}],
                                         'type': 'SEQUENCE'},
                                  'S6': {'members': [{'name': 'a',
                                                      'type': 'INTEGER'},
                                                     '...',
                                                     {'name': 'b',
                                                      'type': 'BOOLEAN'}],
                                         'type': 'SEQUENCE'},
                                  'S7': {'members': [{'name': 'a',
                                                      'tag': {'number': 2},
                                                      'type': 'INTEGER'},
                                                     '...',
                                                     {'name': 'b',
                                                      'type': 'BOOLEAN'}],
                                         'type': 'SEQUENCE'}},
                        'values': {}}}