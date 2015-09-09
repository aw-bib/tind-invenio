/*
 * This file is part of Invenio.
 * Copyright (C) 2011, 2012 CERN.
 *
 * Invenio is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License as
 * published by the Free Software Foundation; either version 2 of the
 * License, or (at your option) any later version.
 *
 * Invenio is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with Invenio; if not, write to the Free Software Foundation, Inc.,
 * 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
 */


function showxml(identifier) {
    $("#dialog-message")[0].innerHTML =  "<pre>" + gAllMarcXml[identifier].replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;') + "</pre>"
    $("#dialog-message").dialog({
      width: window.innerWidth/2,
      height: window.innerHeight/1.5,
      modal: true,
    });
}

function enterKeyLookUp(e) {
    var key;
    if(window.event)
      key = window.event.keyCode;     // IE
    else
      key = e.keyCode || e.which;     // Firefox
    if (key == 13) {
        spinning();
        e.preventDefault()
        return false;
    }
    return true;
}

function spinning(e) {
    $("#middle_area > table").remove();
    $("#middle_area > .error").remove();
    $("#middle_area").append("<p class='spinning_wheel'><i class='fa fa fa-spinner fa-pulse fa-5x'></i></p><p class='bibz39_button_td'>Searching...</p>");
    setTimeout( function() { $("#main_form").submit() }, 1000);
}