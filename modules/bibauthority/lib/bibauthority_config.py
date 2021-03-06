# coding=utf-8
# This file is part of Invenio.
# Copyright (C) 2006, 2007, 2008, 2009, 2010, 2011, 2013 CERN.
#
# Invenio is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.


# constants for CFG_BIBEDIT_AUTOSUGGEST_TAGS
# CFG_BIBAUTHORITY_AUTOSUGGEST_SORT_ALPHA for alphabetical sorting
# ... of drop-down suggestions
# CFG_BIBAUTHORITY_AUTOSUGGEST_SORT_POPULAR for sorting of drop-down
# ... suggestions according to a popularity ranking
try:
    from invenio.config import CFG_BIBAUTHORITY_AUTOSUGGEST_SORT_ALPHA
except ImportError:
    CFG_BIBAUTHORITY_AUTOSUGGEST_SORT_ALPHA = 'alphabetical'
try:
    from invenio.config import CFG_BIBAUTHORITY_AUTOSUGGEST_SORT_POPULAR
except ImportError:
    CFG_BIBAUTHORITY_AUTOSUGGEST_SORT_POPULAR = 'by popularity'


# the record field for authority control numbers
try:
    from invenio.config import CFG_BIBAUTHORITY_RECORD_AUTHOR_CONTROL_NUMBER_FIELDS
except ImportError:
    CFG_BIBAUTHORITY_RECORD_AUTHOR_CONTROL_NUMBER_FIELDS = {
        'AUTHOR': ['100', '700', '600'],
        'CORPORATE': ['110', '710', '610'],
        'MEETING': ['111', '711', '611'],
        'UNIFORM': ['130', '730'],
        'SUBJECT': ['150', '650'],
        'GEOGRAPHICAL': ['151', '751', '651'],
        'GENRE': ['155']
    }

try:
    from invenio.config import CFG_BIBAUTHORITY_RECORD_AUTHOR_CONTROL_NUMBER_FIELDS_REVERSED
except ImportError:
    CFG_BIBAUTHORITY_RECORD_AUTHOR_CONTROL_NUMBER_FIELDS_REVERSED = {
        '100': 'AUTHOR',
        '700': 'AUTHOR',
        '600': 'AUTHOR',
        '110': 'CORPORATE',
        '710': 'CORPORATE',
        '610': 'CORPORATE',
        '111': 'MEETING',
        '711': 'MEETING',
        '611': 'MEETING',
        '130': 'UNIFORM',
        '630': 'UNIFORM',
        '730': 'UNIFORM',
        '150': 'SUBJECT',
        '650': 'SUBJECT',
        '151': 'GEOGRAPHICAL',
        '751': 'GEOGRAPHICAL',
        '651': 'GEOGRAPHICAL',
        '155': 'GENRE',
        '655': 'GENRE',
    }

# CFG_BIBAUTHORITY_CONTROLLED_FIELDS_BIBLIOGRAPHIC
# 1. tells us which bibliographic subfields are under authority control
# 2. tells us which bibliographic subfields refer to which type of
# ... authority record (must conform to the keys of CFG_BIBAUTHORITY_TYPE_NAMES)
# Note: if you want to add new tag here you should also append appropriate tag
# to the miscellaneous index on the BibIndex Admin Site
try:
    from invenio.config import CFG_BIBAUTHORITY_CONTROLLED_FIELDS_BIBLIOGRAPHIC
except ImportError:
    CFG_BIBAUTHORITY_CONTROLLED_FIELDS_BIBLIOGRAPHIC = {
        '100__a': 'AUTHOR',
        '110__a': 'CORPORATE',
        '111__a': 'MEETING',
        '130__a': 'UNIFORM',
        '150__a': 'SUBJECT',
        '151__a': 'GEOGRAPHICAL',
        '700__a': 'AUTHOR',
        '600__a': 'AUTHOR',
        '710__a': 'CORPORATE',
        '610__a': 'CORPORATE',
        '711__a': 'MEETING',
        '611__a': 'MEETING',
        '730__a': 'UNIFORM',
        '650__a': 'SUBJECT',
        '751__a': 'GEOGRAPHICAL',
        '651__a': 'GEOGRAPHICAL',
        '155__a': 'GENRE',
        '655__a': 'GENRE'
    }

