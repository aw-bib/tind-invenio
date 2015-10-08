# -*- coding:utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2010, 2011, 2012 CERN.
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
"""BibIndexItemCountTokenizer: counts the number of copies of a book which is
   owned by the library in the real world.
"""

from invenio.bibindex_tokenizers.BibIndexRecJsonTokenizer import BibIndexRecJsonTokenizer
from invenio.dbquery import run_sql


class BibIndexRenewalsLastTwoYearsTindTokenizer(BibIndexRecJsonTokenizer):
    """
        Returns a number of copies of a book which is owned by the library.
    """

    def __init__(self, stemming_language=None, remove_stopwords=False, remove_html_markup=False,
                 remove_latex_markup=False):
        pass


    def tokenize(self, recid):
        """Tokenizes for number of copies of a book in the 'real' library"""
        try:
            return [run_sql(
                "SELECT SUM(number_of_renewals) "
                "FROM crcLOAN "
                "WHERE loaned_on > DATE_SUB(NOW(),INTERVAL 2 YEAR) "
                "AND  id_bibrec={0}".format(recid))[0][0]]
        except (KeyError, TypeError):
            return []

    def tokenize_for_words(self, recid):
        return self.tokenize(recid)

    def tokenize_for_pairs(self, recid):
        return self.tokenize(recid)

    def tokenize_for_phrases(self, recid):
        return self.tokenize(recid)

    def get_tokenizing_function(self, wordtable_type):
        return self.tokenize
