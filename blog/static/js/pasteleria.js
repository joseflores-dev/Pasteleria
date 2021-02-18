
$(document).ready(function() {
    $('#mitabla').DataTable({
        "sProcessing":     "Procesando...",
        "sLengthMenu":     "Mostrar _MENU_ registros",
        "sZeroRecords":    "No se encontraron resultados",
        "sEmptyTable":     "Ningún dato disponible en esta tabla",
        "sInfo":           "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
        "sInfoEmpty":      "Mostrando registros del 0 al 0 de un total de 0 registros",
        "sInfoFiltered":   "(filtrado de un total de _MAX_ registros)",
        "sInfoPostFix":    "",
        "sSearch":         "Buscar:",
        "sUrl":            "",
        "sInfoThousands":  ",",
        "sLoadingRecords": "Cargando...",
        "oPaginate": {
            "sFirst":    "Primero",
            "sLast":     "Último",
            "sNext":     "Siguiente",
            "sPrevious": "Anterior"
        },
        "oAria": {
            "sSortAscending":  ": Activar para ordenar la columna de manera ascendente",
            "sSortDescending": ": Activar para ordenar la columna de manera descendente"
        }
    })
} );



$( "#id_cantidad" ).change(function() {
    var precio = $('.clm').html();
    var cantidad = $('#id_cantidad').val();
    var total = precio*cantidad;
    $(".totalMontoPedido").html(total*1000);
});


$("#id_cantidad").change(function(){
    var validador = $('#id_cantidad').val();
    if (validador < 0) {
        $('#id_cantidad').html('0');
        $('#id_cantidad').val(0);
        $(".totalMontoPedido").html(0);

        Swal.fire({
            type: 'error',
            title: 'Oops...',
            text: 'No Puedes Pedir Una cantidad menor a 0!',
        })
    }
    
})



$(".eliminarReservaAjax").click(function(){
    var id = $(this).attr("idreserva");
    Swal.fire({
        title: 'Estas seguro?',
        text: "Esta accion es irreversible!",
        type: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, Borrala!'
      }).then((result) => {
        if (result.value) {
            $.ajax({
                type: 'POST',
                url: '/ajax/BorrarReserva/',
                data: {'mydata': id,csrfmiddlewaretoken: window.CSRF_TOKEN},
                success: function (data, textStatus) {
                    Swal.fire({
                        title: 'Eliminado',
                        text: "Procederemos a recargar la pagina",
                        type: 'success',
                        confirmButtonColor: '#3085d6',
                        cancelButtonColor: '#d33',
                        confirmButtonText: 'OK!'
                    }).then((result) => {
                    if (result.value) {
                        location.reload(); 
                    }
                    })
                    // alert(data) // append to inner html
                },
                error: function(xhr, status, e) {
                    alert(status, e);
                }
            });
        }
      })

});


