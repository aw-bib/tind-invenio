# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2008, 2009, 2010, 2011, 2013 CERN.
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

"""
bibcirculation config file
"""

__revision__ = "$Id$"

from invenio.config import CFG_CERN_SITE, \
                           CFG_SITE_URL

from invenio.config import \
    CFG_BIBCIRCULATION_ITEM_STATUS_OPTIONAL, \
    CFG_BIBCIRCULATION_ITEM_STATUS_ON_LOAN, \
    CFG_BIBCIRCULATION_ITEM_STATUS_ON_SHELF, \
    CFG_BIBCIRCULATION_ITEM_STATUS_CANCELLED, \
    CFG_BIBCIRCULATION_ITEM_STATUS_IN_PROCESS, \
    CFG_BIBCIRCULATION_ITEM_STATUS_UNDER_REVIEW, \
    CFG_BIBCIRCULATION_ITEM_STATUS_NOT_ARRIVED, \
    CFG_BIBCIRCULATION_ITEM_STATUS_ON_ORDER, \
    CFG_BIBCIRCULATION_ITEM_STATUS_CLAIMED, \
    CFG_BIBCIRCULATION_LOAN_STATUS_ON_LOAN, \
    CFG_BIBCIRCULATION_LOAN_STATUS_EXPIRED, \
    CFG_BIBCIRCULATION_LOAN_STATUS_RETURNED, \
    CFG_BIBCIRCULATION_REQUEST_STATUS_WAITING, \
    CFG_BIBCIRCULATION_REQUEST_STATUS_PENDING, \
    CFG_BIBCIRCULATION_REQUEST_STATUS_PROPOSED, \
    CFG_BIBCIRCULATION_REQUEST_STATUS_DONE, \
    CFG_BIBCIRCULATION_REQUEST_STATUS_CANCELLED, \
    CFG_BIBCIRCULATION_ILL_STATUS_NEW, \
    CFG_BIBCIRCULATION_ILL_STATUS_REQUESTED, \
    CFG_BIBCIRCULATION_ILL_STATUS_ON_LOAN, \
    CFG_BIBCIRCULATION_ILL_STATUS_RETURNED, \
    CFG_BIBCIRCULATION_ILL_STATUS_CANCELLED, \
    CFG_BIBCIRCULATION_ILL_STATUS_RECEIVED, \
    CFG_BIBCIRCULATION_LIBRARY_TYPE_INTERNAL, \
    CFG_BIBCIRCULATION_LIBRARY_TYPE_EXTERNAL, \
    CFG_BIBCIRCULATION_LIBRARY_TYPE_MAIN, \
    CFG_BIBCIRCULATION_LIBRARY_TYPE_HIDDEN, \
    CFG_BIBCIRCULATION_ACQ_STATUS_NEW, \
    CFG_BIBCIRCULATION_ACQ_STATUS_ON_ORDER, \
    CFG_BIBCIRCULATION_ACQ_STATUS_PARTIAL_RECEIPT, \
    CFG_BIBCIRCULATION_ACQ_STATUS_RECEIVED, \
    CFG_BIBCIRCULATION_ACQ_STATUS_CANCELLED, \
    CFG_BIBCIRCULATION_PROPOSAL_STATUS_NEW, \
    CFG_BIBCIRCULATION_PROPOSAL_STATUS_ON_ORDER, \
    CFG_BIBCIRCULATION_PROPOSAL_STATUS_PUT_ASIDE, \
    CFG_BIBCIRCULATION_PROPOSAL_STATUS_RECEIVED

