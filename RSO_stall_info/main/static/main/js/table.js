$(document).ready(function() {
    var table = $('#example').DataTable( {
        lengthChange: false,
        buttons: [
            'copy',
            {
            extend: 'spacer',
            style: 'bar'
            },
            'print',
            'excel',
            'pdf',
            'colvis',
            'pageLength',

        ],
        select: true,
        autoFill: true,
        colReorder: true,
        fixedHeader: true,

    } );
    table.buttons().container()
        .appendTo( '#example_wrapper .col-md-6:eq(0)' );
} );

