document.getElementById('mailtog').addEventListener("click",function(){
  document.getElementById('personlist').classList.toggle("showlist")
})

count=parseInt(document.getElementById("count").innerHTML)

crosses=document.querySelectorAll(".crossclip")
crosses.forEach((item, i) => {
  item.addEventListener("click",function(){
    if (!item.classList.contains("selected")) {
      let which=item.getAttribute("data-count")
      document.getElementById("sendy"+which).classList.add("off")
      item.classList.add("selected")
      document.getElementById("check"+which).classList.remove("selected")
      count-=1;
      document.getElementById("count").innerHTML=count
    }

  })
});

checks=document.querySelectorAll(".checkclip")
checks.forEach((item, i) => {

  item.addEventListener("click",function(){
    if (!item.classList.contains("selected")) {
      let which=item.getAttribute("data-count")
      document.getElementById("sendy"+which).classList.remove("off")
      item.classList.add("selected")
      document.getElementById("cross"+which).classList.remove("selected")
      count+=1;
      document.getElementById("count").innerHTML=count
    }

  })

});

function buildemaillist(){

  let sendys=document.querySelectorAll(".sendy")

  let mylist=[]
  sendys.forEach((item, i) => {
    if (!item.classList.contains("off")) {
      mylist.push(item.getAttribute("data-email"))
    }
  });

  return mylist

}

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

document.getElementById("send").addEventListener("click",addToEmailList)
function addToEmailList(){


    let subject=document.getElementById('subject').value
    let linktoimage=document.getElementById('linktoimage').value
    let message=document.getElementById("message").value
    let guys=buildemaillist()


    let newperson={"subject":subject,"linktoimage":linktoimage,"message":message,"guys":guys}

    path=extension+"/sendemail"
    whattosend=JSON.stringify(newperson)

    setreq()
    fetch(newreq).then(function(response) {
      return response.json()
    }).then(function(x) {
      alert(x["message"])
    });

}