# templates used to notify borrowers
if CFG_CERN_SITE == 1:
    CFG_BIBCIRCULATION_TEMPLATES = {
    'OVERDUE': 'Overdue letter template (write some text)',
    'REMINDER': 'Reminder letter template (write some text)',
    'NOTIFICATION': 'Hello,\n'\
                    'This is an automatic email for confirming the request for a book on behalf of:\n'\
                    '%s (ccid: %s, email: %s)\n'\
                    '%s (%s)\n\n'\
                    '\tTitle: %s\n'\
                    '\tAuthor: %s\n'\
                    '\tPublisher: %s\n'\
                    '\tYear: %s\n'\
                    '\tIsbn: %s\n\n'\
                    '\tLocation: %s\n'\
                    '\tLibrary: %s\n'\
                    '\t%s\n\n'\
                    '\tRequest date: %s\n\n'\
                    'The document will be sent to you via internal mail.\n\n'\
                    'Best regards\n',
    #user_name, ccid, user_email, address,department, mailbox, title,
    #author, publisher, year, isbn, location, library,
    #link_to_holdings_details, request_date

    'ILL_RECEIVED': 'Dear colleague,\n\n'\
                    'The document you requested has been received. '\
                    'Do you want to come to the Library desk to pick it up or do you prefer we send it to you by internal mail?\n\n'\
                    'Best regards,\nCERN Library team\n',

        'ILL_RECALL1':  'Dear Colleague,\n\n'\
                        'The loan period has now expired for the following document which has been borrowed for you '\
                        'from another Library.\n\n'\
                        'Please return it to the Library (either personally or by internal mail). Failure to do that could result in the library being fined. '\
                        'If you have already returned the document, please ignore this message.\n'\
                        'If you still need this title, please let us know by answering this email and we will check '\
                        'with the external library if the loan can be extended or if we can find another copy for you.\n\n'\
                        'Thank you for using our services,\n'\
                        'CERN Library Staff',

        'ILL_RECALL2':  'Dear Colleague,\n\n'\
                        'The return date for the following document which has been borrowed for you from another '\
                        'library is now well past.\n\n'\
                        'According to our records you have not responded to our first recall message, so we now ask '\
                        'you to return the document to the Library without delay (either personally or by internal '\
                        'mail). Failure to do that could result in the library being fined. '\
                        'If you have already returned the document, please ignore this message.\n'\
                        'If you still need this title, please let us know by answering this email and we will check '\
                        'with the external library if the loan can be extended or if we can find another copy for you.\n\n'\
                        'Thank you for using our services,\n'\
                        'CERN Library Staff',

        'ILL_RECALL3':  'Dear Colleague,\n\n'\
                        'We have already sent you two messages about the following document borrowed for you from '\
                        'another Library.\n\n'\
                        'According to our records, you have not responded to either of them. Please return the '\
                        'document to the  library without delay (either personally or by internal mail) or reply to '\
                        'this mail giving any comments.'\
                        'Failure to do that could result in the Library being fined. If you have already returned the document, please ignore this message.\n\n'\
                        'Thank you for using our services,\n'\
                        'Jens Vigen, Head of CERN Library',

    'PROPOSAL_NOTIFICATION': 'Dear colleague,\n\n'\
                    'We thank you for your suggestion for the Library collection: \n'\
                    '\tTitle: %s\n\n'\
                    'Our team will review your proposal and will get back to you soon to inform you of our decision.\n\n'\
                    'Best regards,\nCERN Library team\n',

    'PROPOSAL_ACCEPTANCE_NOTIFICATION': 'Dear colleague,\n\n'\
                    'Following your suggestion, our team has decided to acquire the book for the Library collection. '\
                    'As soon as we receive the book, we will send it on loan to you via internal mail. \n\n'\
                    'Best regards,\nCERN Library team\n',

    'PROPOSAL_REFUSAL_NOTIFICATION': 'Dear colleague,\n\n'\
                    'Concerning your suggestion, we regret to inform you that our team has decided not to acquire the book '\
                    'for the Library collection for the following reason(s): <Reason> \n\n'\
                    'However, if you need this document for your work, we will be able to get it on loan from another Library. '\
                    'Please let us know if this solution suits you.\n\n'\
                    'Best regards,\nCERN Library team\n',

    'PURCHASE_NOTIFICATION': 'Dear colleague,\n\n'\
                    'We have received your request.\n'\
                    '\tTitle: %s\n\n'\
                    'We will process your order of the document immediately and will contact you as soon as it is delivered.\n\n'\
                    'Best regards,\nCERN Library team\n',

    'PURCHASE_RECEIVED_TID': 'Dear colleague,\n\n'\
                    'The document you requested has been received. '\
                    'The price is %s'\
                    'A TID will be issued for the payment. \n\n'\
                    'Do you want to come to the Library desk to pick it up or do you prefer we send it to you by internal mail?\n\n'\
                    'Best regards,\nCERN Library team\n',

    'PURCHASE_RECEIVED_CASH': 'Dear colleague,\n\n'\
                    'The document you requested has been received. '\
                    'The price is %s\n\n'\
                    'Please come to the library desk to pay and pick up the document.\n\n'\
                    'Best regards,\nCERN Library team\n',

    'SEND_RECALL': 'Dear Colleague,\n\n'\
                       'The loan for the document(s)\n\n'\
                       'Item information:\n\n'\
                       '\t title: %s \n'\
                       '\t year: %s \n'\
                       '\t author(s): %s \n'\
                       '\t isbn: %s \n'\
                       '\t publisher: %s \n\n'\
                       'is overdue and another reader(s) is/are waiting for the document(s). '\
                       'Please return them to the Library as soon as possible.'\
                       '\n\nBest regards',
    'RECALL1': 'Dear Colleague,\n\n'\
               'The loan period has now expired for the following Library item which you '\
               ' borrowed. Please return it to the Library (either personally or by '\
               ' internal mail) or extend the loan at:\n\n'\
               '%s/yourloans/display \n\n' % CFG_SITE_URL +
               'If you have already done so, please ignore this message.\n\n'\
               'Item information:\n\n'\
               '%s \n'\
               '%s \n'\
               '%s \n'\
               '%s \n'\
               '%s \n\n'\
               'Thank you for using our services, Library Staff \n\n\n\n'\
               'If you are not able to update your loans via WWW or for any other '\
               'matter concerning circulation of library material, please simply '\
               'reply to this mail.',
    'RECALL2': 'Dear Colleague\n\n'\
               'The return date for the following Library item which you borrowed is now '\
               'well past. According to our records you have not responded to our first '\
               'recall message, so we now ask you to return the item to the Library '\
               'without delay (either personally or by internal mail) or extend the loan at:\n\n'\
               '%s/yourloans/display \n\n' % CFG_SITE_URL +
               'If you have already done so, please ignore this message. To send any comments, '\
               'reply to this mail.\n\n' \
               'Item information:\n\n'\
               '%s \n'\
               '%s \n'\
               '%s \n'\
               '%s \n'\
               '%s \n\n'\
               'Thank you in advance for your cooperation, CERN Library Staff',
    'RECALL3': 'Dear Colleague,\n\n'\
               'We have already sent you two messages about the following Library item, '\
               'which should have been returned a long time ago. According to our records, '\
               'you have not responded to either of them. Please return the item to the '\
               'Library without delay (either personally or by internal mail) or reply to '\
               'this mail giving any comments or extend the loan at:\n\n'\
               '%s/yourloans/display \n\n' % CFG_SITE_URL +
               'If you have already returned the item, please ignore this message.\n\n'\
               'Item information:\n\n'\
               '%s \n'\
               '%s \n'\
               '%s \n'\
               '%s \n'\
               '%s \n\n'\
               'Thank you in advance for your cooperation, CERN Library Staff',
    'EMPTY': 'Please choose one template'
    }

