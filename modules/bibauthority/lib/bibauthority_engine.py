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

# pylint: disable=C0103
"""Invenio BibAuthority Engine."""
import re

from invenio.bibauthority_config import \
    CFG_BIBAUTHORITY_RECORD_CONTROL_NUMBER_FIELD, \
    CFG_BIBAUTHORITY_AUTHORITY_SUBFIELDS_TO_INDEX, \
    CFG_BIBAUTHORITY_PREFIX_SEP, \
    CFG_BIBAUTHORITY_AUTHORITY_COLLECTION_IDENTIFIER, \
    CFG_BIBAUTHORITY_AUTOSUGGEST_CONFIG, \
    CFG_BIBAUTHORITY_RECORD_AUTHOR_CONTROL_NUMBER_FIELDS, \
    CFG_BIBAUTHORITY_RECORD_AUTHOR_CONTROL_NUMBER_FIELDS_REVERSED, \
    CFG_AUTHORITY_COPY_NATIVE_FIELD, \
    CFG_ARBITRARY_AUTOSUGGEST_FIELD

from invenio.errorlib import register_exception
from invenio.search_engine import search_pattern, \
    record_exists
from invenio.search_engine_utils import get_fieldvalues
from invenio.docextract_record import get_record
from invenio.dbquery import run_sql


def is_authority_record(recID):
    """
    returns whether recID is an authority record

    :param recID: the record id to check
    :type recID: int

    :return: True or False
    """
    # low-level: don't use possibly indexed logical fields !
    return recID in search_pattern(p='980__a:AUTHORITY')


def get_all_record_for_field(field, value):
    """
    Return all the authority record for a specific field.

    This function will look in the configuration to see if it can create
    a link between the field and the authority category.
    If yes then it will do a database request to retrieve all the authority record matching
    with it
    .
    :param field: Field tag for searching.
    :return: List of records from bibextract
    """

    sql_request = 'select bibrec_bib{0}x.id_bibrec from bibrec_bib{0}x, bib{0}x where bib{0}x.tag like "{2}%" and bib{0}x.value like "%{1}%" and bibrec_bib{0}x.id_bibxxx = bib{0}x.id'.format(
        field[:2], value, field)
    authority_records_matching = run_sql(sql_request)
    authority_records_matching = authority_records_matching[:20]
    authority_records = []
    for authority_record in authority_records_matching:
        authority_records.append(get_record(authority_record[0]).record)
    return authority_records

def get_all_authority_record_for_field(field, value):
    """
    Return all the authority record for a specific field.

    This function will look in the configuration to see if it can create
    a link between the field and the authority category.
    If yes then it will do a database request to retrieve all the authority record matching
    with it
    .
    :param field: Field tag for searching.
    :return: List of records from bibextract
    """
    if field in CFG_BIBAUTHORITY_RECORD_AUTHOR_CONTROL_NUMBER_FIELDS_REVERSED:
        authority_type = CFG_BIBAUTHORITY_RECORD_AUTHOR_CONTROL_NUMBER_FIELDS_REVERSED[field]
        list_index_fields = CFG_BIBAUTHORITY_AUTHORITY_SUBFIELDS_TO_INDEX[
            CFG_BIBAUTHORITY_RECORD_AUTHOR_CONTROL_NUMBER_FIELDS_REVERSED[field]]

        list_request = []

        for field in list_index_fields:
            first_two_char = field[:2]
            list_request.append(
                'select bibrec_bib{0}x.id_bibrec from bibrec_bib{0}x, bib{0}x '
                'where bib{0}x.tag="{2}" and bib{0}x.value like "%{1}%" '
                'and bibrec_bib{0}x.id_bibxxx = bib{0}x.id'.format(first_two_char, value, field))

        sql_request = " UNION ".join(list_request)
        authority_records_matching = run_sql(sql_request)
        authority_records_matching = authority_records_matching[:20]
        authority_records = []
        for authority_record in authority_records_matching:
            authority_records.append(get_record(authority_record[0]).record)
        return authority_records
    else:
        return []


