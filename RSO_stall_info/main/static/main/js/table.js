$(document).ready(function() {
    var table = $('#example').DataTable( {
        dom: '<"d-flex justify-content-between mb-4"Bf>rt<"d-flex justify-content-between"ip>',
        lengthChange: false,
        buttons: [
            'pageLength',
            'colvis',
            {
                extend: 'copy',
                split: [ 'pdf', 'excel', 'print'],
            },
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

