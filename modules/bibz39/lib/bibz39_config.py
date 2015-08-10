# coding=utf-8


CFG_Z39_SERVER = {
    'Library of Congress': {'address': 'lx2.loc.gov', 'port': 210, 'databasename': 'LCDB',
                            'preferredRecordSyntax': 'USMARC'},
    'UNOG Library': {'address': 'eu.alma.exlibrisgroup.com', 'port': 1921,
                     'databasename': '41UNOG_INST',
                     'preferredRecordSyntax': 'USMARC', 'default': True},
    'University of Chicago': {'address': 'ole.uchicago.edu', 'port': 210, 'databasename': 'ole',
                              'preferredRecordSyntax': 'USMARC', 'default': False}}