def process_authority_autosuggest(value, field):
    """
    This function will return the list of authority that are
    matching value in field.

    :param value: the value that we are looking for
    :param field: the field in which we are looking for
    :return: None or a list of authority information
    """
    final_result = {"name": "Authority", "suggestions": []}
    if field[:3] in CFG_BIBAUTHORITY_RECORD_AUTHOR_CONTROL_NUMBER_FIELDS_REVERSED:
        field = field[:3]
        res = find_records(value, field)
        res_sorted = res.keys()
        for res_to_process in res_sorted:
            record = res[res_to_process]["record"]
            final_result["suggestions"].append(format_record_for_bibedit(record, field))
        return final_result
    elif field in CFG_ARBITRARY_AUTOSUGGEST_FIELD:
        final_result["name"] = CFG_ARBITRARY_AUTOSUGGEST_FIELD[field]["name"]
        res = find_records_global(value, CFG_ARBITRARY_AUTOSUGGEST_FIELD[field]["main"].keys()[0])
        res_sorted = res.keys()
        for res_to_process in res_sorted:
            record = res[res_to_process]["record"]
            final_result["suggestions"].append(format_record_for_bibedit_global(record, field))
        return final_result
    else:
        return None


def find_records(value, field):
    records = get_all_authority_record_for_field(field, value)
    result = {}
    for record in records:
        result[record.get("001")[0].value] = {"record": record}
    return result

def find_records_global(value, field):
    records = get_all_record_for_field(field, value)
    result = {}
    for record in records:
        result[record.get("001")[0].value] = {"record": record}
    return result


def format_record_for_bibedit_global(record, field):
    """
    Process the record to be manipulated by bibedit

    :param record: The record you want to manipulate.
    :param field: The field which is interesting you.
    :return: Dict with the values needed by bibedit to work.
    """
    final_shape = {}
    final_shape["fields"] = {}
    try:
        fields = CFG_ARBITRARY_AUTOSUGGEST_FIELD[field]
        final_shape["print"] = record_get_field(record, fields["main"].keys()[0])[0]
        final_shape["fields"][field[:3]] = {}
        final_shape["fields"][field[:3]][fields["main"][fields["main"].keys()[0]]] = [record_get_field(record, fields["main"].keys()[0])[0]]

        for field_to_add in fields["sub"]:
            final_shape["fields"][field[:3]][field_to_add.values()[0]] = [record_get_field(record, field_to_add.keys()[0])[0]]

    except:
        register_exception()
        final_shape["print"] = ""

    return final_shape


def format_record_for_bibedit(record, field):
    """
    Process the record to be manipulated by bibedit

    :param record: The record you want to manipulate.
    :param field: The field which is interesting you.
    :return: Dict with the values needed by bibedit to work.
    """
    final_shape = {}
    field_list = ["035"]

    if CFG_AUTHORITY_COPY_NATIVE_FIELD:
        field_list.append(CFG_BIBAUTHORITY_RECORD_AUTHOR_CONTROL_NUMBER_FIELDS[
            CFG_BIBAUTHORITY_RECORD_AUTHOR_CONTROL_NUMBER_FIELDS_REVERSED[field]][0])

    if "disambiguation_fields" in CFG_BIBAUTHORITY_AUTOSUGGEST_CONFIG[
        CFG_BIBAUTHORITY_RECORD_AUTHOR_CONTROL_NUMBER_FIELDS_REVERSED[field]]:
        disambiguation_fields = CFG_BIBAUTHORITY_AUTOSUGGEST_CONFIG[
            CFG_BIBAUTHORITY_RECORD_AUTHOR_CONTROL_NUMBER_FIELDS_REVERSED[field]][
            "disambiguation_fields"]
        try:
            label = record_get_field(record, CFG_BIBAUTHORITY_RECORD_AUTHOR_CONTROL_NUMBER_FIELDS[
                CFG_BIBAUTHORITY_RECORD_AUTHOR_CONTROL_NUMBER_FIELDS_REVERSED[field]][0])[0]
        except:
            label = ""

        for field_d in disambiguation_fields:
            label += " ; {0}".format(', '.join(record_get_field(record, field_d)))
        final_shape["print"] = label

        final_shape["fields"] = convert_record_to_dict(record, field_list, field)

    else:
        try:
            final_shape["print"] = record_get_field(record,
                                                    CFG_BIBAUTHORITY_RECORD_AUTHOR_CONTROL_NUMBER_FIELDS[
                                                        CFG_BIBAUTHORITY_RECORD_AUTHOR_CONTROL_NUMBER_FIELDS_REVERSED[
                                                            field]][0])[0]
        except:
            final_shape["print"] = ""
        final_shape["fields"] = convert_record_to_dict(record, field_list, field)
    return final_shape


