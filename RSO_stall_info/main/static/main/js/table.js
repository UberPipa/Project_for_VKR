$(document).ready(function() {
    var table = $('#example').DataTable( {
        lengthChange: true,
        buttons: [ 'copy',  'print', 'excel', 'pdf', 'colvis'],
        select: true,
        autoFill: true,
        colReorder: true,
        fixedHeader: true

    } );

    table.buttons().container()
        .appendTo( '#example_wrapper .col-md-6:eq(0)' );
} );