else:
    CFG_BIBCIRCULATION_TEMPLATES = {
        'OVERDUE': 'Dear colleague,\n'
                   'We would like to inform you that the following item '
                   'is now overdue :\n\n'

                   'Please return it to the Library as soon as possible. '
                   'If you would like to renew this title, please contact the '
                   'Library to do so.\n\n'

                   'Sincerely,',

        'REMINDER': 'Reminder letter template (write some text)\n\n\n'
                    'Dear colleague,\n'
                    'This is a gentle reminder that the following item at '
                    'your disposal is now overdue :\n\n'

                    'Please return it to the Library as soon as possible. '
                    'If you would like to renew this title, please contact '
                    'the Library to do so.\n\n'

                    'Sincerely,',
        'PICKUP': 'Dear patron,\n\n'
                  'The following item is now ready for pickup at %s:\n\n'
                  '\tTitle: %s\n'
                  '\tAuthor(s): %s\n'
                  '\tPublisher: %s\n'
                  '\tYear: %s\n'
                  '\tIsbn: %s\n\n'
                  'Please come to the library to check out your item.\n\n'
                  'Sincerely,\n'
                  'Sherman Fairchild Library\n'
                  'library@caltech.edu\n'
                  '626-395-3405\n',

        'NOTIFICATION': 'Hello,\n'
                        'This is an automatic email to confirm the request '
                        'for a book on behalf of:\n'
                        '%s (ccid: %s, email: %s)\n'
                        '%s (%s)\n\n'
                        '\tTitle: %s\n'
                        '\tAuthor: %s\n'
                        '\tPublisher: %s\n'
                        '\tYear: %s\n'
                        '\tIsbn: %s\n\n'
                        '\tLocation: %s\n'
                        '\tLibrary: %s\n'
                        '\t%s\n\n'
                        '\tRequest date: %s\n\n'
                        'You will be notified when this item is ready to be '
                        'picked up.\n\n'
                        'Sincerely,\n'
                        '%s\n'
                        '%s\n'
                        '%s\n',

        'ILL_RECEIVED': 'Dear colleague,\n\n'
                        'The interlibrary loan you requested has been '
                        'received and is ready to be picked up in the '
                        'Library.\n\n'
                        'Best regards,\nLibrary team\n',

        'ILL_RECALL1':  'Dear Colleague,\n\n'

                        'The following interlibrary loan is now overdue:\n\n'

                        'Please return it to the Library as soon as possible.'
                        'Failure to return it in a timely fashion could '
                        'result in the Library being fined.\n\n'

                        'If you have already returned the item, please '
                        'ignore this message.\n\n'

                        'If you still need this title, please let us know by '
                        'answering this email and we will check with the '
                        'external library if the loan can be extended or '
                        'if we can find another copy for you.\n\n'

                        'Thank you for using our services',

        'ILL_RECALL2':  'Dear Colleague,\n\n'

                        'This is a follow up message about the following '
                        'overdue item borrowed for you from another '
                        'library:\n\n'

                        'According to our records, you have not responded. '
                        'Please return the item to the Library without delay. '
                        'Failure to return it in a timely fashion could '
                        'result in the Library being fined.\n\n'

                        'If you have already returned the item, please '
                        'ignore this message.\n\n'

                        'If you still need this title, please let us know by '
                        'answering this email and we will check with the '
                        'external library if the loan can be extended or if '
                        'we can find another copy for you.\n\n'

                        'Thank you for using our services',

        'ILL_RECALL3':  'Dear Colleague,\n\n'

                        'We have already sent you two messages about the '
                        'following item borrowed for you from '
                        'another Library.\n\n'

                        'According to our records, you have not responded to '
                        'either of them. Please return the '
                        'item to the library without delay. '
                        'Failure to return it in a timely fashion could '
                        'result in the Library being fined. \n\n'

                        'If you have already returned the document, '
                        'please ignore this message.\n\n'

                        'Thank you for using our services,\n\n',

        'PURCHASE_NOTIFICATION': 'Hello,\n'
                                 'This is an automatic email confirming the '
                                 'request to purchase the following book on '
                                 'behalf of:\n'
                                 '\n'
                                 '\n'
                                 '\tTitle: %s\n\n'
                                 '\n'
                                 '\n'
                                 'Your request will be evaluated against '
                                 'our collection development policy and you '
                                 'will be notified if the Library decides '
                                 'to proceed with the purchase.\n\n'

                                 'Sincerely,\n'
                                 'The Library Team',


        'PURCHASE_RECEIVED': 'Dear colleague,\n\n'

                        'The book you requested has been received.\n'
                        'and is available to be picked up in the Library.'
                        '\n\n'

                        'Sincerely,\n'
                        'The Library Team',

        'PURCHASE_RECEIVED_TID': 'Dear colleague,\n\n'
                        'The document you requested has been received. '
                        'The price is %s\n\n'
                        'A TID will be issued for the payment. \n\n'
                        'Do you want to come to the Library desk to pick it '
                        'up or do you prefer we deliver it to your office?\n\n'
                        'Best regards,\nLibrary team\n',

        'PURCHASE_RECEIVED_CASH': 'Dear colleague,\n\n'
                        'The document you requested has been received. '
                        'The price is %s\n\n'
                        'Please come to the library desk to pay '
                        'and pick up the document.\n\n'
                        'Best regards,\nLibrary team\n',

        'PROPOSAL_NOTIFICATION': 'Dear colleague,\n\n'
                    'We thank you for your suggestion for the '
                    'library collection: \n'
                    '\tTitle: %s\n\n'
                    'Our team will review your proposal and will get back to '

                    'you soon to inform you of our decision.\n\n'
                    'Best regards,',

        'PROPOSAL_ACCEPTANCE_NOTIFICATION': 'Dear colleague,\n\n'
                                            'Following your suggestion, our '
                                            'team has decided to acquire the '
                                            'book for the Library collection. '
                                            'As soon as we receive the book, '
                                            'we will contact you. \n\n'
                                            'Best regards,\nLibrary team\n',

        'PROPOSAL_REFUSAL_NOTIFICATION': 'Dear colleague,\n\n'
                                         'Concerning your suggestion, we '
                                         'regret to inform you that our team '
                                         'has decided not to acquire the book '
                                         'for the Library collection for the '
                                         'following reason(s): <Reason> \n\n'
                                         'However, if you need this document '
                                         'for your work, we will be able to '
                                         'get it on loan from another '
                                         'library. '
                                         'Please let us know if this solution '
                                         'suits you.\n\n'
                                         'Best regards,',

        'SEND_RECALL': 'Dear colleague,\n'
                   'We would like to remind you that the following item at your disposal is overdue:\n'
                   ' \n'
                   '\t title: %s \n'\
                   '\t year: %s \n'\
                   '\t author(s): %s \n'\
                   '\t isbn: %s \n'\
                   '\t publisher: %s \n'\
                   '\t due date: %s \n\n'\
                   'Please return the book to the %s as soon as possible.\n'
                   'If you would like to renew it, please login to your account to do so (https://unov.tind.io/youraccount/login?ln=en) or contact the library.\n'
                   ' \n'
                   'Sincerely,\n'
                   '%s\n'
                   '%s\n'
                   '%s\n',

        'RECALL1': 'Dear Colleague,\n\n'\
                   'This is an automated notification. We would like to remind you that the '\
                   'following library item, which you borrowed, is now overdue. Please return it to the library '\
                   '(either personally or by internal mail) or extend the loan at:\n\n'\

                   '%s/yourloans/display \n\n' % CFG_SITE_URL +
                   'If you have already done so, please ignore this message.\n\n'\
                   'Item information:\n\n'\
                   '\t title: %s \n'\
                   '\t year: %s \n'\
                   '\t author(s): %s \n'\
                   '\t isbn: %s \n'\
                   '\t publisher: %s \n'\
                   '\t due date: %s\n\n'\

                   'Please return the book to the %s as soon as possible.\n\n'

                   'Thank you for using our services\n'\
                   '%s\n'\
                   '%s\n'\
                   '%s\n'\

                   'If you are not able to update your loans via WWW or for any other ' \
                   'matter concerning circulation of library material, please simply ' \
                   'reply to this mail.',

        'RECALL2': 'Dear Colleague,\n\n'\
                   'This is an automated notification. We would like to remind you that the '\
                   'following library item, which you borrowed, is now overdue. Please return it to the library '\
                   '(either personally or by internal mail) or extend the loan at:\n\n'\

                   '%s/yourloans/display \n\n' % CFG_SITE_URL +
                   'If you have already done so, please ignore this message.\n\n'\
                   'Item information:\n\n'\
                   '\t title: %s \n'\
                   '\t year: %s \n'\
                   '\t author(s): %s \n'\
                   '\t isbn: %s \n'\
                   '\t publisher: %s \n'\
                   '\t due date: %s\n\n'\

                   'Please return the book to the %s as soon as possible.\n\n'

                   'Thank you for using our services\n'\
                   '%s\n'\
                   '%s\n'\
                   '%s\n'\

                   'If you are not able to update your loans via WWW or for any other ' \
                   'matter concerning circulation of library material, please simply ' \
                   'reply to this mail.',

        'RECALL3': 'Dear Colleague,\n\n'
                   'This is an automated notification from the Library. '
                   'We have already sent you several messages about the '
                   'following Library item, which should have been returned '
                   'a long time ago. According to our records, you have not '
                   'responded to either of them. Please return the item to '
                   'the Library without delay or contact us to extend the '
                   'loan.\n\n'

                   'If you have already returned the item, please ignore '
                   'this message.\n\n'
                   'Item information:\n\n'
                   '\t title: %s \n'
                   '\t year: %s \n'
                   '\t author(s): %s \n'
                   '\t isbn: %s \n'
                   '\t publisher: %s \n'
                   '\t due date: %s\n'
                   '\t library: %s\n\n'

                   'Thank you in advance for your cooperation,\n'
                   '%s\n'
                   '%s\n'
                   '%s\n',
        'EMPTY': 'Please choose one template'
        }