def convert_record_to_dict(record, field_list, field_f):
    final = {}
    for key in record:
        if key[:2] == "00" or key not in field_list:
            continue

        if key == CFG_BIBAUTHORITY_RECORD_AUTHOR_CONTROL_NUMBER_FIELDS[
            CFG_BIBAUTHORITY_RECORD_AUTHOR_CONTROL_NUMBER_FIELDS_REVERSED[field_f]][0]:
            final_key = field_f
        else:
            final_key = key

        final[final_key] = {}
        for field in record[key]:
            for subfield in field.subfields:
                if final_key == "035" and subfield.code != "a":
                    pass
                if subfield.code not in final[final_key]:
                    final[final_key][subfield.code] = [subfield.value]
                else:
                    final[final_key][subfield.code].append(subfield.value)
    return final


def record_get_field(record, field):
    values = []
    fa = field[:3]
    ind1 = None
    ind2 = None
    fb = None
    try:
        ind1 = field[3]
        ind2 = field[4]
        fb = field[5]
    except:
        pass
    if ind1 == "_":
        ind1 = " "
    if ind2 == "_":
        ind2 = " "
    fields = record.get(fa)
    if fields:
        for field in fields:
            if fa[:2] != "00":
                try:
                    if (ind1 and ind2 and ind1 == field.ind1 and ind2 == field.ind2) or (not ind1 and not ind2):
                        if fb:
                            values.append(field.find_subfields(fb)[0].value)
                        else:
                            values.append(" ".join(x.value for x in field.subfields))
                except:
                    register_exception()
            else:
                values.append(field.value)
    return values


def get_field_values_authority_record(field):
    list_of_field = []
    list_index_fields = CFG_BIBAUTHORITY_AUTHORITY_SUBFIELDS_TO_INDEX[
        CFG_BIBAUTHORITY_RECORD_AUTHOR_CONTROL_NUMBER_FIELDS_REVERSED[field]]
    for field in list_index_fields:
        field_corrected = field[:5].strip("_")
        if field_corrected not in list_of_field:
            list_of_field.append(field_corrected)
    return list_of_field


def generate_all_variants(record, field):
    list_field_to_get = get_field_values_authority_record(field)
    list_key_word = []
    for field in list_field_to_get:
        list_values = record.get(field)
        if not list_values:
            continue
        for value in list_values:
            values = value.find_subfields("a")[0].value
            values = values.split(",")
            for val in values:
                if val not in list_key_word:
                    list_key_word.append(val)

    return list_key_word


def get_dependent_records_for_control_no(control_no):
    """
    returns a list of recIDs that refer to an authority record containing
    the given control_no.
    E.g. if an authority record has the control number
    "AUTHOR:(CERN)aaa0005" in its '035__a' subfield, then this function will return all
    recIDs of records that contain any 'XXX__0' subfield
    containing "AUTHOR:(CERN)aaa0005"

    :param control_no: the control number for an authority record
    :type control_no: string

    :return: list of recIDs
    """
    # We don't want to return the recID who's control number is control_no
    myRecIDs = _get_low_level_recIDs_intbitset_from_control_no(control_no)
    # Use search_pattern, since we want to find records from both bibliographic
    # as well as authority record collections
    return list(search_pattern(p='"' + control_no + '"') - myRecIDs)


