$(document).ready(function() {
    var table = $('#example').DataTable( {
        dom: '<"d-flex justify-content-between mb-4"Bf>rt<"d-flex justify-content-between"ip>',
        lengthChange: false,
        buttons: [
            'pageLength',
            {
                extend: 'spacer',
                style: 'bar',
            },
            'colvis',
            {
                extend: 'spacer',
                style: 'bar',
            },
            {
                extend: 'copy',
                split: [ 'pdf', 'excel', 'print'],
            },
//            {
//            extend: 'spacer',
//            style: 'bar'
//            },

        ],
        select: true,
        autoFill: true,
        colReorder: true,
        fixedHeader: true,
        searching: true,
    } );
        table.buttons( 1, null ).container().appendTo(
        table.table().container()
    );
} );

