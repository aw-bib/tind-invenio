var scrollPos = 0;

function changepage(type) {
            scrollPos =  $(window).scrollTop();
            var oTable = $('#table_all_loans').dataTable();
            var Table = $('#table_all_loans').DataTable();
            oTable.fnPageChange(type);
            pg_info = Table.page.info();
            $('.pagedisplay')[0].value = (pg_info.page + 1) + "/" + pg_info.pages
}

function changelength() {
        scrollPos =  $(window).scrollTop();
        var oTable = $('#table_all_loans').dataTable();
        oTable._fnLengthChange(parseInt($('.pagesize').val()));
        oTable.fnDraw();

}


$(document).ready(function(){
    var elems = Array.prototype.slice.call(document.querySelectorAll('.js-switch'));
    elems.forEach(function(html) {
      var switchery = new Switchery(html, { color:'#006FB7', size:'small' });
    });
    $('.checkboxes_exp_loan').wrap('<span style="text-align: left; margin-bottom: 5px; font-size: 14px;">');
    if ($("#table_all_loans").length > 0) {
        $("#table_all_loans").DataTable({
            "columns": [
            null,
            null,
            null,
            null,
            null,
            { className: "centered" },
            { className: "centered" },
            null,
            null,
            null,
            ],
            "processing": true,
            "serverSide": true,
            "searching": false,
            "bInfo" : false,
            "dom": 'rt<"bottom"iflp<"clear">>',
            "ajax": {
            url: ajax_url,
            data: function ( d ) {
                return $.extend( {}, d, {
                "library" :$("input:checkbox:checked").map(function(){
                              return $(this).val();
                            }).get()
                })
        },

        }});
    }

    $("input[type='checkbox']").on("change", function() {
        scrollPos =  $(window).scrollTop();
        $("#table_all_loans").DataTable().ajax.reload(function () {$(window).scrollTop(scrollPos)});

    });
    $('.dataTables_paginate').hide();
    $('#table_all_loans_length').hide();
    $(".dataTables_processing").remove();



     $("#table_all_loans").on( 'draw.dt', function () {
        var Table = $('#table_all_loans').DataTable();
        pg_info = Table.page.info();
        $('.pagedisplay')[0].value = (pg_info.page + 1) + "/" + pg_info.pages
        $(window).scrollTop(scrollPos);
    } );
     $('.pagedisplay').keypress(function(e){
        if (!e) e = window.event;
        var keyCode = e.keyCode || e.which;
        if (keyCode == '13'){
          changepage(parseInt($('.pagedisplay')[0].value.split("/")[0] ) - 1 );
          e.preventDefault();

          return false;
        }
      })
      $('.pagesize').on('change', function() {
        changelength();
      });

});