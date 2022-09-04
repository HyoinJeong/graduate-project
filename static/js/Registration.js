$('#voice_registration').click(function(){
name=$('#name').val();
age=$('#age').val();
sex=$("input[name='sex']:checked").val(); 
alert("확인버튼을 누르면 5초동안 녹음이 시작됩니다.");

var data = {
     'name':name,
     'age':age,
     'sex':sex
   }

   $.ajax({
     type: 'POST',
     url: '/register',
     data: JSON.stringify(data),
     dataType : 'JSON',
     contentType: "application/json",
     processData : false,
     success: function(data){
       alert('목소리 등록이 완료되었습니다');
     },
     error: function(request, status, error){
       alert(request.status+" "+request.statusText);
     }
   })
 })
 
  $('#check_voice').click(function(){
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
window.location.href = '/voicecheck/'+decodeURI(data);
  })
  
 
 $('#delete_user').click(function(){
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
window.location.href = '/delete_user/'+decodeURI(data);
 })
 
  $('#home').click(function(){
    //   alert(window.location.href);
    //   alert(window.location.hostname);
      window.location.href ='http://'+window.location.hostname;
 })
 
   $('#training').click(function(){
      window.location.href ='/training';
 })