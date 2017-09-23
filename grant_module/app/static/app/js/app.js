$(function () {
  urlname = ''
  $(".js-create-student").click(function () {
    urlname=$(this).attr('data')
    $.ajax({

      url: urlname,
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-student").modal('show');
      },
      success: function (data) {
        $("#modal-student .modal-content").html(data.html_form);
      }
    });
  });



    $("#modal-student").on("submit", ".student-create", function () {


    var form = $(this);
    $.ajax({
      url: urlname,
      data: form.serialize(),
      type: 'post',
      dataType: 'json',
      success: function (data) {

        if (data.form_is_valid) {
          $("table tbody").html(data.html_student_list);
          $("#modal-student").modal('hide');
          
          
        }
        else {
          $("table tbody").html(data.html_student_list);
        }

      }
    });
    return false;
  });

});