if CFG_CERN_SITE == 1:
    CFG_BIBCIRCULATION_ILLS_EMAIL = 'CERN External loans<external.loans@cern.ch>'
    CFG_BIBCIRCULATION_LIBRARIAN_EMAIL = 'CERN Library Desk<library.desk@cern.ch>'
    CFG_BIBCIRCULATION_LOANS_EMAIL = 'CERN Lib loans<lib.loans@cern.ch>'
else:
    CFG_BIBCIRCULATION_ILLS_EMAIL = 'UNOV Library<library@unvienna.org>'
    CFG_BIBCIRCULATION_LIBRARIAN_EMAIL = 'UNOV Library<library@unvienna.org>'
    CFG_BIBCIRCULATION_LOANS_EMAIL = CFG_BIBCIRCULATION_LIBRARIAN_EMAIL

if CFG_CERN_SITE:
    CFG_BIBCIRCULATION_HOLIDAYS = ['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
                                   '2013-03-29', '2013-04-01', '2013-05-01', '2013-05-09',
                                   '2013-05-20', '2013-09-05', '2013-12-23', '2013-12-24',
                                   '2013-12-25', '2013-12-26', '2013-12-27', '2013-12-30',
                                   '2013-12-31', '2014-01-01', '2014-01-02', '2014-01-03']

