document.addEventListener("readystatechange", (event) => {
  if (document.readyState === 'complete') {
    $("#tableContainer").hide();
  }
});

$("#check").click(function () {
    var url = $("#ResultForm").attr("data-url");
    var url_list = $("#ResultForm").attr("data-url-subject");
    var url_student_list = $("#ResultForm").attr("data-url-student");
    // var paperAuthorId = $(this).val();
    var level_id = $('#id_level').val();
    var section_id = $('#id_section').val();
    var semester_id = $('#id_semester').val();
    var check_file = $('button').val()

// The student can check their registered courses
    if (check_file=='check_courses') {
        console.log('is check_courses');
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
            reg_course();
          },
        });
    }else if (check_file=='student_courses') {
// HOD can check the list of registered students
        console.log('is student_courses');
        $.ajax({
          url: url_student_list,
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
            // to_approve();
          },
        });
    }else{
// This enable studdents to register their courses 
        console.log('is not enmpty');
        $.ajax({
          url: url_list,
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
            // src_after_file_ajax()
          },
        });
    };
});



function reg_course(){
  $('#reg-courses').click((e)=>{
  e.preventDefault();
  const formElement = document.querySelector("form#formdata");
  // var formData = new FormData(formElement);
  // var formData = new FormData();
  var selOption = formElement.selOption;
  var inputOption = formElement.inputOption;
  var checkLenght = inputOption.length;
  var selOptionArray = [];
  console.log(inputOption);
  console.log(inputOption.length);

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
  var url_file = $('form#formdata').attr("data-url-course");
  console.log(url_file)

  $.ajax({
    url: url_file,
    // type:'POST',
    data: {data:JSON.stringify(selOptionArray)},
    success: function (data) {
      alert('Courses Registered')
      location.reload()
    },
  });

});

}


// function to_approvePP(){
//   $("table").on('click','td','a', function (e) {
//     var courseId = e.target.id
//     var url = $('table').attr("data-url-to-approve");
//     feedback = e.target.id
//     console.log(e.target.id)
//     $.ajax({
//       // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
//       url: url,
//       // type:'POST',
//       data: {
//         course: JSON.stringify([courseId])
//       },
//       success: function (data) {
//         console.log(data);
//         $('.'+feedback[1]).html(data.data);
//       },
//     });

//   });
// }

// This captures checkbox status during student course registration
$("table").on('click','td','a', function (e) {
  var courseId = e.target.id
  var url = $('table').attr("data-url-course-status");
  feedback = e.target.id.split('-')
  // console.log(e.target.id.split('-'))
  $.ajax({
    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
    url: url,
    // type:'POST',
    data: {
      course: JSON.stringify([courseId])
    },
    success: function (data) {
      // console.log(data.data);
      $('.'+feedback[1]).html(data.data);
    },
  });
});

