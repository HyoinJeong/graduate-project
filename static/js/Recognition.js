$('#voice_recognition').click(function(){
name=$('#name').val();
age=$('#age').val();
sex=$("input[name='sex']:checked").val(); 
// alert(name+age+sex);

var data = {
     'name':name,
     'age':age,
     'sex':sex
   }

var data = name+age+sex;
window.location.href = '/recognition/'+decodeURI(data);

 })
 
$('#recording_recognition').click(function(){
url=window.location.pathname    
user_info=url.split('/')[2]

var data = user_info

alert("5초동안 녹음이 시작됩니다.");

  $.ajax({
     type: 'POST',
     url: '/recording_recognition',
     data: JSON.stringify(data),
     dataType : 'JSON',
     contentType: "application/json",
     processData : false,
     success: function(data){
         var result = data.result;
         if (result=="success"){
             alert('화자인식에 성공하셨습니다.');
         }
         else{
             alert('화자인식에 실패하셨습니다. 다시 시도해주세요.');
         }
     },
     error: function(request, status, error){
      alert(request.status+" "+request.statusText);
     }
  })

  })