else:
    CFG_BIBCIRCULATION_HOLIDAYS = []

CFG_BIBCIRCULATION_WORKING_DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

# You can edit this variable if you want to have customized statuses

# Custom/additional item statuses
CFG_BIBCIRCULATION_ITEM_STATUS_ON_HOLDSHELF = "On holdshelf"

CFG_BIBCIRCULATION_ITEM_STATUS = CFG_BIBCIRCULATION_ITEM_STATUS_OPTIONAL + \
                                 ["On holdshelf", "Limited circulation", "Lost",
                                  "Archival copy", "At bindery", "In Technical Services",
                                  "On order", "Ask at office", "At UMI",
                                  "Key is at SFL circ desk", "Missing", "Overdue",
                                  "Library use only", "To be replaced", "In repair",
                                  "See notes", "In transit", "Online", "To delete",
                                  CFG_BIBCIRCULATION_ITEM_STATUS_ON_SHELF,
                                  CFG_BIBCIRCULATION_ITEM_STATUS_ON_LOAN,
                                  CFG_BIBCIRCULATION_ITEM_STATUS_IN_PROCESS,
                                  #CFG_BIBCIRCULATION_ITEM_STATUS_UNDER_REVIEW,
                                  #CFG_BIBCIRCULATION_ITEM_STATUS_CANCELLED,
                                  #CFG_BIBCIRCULATION_ITEM_STATUS_NOT_ARRIVED,
                                  CFG_BIBCIRCULATION_ITEM_STATUS_ON_ORDER,
                                  CFG_BIBCIRCULATION_ITEM_STATUS_CLAIMED,
                                  'Withdrawn',]