def get_dependent_records_for_recID(recID):
    """
    returns a list of recIDs that refer to an authority record containing
    the given record ID.

    'type' is a string (e.g. "AUTHOR") referring to the type of authority record

    :param recID: the record ID for the authority record
    :type recID: int

    :return: list of recIDs
    """
    recIDs = []

    # get the control numbers
    control_nos = get_control_nos_from_recID(recID)
    for control_no in control_nos:
        recIDs.extend(get_dependent_records_for_control_no(control_no))

    return recIDs


def guess_authority_types(recID):
    """
    guesses the type(s) (e.g. AUTHOR, INSTITUTE, etc.)
    of an authority record (should only have one value)

    :param recID: the record ID of the authority record
    :type recID: int

    :return: list of strings
    """
    types = get_fieldvalues(recID,
                            '980__a',
                            repetitive_values=False)  # remove possible duplicates !

    # filter out unwanted information
    while CFG_BIBAUTHORITY_AUTHORITY_COLLECTION_IDENTIFIER in types:
        types.remove(CFG_BIBAUTHORITY_AUTHORITY_COLLECTION_IDENTIFIER)
    types = [_type for _type in types if _type.isalpha()]

    return types


def get_low_level_recIDs_from_control_no(control_no):
    """
    returns the list of EXISTING record ID(s) of the authority records
    corresponding to the given (INVENIO) MARC control_no
    (e.g. 'AUTHOR:(XYZ)abc123')
    (NB: the list should normally contain exactly 1 element)

    :param control_no: a (INVENIO) MARC internal control_no to an authority record
    :type control_no: string

    :return:: list containing the record ID(s) of the referenced authority record
        (should be only one)
    """
    # values returned
    # recIDs = []
    #check for correct format for control_no
    #    control_no = ""
    #    if CFG_BIBAUTHORITY_PREFIX_SEP in control_no:
    #        auth_prefix, control_no = control_no.split(CFG_BIBAUTHORITY_PREFIX_SEP);
    #        #enforce expected enforced_type if present
    #        if (enforced_type is None) or (auth_prefix == enforced_type):
    #            #low-level search needed e.g. for bibindex
    #            hitlist = search_pattern(p='980__a:' + auth_prefix)
    #            hitlist &= _get_low_level_recIDs_intbitset_from_control_no(control_no)
    #            recIDs = list(hitlist)

    recIDs = list(_get_low_level_recIDs_intbitset_from_control_no(control_no))

    # filter out "DELETED" recIDs
    recIDs = [recID for recID in recIDs if record_exists(recID) > 0]

    # normally there should be exactly 1 authority record per control_number
    _assert_unique_control_no(recIDs, control_no)

    # return
    return recIDs


# def get_low_level_recIDs_from_control_no(control_no):
#    """
#    Wrapper function for _get_low_level_recIDs_intbitset_from_control_no()
#    Returns a list of EXISTING record IDs with control_no
#
#    :param control_no: an (INVENIO) MARC internal control number to an authority record
#    :type control_no: string
#
#    :return: list (in stead of an intbitset)
#    """
#    #low-level search needed e.g. for bibindex
#    recIDs = list(_get_low_level_recIDs_intbitset_from_control_no(control_no))
#
#    # filter out "DELETED" recIDs
#    recIDs = [recID for recID in recIDs if record_exists(recID) > 0]
#
#    # normally there should be exactly 1 authority record per control_number
#    _assert_unique_control_no(recIDs, control_no)
#
#    # return
#    return recIDs

