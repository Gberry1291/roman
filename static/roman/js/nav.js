const slideables=document.querySelectorAll(".slideit")

slideables.forEach((item, i) => {
  item.addEventListener("click",function(){
    document.getElementById("slide").classList.toggle("slideon")
  })
});