CFG_BIBCIRCULATION_LOAN_STATUS = [CFG_BIBCIRCULATION_LOAN_STATUS_ON_LOAN,
                                  CFG_BIBCIRCULATION_LOAN_STATUS_EXPIRED,
                                  CFG_BIBCIRCULATION_LOAN_STATUS_RETURNED]

CFG_BIBCIRCULATION_REQUEST_STATUS = [CFG_BIBCIRCULATION_REQUEST_STATUS_WAITING,
                                     CFG_BIBCIRCULATION_REQUEST_STATUS_PENDING,
                                     CFG_BIBCIRCULATION_REQUEST_STATUS_DONE,
                                     CFG_BIBCIRCULATION_REQUEST_STATUS_PROPOSED,
                                     CFG_BIBCIRCULATION_REQUEST_STATUS_CANCELLED]

CFG_BIBCIRCULATION_ILL_STATUS = [CFG_BIBCIRCULATION_ILL_STATUS_NEW,
                                 CFG_BIBCIRCULATION_ILL_STATUS_REQUESTED,
                                 CFG_BIBCIRCULATION_ILL_STATUS_ON_LOAN,
                                 CFG_BIBCIRCULATION_ILL_STATUS_RETURNED,
                                 CFG_BIBCIRCULATION_ILL_STATUS_RECEIVED,
                                 CFG_BIBCIRCULATION_ILL_STATUS_CANCELLED]

CFG_BIBCIRCULATION_ITEM_LOAN_PERIOD = ['4 weeks', '1 week', 'Reference']

CFG_BIBCIRCULATION_ACQ_TYPE = ['acq-book', 'acq-standard']

