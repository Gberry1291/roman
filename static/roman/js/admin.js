function buildsave(){

  let savebutton=document.createElement("div")
  savebutton.addEventListener("click",save)
  savebutton.classList.add("savebutton")

  let savetext=document.createElement("div")
  savetext.innerHTML="save"
  savetext.classList.add("savetext")
  savebutton.appendChild(savetext)

  document.body.appendChild(savebutton)

}
buildsave()


function save(){

  let inputinfo={}

  inputinfo["from"]=document.getElementById("whichadmin").getAttribute("data-from")

  const admininputs = document.querySelectorAll(".admininput");
  admininputs.forEach((item, i) => {
    inputinfo[item.name]=item.value
  });

  path=extension+"/saveadmin"
  whattosend=JSON.stringify(inputinfo)


  setreq()
  fetch(newreq).then(function(response) {
    return response.json()
  }).then(function(x) {
    alert(x["message"])
  });

}
