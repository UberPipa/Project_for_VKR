$(document).ready(function() {
    var table = $('#example').DataTable( {
        lengthChange: false,
        buttons: [
            'pageLength',
            {
            extend: 'spacer',
            style: 'bar'
            },
            'copy',
            'print',
            'excel',
            'pdf',
            {
            extend: 'spacer',
            style: 'bar'
            },
            'colvis',
        ],
        select: true,
        autoFill: true,
        colReorder: true,
        fixedHeader: true,
        searching: true,
    } );
    table.buttons().container()
        .appendTo( '#example_wrapper .col-md-6:eq(0)' );
} );