CFG_BIBCIRCULATION_PROPOSAL_TYPE = ['proposal-book']

CFG_BIBCIRCULATION_COLLECTION = ["am", "Monograph", "Article", "Bibliographie",
                                 "Book", "Conference", "Directory",
                                 "Multimedia", "Occasional paper",
                                 "Pamphlets/Leaflets", "Periodical",
                                 "Picture book", "Plans of action", "Report",
                                 "Reference material",
                                 "Teaching materials, manuals", "Textbook"]

AMZ_ACQUISITION_IDENTIFIER_TAG = '595__a'

AMZ_BOOK_PUBLICATION_DATE_TAG = '269__c'

# The library whose id will be used by default at the time inserting a
# dummy/temporary item.
CFG_BIBCIRCULATION_DEFAULT_LIBRARY_ID = 6

CFG_BIBCIRCULATION_PROPOSAL_STATUS = [CFG_BIBCIRCULATION_PROPOSAL_STATUS_NEW,
                                      CFG_BIBCIRCULATION_PROPOSAL_STATUS_ON_ORDER,
                                      CFG_BIBCIRCULATION_PROPOSAL_STATUS_PUT_ASIDE,
                                      CFG_BIBCIRCULATION_PROPOSAL_STATUS_RECEIVED]

# move these 2 to local config file and delete from here
#CFG_BIBCIRCULATION_AMAZON_ACCESS_KEY = 1T6P3M3TDMW9HWJ212R2
#CFG_BIBCIRCULATION_ITEM_STATUS_OPTIONAL = missing, out of print, in binding, untraceable, order delayed, not published, claimed

CFG_BIBCIRCULATION_LIBRARY_TYPE = [CFG_BIBCIRCULATION_LIBRARY_TYPE_INTERNAL,
                                   CFG_BIBCIRCULATION_LIBRARY_TYPE_EXTERNAL,
                                   CFG_BIBCIRCULATION_LIBRARY_TYPE_MAIN,
                                   CFG_BIBCIRCULATION_LIBRARY_TYPE_HIDDEN]

CFG_BIBCIRCULATION_ACQ_STATUS = [CFG_BIBCIRCULATION_ACQ_STATUS_NEW,
                                 CFG_BIBCIRCULATION_ACQ_STATUS_ON_ORDER,
                                 CFG_BIBCIRCULATION_ACQ_STATUS_PARTIAL_RECEIPT,
                                 CFG_BIBCIRCULATION_ACQ_STATUS_RECEIVED,
                                 CFG_BIBCIRCULATION_ACQ_STATUS_CANCELLED]

CFG_BIBCIRCULATION_COLLECTION_SEARCH = ["Books"]

CFG_BIBCIRCULATION_LOAN_RULE_CODE_ABSOLUTE = 'Absolute day of year (1-365)'
CFG_BIBCIRCULATION_LOAN_RULE_CODE_REGULAR = 'Regular (days)'
CFG_BIBCIRCULATION_LOAN_RULE_CODE_HOURS_OVERNIGHT = 'Hours (rounding up)'
CFG_BIBCIRCULATION_LOAN_RULE_CODE_HOURS = 'Hours (rounding up, no overnight)'
CFG_BIBCIRCULATION_LOAN_RULE_CODE_HOURS_MINUTE_OVERNIGHT = 'Hours (exact)'
CFG_BIBCIRCULATION_LOAN_RULE_CODE_HOURS_MINUTE = 'Hours (exact, no overnight)'
CFG_BIBCIRCULATION_LOAN_RULE_CODE_NON_CIRC = 'Non circulating'

CFG_BIBCIRCULATION_LOAN_RULE_CODES = [CFG_BIBCIRCULATION_LOAN_RULE_CODE_REGULAR,
                                      CFG_BIBCIRCULATION_LOAN_RULE_CODE_ABSOLUTE,
                                      CFG_BIBCIRCULATION_LOAN_RULE_CODE_HOURS_OVERNIGHT,
                                      CFG_BIBCIRCULATION_LOAN_RULE_CODE_HOURS,
                                      CFG_BIBCIRCULATION_LOAN_RULE_CODE_HOURS_MINUTE_OVERNIGHT,
                                      CFG_BIBCIRCULATION_LOAN_RULE_CODE_HOURS_MINUTE,
                                      CFG_BIBCIRCULATION_LOAN_RULE_CODE_NON_CIRC]
