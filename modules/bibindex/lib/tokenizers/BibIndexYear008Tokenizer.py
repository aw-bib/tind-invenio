# -*- coding:utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2010, 2011, 2012 CERN.
##
## Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
"""BibIndexYearLeaderTokenizer: extracts words form a given document.
   Document is given by its URL.
"""

from invenio.intbitset import intbitset
from invenio.bibindex_tokenizers import BibIndexFulltextTokenizer
from invenio.bibindex_tokenizers.BibIndexDefaultTokenizer import BibIndexDefaultTokenizer


fulltext_added = intbitset() # stores ids of records whose fulltexts have been added




class BibIndexYear008Tokenizer(BibIndexDefaultTokenizer):
    """
        Exctracts all the words contained in document specified by url.
    """

    def __init__(self, stemming_language = None, remove_stopwords = False, remove_html_markup = False, remove_latex_markup = False):
        self.verbose = 3
        BibIndexDefaultTokenizer.__init__(self, stemming_language,
                                                remove_stopwords,
                                                remove_html_markup,
                                                remove_latex_markup)

    def set_verbose(self, verbose):
        """Allows to change verbosity level during indexing"""
        self.verbose = verbose

    def tokenize_for_words_default(self, phrase):
        """Default tokenize_for_words inherited from default tokenizer"""
        return super(BibIndexFulltextTokenizer, self).tokenize_for_words(phrase)


    def tokenize_for_words(self, phrase):
        result = phrase[7:11]
        if isinstance(result,list):
            result = ''.join(result)
        return [result]

    def tokenize_for_pairs(self, phrase):
        result = phrase[7:11]
        if isinstance(result,list):
            result = ''.join(result)
        return [result]

    def tokenize_for_phrases(self, phrase):
        result = phrase[7:11]
        if isinstance(result,list):
            result = ''.join(result)
        return [result]