# CFG_BIBAUTHORITY_AUTOSUGGEST_CONFIG
# some additional configuration for auto-suggest drop-down
# 'field' : which logical or MARC field field to use for this
# ... auto-suggest type
# 'insert_here_field' : which authority record field to use
# ... for insertion into the auto-completed bibedit field
# 'disambiguation_fields': an ordered list of fields to use
# ... in case multiple suggestions have the same 'insert_here_field' values
# TODO: 'sort_by'. This has not been implemented yet !
try:
    from invenio.config import CFG_BIBAUTHORITY_AUTOSUGGEST_CONFIG
except ImportError:
    CFG_BIBAUTHORITY_AUTOSUGGEST_CONFIG = {
        'AUTHOR': {
            'field': 'authorityauthor',
            'insert_here_field': '100__a',
            'sort_by': CFG_BIBAUTHORITY_AUTOSUGGEST_SORT_POPULAR,
            'disambiguation_fields': ['100__d', '270__m'],
        },
        'CORPORATE': {
            'field': 'authoritycorporate',
            'insert_here_field': '110__a',
            'sort_by': CFG_BIBAUTHORITY_AUTOSUGGEST_SORT_ALPHA,
        },
        'MEETING': {
            'field': 'authoritymeeting',
            'insert_here_field': '111__a',
            'sort_by': CFG_BIBAUTHORITY_AUTOSUGGEST_SORT_POPULAR,
        },
        'UNIFORM': {
            'field': 'authorityuniform',
            'insert_here_field': '130__a',
            'sort_by': CFG_BIBAUTHORITY_AUTOSUGGEST_SORT_ALPHA,
        },
        'SUBJECT': {
            'field': 'authoritysubject',
            'insert_here_field': '150__a',
            'sort_by': CFG_BIBAUTHORITY_AUTOSUGGEST_SORT_ALPHA,
        },
        'GEOGRAPHICAL': {
            'field': 'authoritygeopgrahical',
            'insert_here_field': '151__a',
            'sort_by': CFG_BIBAUTHORITY_AUTOSUGGEST_SORT_ALPHA,
        },
        'GENRE': {
            'field': 'authoritygeopgrahical',
            'insert_here_field': '155__a',
            'sort_by': CFG_BIBAUTHORITY_AUTOSUGGEST_SORT_ALPHA,
        },
    }

# list of authority record fields to index for each authority record type
# R stands for 'repeatable'
# NR stands for 'non-repeatable'
try:
    from invenio.config import CFG_BIBAUTHORITY_AUTHORITY_SUBFIELDS_TO_INDEX
except ImportError:
    CFG_BIBAUTHORITY_AUTHORITY_SUBFIELDS_TO_INDEX = {
        'AUTHOR': [
            '100__a',  # Personal Name (NR, NR)
            '100__d',  # Year of birth or other dates (NR, NR)
            '100__q',  # Fuller form of name (NR, NR)
            '400__a',  # (See From Tracing) (R, NR)
            '400__d',  # (See From Tracing) (R, NR)
            '400__q',  #(See From Tracing) (R, NR)
        ],
        'CORPORATE': [
            '110__a',  # (NR, NR)
            '410__a',  # (R, NR)
        ],
        'MEETING': [
            '111__a',  # (NR, NR)
            '111__f',  # (NR, NR)
            '111__l',  # (NR, NR)
            '411__a',  # (R, NR)
        ],
        'UNIFORM': [
            '130__a',  # (NR, NR)
            '430__a',  # (R, NR)
        ],
        'SUBJECT': [
            '150__a',  # (NR, NR)
            '450__a',  # (R, NR)
        ],
        'GEOGRAPHICAL': [
            '151__a',  # (NR, NR)
            '451__a',  # (R, NR)
        ],
        'GENRE': [
            '155__a',
            '455__a',
        ]
    }

