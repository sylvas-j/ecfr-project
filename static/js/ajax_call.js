document.addEventListener("readystatechange", (event) => {
  if (document.readyState === 'complete') {
    $("#tableContainer").hide();
  }
});

$("#check").click(function () {
    var url = $("#ResultForm").attr("data-url");
    var url_file = $("#ResultForm").attr("data-url-file");
    // var paperAuthorId = $(this).val();
    var level_id = $('#id_level').val();
    var section_id = $('#id_section').val();
    var semester_id = $('#id_semester').val();
    var check_file = $('button').val()

// This student detail to check their results
    if (check_file=='') {
        console.log('is empty');
        $.ajax({
          url: url,
          data: {
            level: level_id,
            section: section_id,
            semester: semester_id,
          },
          success: function (data) {
            // console.log(data)
            // $("#selectForm").hide();
            $("#tableContainer").show();
            $("#tableContainer").html(data);
            src_after_file_ajax()
          },
        });
    }else{

// This pull out results files for download
        console.log('is not enmpty');
        $.ajax({
          url: url_file,
          data: {
            level: level_id,
            section: section_id,
            semester: semester_id,
          },
          success: function (data) {
            // console.log(data)
            // $("#selectForm").hide();
            $("#tableContainer").show();
            $("#tableContainer").html(data);
            src_after_file_ajax()
          },
        });
    };
});




$('#reg-courses').click((e)=>{
  e.preventDefault();
  const formElement = document.querySelector("form");
  // var formData = new FormData(formElement);
  // var formData = new FormData();
  var selOption = formElement.selOption;
  var inputOption = formElement.inputOption;
  var checkLenght = inputOption.length;
  var selOptionArray = [];

  for(var i=0; i<checkLenght; i++){
    if (inputOption[i].checked) {
      selOptionArray.push(selOption[i].value)
      // console.log(selOptionArray)
    }

  } //end for loop

  console.log(selOptionArray)
  // console.log(formData.getAll('selOption'))
  // const values = [...formData.entries()];
  // console.log(values);
  var url_file = $('form').attr("data-url-course");
  console.log(url_file)

  $.ajax({
    url: url_file,
    // type:'POST',
    data: {data:JSON.stringify(selOptionArray)},
    success: function (data) {
      // console.log(data)
      // console.log('checking output')
    },
  });

});


$("table").on('click','td','a', function (e) {
  var courseId = e.target.id
  var url = $('table').attr("data-url-course-status");
  feedback = e.target.id.split('-')
  // console.log(e.target.id.split('-'))
  // console.log(url)
  $.ajax({
    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
    url: url,
    // type:'POST',
    data: {
      course: JSON.stringify([courseId])
    },
    success: function (data) {
      console.log(data.data);
      console.log('okk')
      $('.'+feedback[1]).html(data.data);
    },
  });
});


