$(document).ready(function() {
  $('#example').DataTable({
  	paging: false,

    "language": {
        "sProcessing":    "Procesando...",
        "sLengthMenu":    "Mostrar _MENU_ registros",
        "sZeroRecords":   "No se encontraron resultados",
        "sEmptyTable":    "Ningún dato disponible en esta tabla",
        "sInfo":          "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
        "sInfoEmpty":     "Mostrando registros del 0 al 0 de un total de 0 registros",
        "sInfoFiltered":  "(filtrado de un total de _MAX_ registros)",
        "sInfoPostFix":   "",
        "sSearch":        "Buscar:",
        "sUrl":           "",
        "sInfoThousands":  ",",
        "sLoadingRecords": "Cargando...",
        "oPaginate": {
            "sFirst":    "Primero",
            "sLast":    "Último",
            "sNext":    "Siguiente",
            "sPrevious": "Anterior"
        },
        "oAria": {
            "sSortAscending":  ": Activar para ordenar la columna de manera ascendente",
            "sSortDescending": ": Activar para ordenar la columna de manera descendente"
        }
    }
	});

  $('#selectAll').click(function(event) {  //on click
      if(this.checked) { // check select status
          $('.checkbox-doc').each(function() { //loop through each checkbox
              this.checked = true;  //select all checkboxes with class "checkbox1"              
          });
          $('table.dataTable tbody tr').removeClass("non-print");
      }else{
          $('.checkbox-doc').each(function() { //loop through each checkbox
              this.checked = false; //deselect all checkboxes with class "checkbox1"                      
          });
          $('table.dataTable tbody tr').addClass("non-print");
      }
  });

  $('.checkbox-doc').click(function(event) {
  	if(this.checked) { // check select status

  	}else{

  	}
  }
});