try:
    from invenio.config import CFG_AUTHORITY_COPY_NATIVE_FIELD
except ImportError:
    CFG_AUTHORITY_COPY_NATIVE_FIELD = True

try:
    from invenio.config import CFG_ARBITRARY_AUTOSUGGEST_FIELD
except ImportError:
    CFG_ARBITRARY_AUTOSUGGEST_FIELD = {
        "962__t": {"main": {"245": "t"},
                   "sub": [{"001": "w"}],
                   "name": "Cross Reserves"}
    }

##################
#  NOT USED BY TIND
# NOT USED BY TIND
# NOT USED BY TIND
##################



# CFG_BIBAUTHORITY_RECORD_CONTROL_NUMBER_FIELD
# the authority record field containing the authority record control number
try:
    from invenio.config import CFG_BIBAUTHORITY_RECORD_CONTROL_NUMBER_FIELD
except ImportError:
    CFG_BIBAUTHORITY_RECORD_CONTROL_NUMBER_FIELD = '035__a'



# Config variable to define if yes or no should the autocomplete check for authority record.
try:
    from invenio.config import CFG_AUTHORITY_AUTOCOMPLETE
except ImportError:
    CFG_AUTHORITY_AUTOCOMPLETE = True

# Separator to be used in control numbers to separate the authority type
# PREFIX (e.g. "INSTITUTE") from the control_no (e.g. "(CERN)abc123"
try:
    from invenio.config import CFG_BIBAUTHORITY_PREFIX_SEP
except ImportError:
    CFG_BIBAUTHORITY_PREFIX_SEP = '|'

# the ('980__a') string that identifies an authority record
try:
    from invenio.config import CFG_BIBAUTHORITY_AUTHORITY_COLLECTION_IDENTIFIER
except ImportError:
    CFG_BIBAUTHORITY_AUTHORITY_COLLECTION_IDENTIFIER = 'AUTHORITY'

# the name of the authority collection.
# This is needed for searching within the authority record collection.
try:
    from invenio.config import CFG_BIBAUTHORITY_AUTHORITY_COLLECTION_NAME
except ImportError:
    CFG_BIBAUTHORITY_AUTHORITY_COLLECTION_NAME = 'Authorities'

# CFG_BIBAUTHORITY_TYPE_NAMES
# Some administrators may want to be able to change the names used for the
# authority types. Although the keys of this dictionary are hard-coded into
# Invenio, the values are not and can therefore be changed to match whatever
# values are to be used in the MARC records.
# WARNING: These values shouldn't be changed on a running INVENIO installation
# ... since the same values are hard coded into the MARC data,
# ... including the 980__a subfields of all authority records
# ... and the $0 subfields of the bibliographic fields under authority control
try:
    from invenio.config import CFG_BIBAUTHORITY_TYPE_NAMES
except ImportError:
    CFG_BIBAUTHORITY_TYPE_NAMES = {
        'AUTHOR': 'AUTHOR',
        'CORPORATE': 'CORPORATE',
        'MEETING': 'MEETING',
        'UNIFORM': 'UNIFORM',
        'SUBJECT': 'SUBJECT',
        'GEOGRAPHICAL': 'GEOGRAPHICAL'
    }

# CFG_BIBAUTHORITY_CONTROLLED_FIELDS_AUTHORITY
# Tells us which authority record subfields are under authority control
# used by autosuggest feature in BibEdit
# authority record subfields use the $4 field for the control_no (not $0)
try:
    from invenio.config import CFG_BIBAUTHORITY_CONTROLLED_FIELDS_AUTHORITY
except ImportError:
    CFG_BIBAUTHORITY_CONTROLLED_FIELDS_AUTHORITY = {
        '500__a': 'AUTHOR',
        '510__a': 'CORPORATE',
        '511__a': 'MEETING',
        '530__a': 'UNIFORM',
        '550__a': 'SUBJECT',
        '551__a': 'GEOGRAPHICAL',
        '909C1u': 'INSTITUTE',  # used in bfe_affiliation
        '920__v': 'INSTITUTE',  # used by FZ Juelich demo data
    }

