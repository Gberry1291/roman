const slideables=document.querySelectorAll(".slideit")

slideables.forEach((item, i) => {
  item.addEventListener("click",function(){
    document.getElementById("slide").classList.toggle("slideon")
  })
});

const questionables=document.querySelectorAll(".togquestion")
questionables.forEach((item, i) => {
  item.addEventListener("click",function(){
    document.getElementById("questionhouse").classList.toggle("questionon")
  })
});


var startpat=window.location.href
let pattern=/\S*\/\/\S+?(?=\/)/
var extension=startpat.match(pattern)[0];
var newreq=""
var whattosend=""
var path=""
const csrftoken = getCookie('csrftoken');
function setreq(){
  newreq = new Request(
      path,
      {
          method: 'POST',
          headers: {'X-CSRFToken': csrftoken},
          mode: 'same-origin', // Do not send CSRF token to another domain.
          body: whattosend
      }
  );
}
function getCookie(cname) {
  let name = cname + "=";
  let decodedCookie = decodeURIComponent(document.cookie);
  let ca = decodedCookie.split(';');
  for(let i = 0; i <ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}
function setCookie(cname, cvalue, exdays) {
  const d = new Date();
  d.setTime(d.getTime() + (exdays*24*60*60*1000));
  let expires = "expires="+ d.toUTCString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";"+"SameSite=None; Secure";
}

document.getElementById("newquestion").addEventListener("click",addToEmailList)
function addToEmailList(){


    let name=document.getElementById('questionnameinput').value
    let email=document.getElementById('questionemailinput').value
    let message=document.getElementById("questionjobinput").value

    let newperson={"name":name,"email":email,"message":message}

    path=extension+"/question"
    whattosend=JSON.stringify(newperson)

    setreq()
    fetch(newreq).then(function(response) {
      return response.json()
    }).then(function(x) {
      alert(x["message"])
    });

}