def _get_low_level_recIDs_intbitset_from_control_no(control_no):
    """
    returns the intbitset hitlist of ALL record ID(s) of the authority records
    corresponding to the given (INVENIO) MARC control number
    (e.g. '(XYZ)abc123'), (e.g. from the 035 field) of the authority record.

    Note: This function does not filter out DELETED records!!! The caller
    to this function must do this himself.

    :param control_no: an (INVENIO) MARC internal control number to an authority record
    :type control_no: string

    :return:: intbitset containing the record ID(s) of the referenced authority record
        (should be only one)
    """
    #low-level search needed e.g. for bibindex
    hitlist = search_pattern(
        p=CFG_BIBAUTHORITY_RECORD_CONTROL_NUMBER_FIELD + ":" +
          '"' + control_no + '"')

    # return
    return hitlist


def _assert_unique_control_no(recIDs, control_no):
    """
    If there are more than one EXISTING recIDs with control_no, log a warning

    :param recIDs: list of record IDs with control_no
    :type recIDs: list of int

    :param control_no: the control number of the authority record in question
    :type control_no: string
    """

    if len(recIDs) > 1:
        error_message = \
            "DB inconsistency: multiple rec_ids " + \
            "(" + ", ".join([str(recID) for recID in recIDs]) + ") " + \
            "found for authority record control number: " + control_no
        try:
            raise Exception
        except:
            register_exception(prefix=error_message,
                               alert_admin=True,
                               subject=error_message)


def get_control_nos_from_recID(recID):
    """
    get a list of control numbers from the record ID

    :param recID: record ID
    :type recID: int

    :return: authority record control number
    """
    return get_fieldvalues(recID, CFG_BIBAUTHORITY_RECORD_CONTROL_NUMBER_FIELD,
                           repetitive_values=False)


def get_type_from_control_no(control_no):
    """simply returns the authority record TYPE prefix contained in
    control_no or else an empty string.

    :param control_no: e.g. "AUTHOR:(CERN)abc123"
    :type control_no: string

    :return: e.g. "AUTHOR" or ""
    """

    # pattern: any string, followed by the prefix, followed by a parenthesis
    pattern = \
        r'.*' + \
        r'(?=' + re.escape(CFG_BIBAUTHORITY_PREFIX_SEP) + re.escape('(') + r')'
    m = re.match(pattern, control_no)
    return m and m.group(0) or ''


def guess_main_name_from_authority_recID(recID):
    """
    get the main name of the authority record

    :param recID: the record ID of authority record
    :type recID: int

    :return: the main name of this authority record (string)
    """
    #tags where the main authority record name can be found
    main_name_tags = ['100__a', '110__a', '130__a', '150__a']
    main_name = ''
    # look for first match only
    for tag in main_name_tags:
        fieldvalues = get_fieldvalues(recID, tag, repetitive_values=False)
        if len(fieldvalues):
            main_name = fieldvalues[0]
            break
    # return first match, if found
    return main_name


def get_index_strings_by_control_no(control_no):
    """extracts the index-relevant strings from the authority record referenced by
    the 'control_no' parameter and returns it as a list of strings

    :param control_no: a (INVENIO) MARC internal control_no to an authority record
    :type control_no: string (e.g. 'author:(ABC)1234')

    :param expected_type: the type of authority record expected
    :type expected_type: string, e.g. 'author', 'journal' etc.

    :return: list of index-relevant strings from the referenced authority record

    """

    from invenio.bibindex_engine import list_union

    #return value
    string_list = []
    #1. get recID and authority type corresponding to control_no
    rec_IDs = get_low_level_recIDs_from_control_no(control_no)
    #2. concatenate and return all the info from the interesting fields for this record
    for rec_id in rec_IDs:  # in case we get multiple authority records
        for tag in CFG_BIBAUTHORITY_AUTHORITY_SUBFIELDS_TO_INDEX.get(
                get_type_from_control_no(control_no)):
            new_strings = get_fieldvalues(rec_id, tag)
            string_list = list_union(new_strings, string_list)
    #return
    return string_list
