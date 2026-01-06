let date = new Date();
let year = date.getFullYear();
let month = date.getMonth();

var eventinfo = JSON.parse(document.getElementById('alldays').textContent);

const day = document.querySelector(".calendar-dates");
const currdate = document.querySelector(".calendar-current-date");
const prenexIcons = document.querySelectorAll(".calendar-navigation");

const months = [
  "January", "February", "March", "April", "May", "June",
  "July", "August", "September", "October", "November", "December"
];

let clickedDay = null;
let selectedDayElement = null;
const manipulate = () => {
  let dayone = new Date(year, month, 1).getDay();
  let lastdate = new Date(year, month + 1, 0).getDate();
  let dayend = new Date(year, month, lastdate).getDay();
  let monthlastdate = new Date(year, month, 0).getDate();

  let daycount=0

  let lit = "";

  for (let i = dayone; i > 0; i--) {
    daycount+=1
    let thedate=i+"-"+(month-1)+"-"+year
    if (eventinfo[thedate]) {
      lit += `<div class="day inactive" data-month="${month-1}" data-year="${year}" data-day="${monthlastdate - i + 1}"> <div class="center">${monthlastdate - i + 1}</div> </div>`
      lit += `</div>`

    }else{
      lit += `<div class="day inactive" data-month="${month-1}" data-year="${year}" data-day="${monthlastdate - i + 1}"> <div class="center">${monthlastdate - i + 1}</div> </div>`;
    }
  }


  for (let i = 1; i <= lastdate; i++) {

    daycount+=1

    let isToday = (i === date.getDate()
      && month === new Date().getMonth()
      && year === new Date().getFullYear()) ? "active" : "";

    let thedate=i+"-"+(month+1)+"-"+year

    if (eventinfo[thedate]) {

      lit += `<div class="eventday semi" data-day="${i}" data-month="${month+1}" data-year="${year}"> <div class="fullfill"><div class="center ${isToday}">${i}</div></div>`;
      lit += `</div>`

    }else{
      lit += `<div class="day" data-day="${i}" data-month="${month+1}" data-year="${year}"> <div class="center ${isToday}">${i}</div> </div>`;
    }

  }


  for (let i = dayend; i < 6; i++) {

    let thedate=(i - dayend + 1)+"-"+(month+2)+"-"+year
    if (eventinfo[thedate]) {
      lit += `<div class="eventday semi inactive" data-month="${month+2}" data-year="${year}" data-day="${i - dayend + 1}"> <div class="fullfill"><div class="center">${i - dayend + 1}</div> </div>`
      lit += `</div>`

    }else{
      lit += `<div class="day inactive" data-day="${i - dayend + 1}" data-month="${month+2}" data-year="${year}"> <div class="center">${i - dayend + 1}</div> </div>`;
    }

    daycount+=1

  }


  day.style.gridTemplateRows = `repeat(${daycount/7},${100/(daycount/7)}%)`;

  currdate.innerText = `${months[month]} ${year}`;
  day.innerHTML = lit;

  addClickListenersToDays();
  addEventDayClicks();
};

var selectedday=""
function addClickListenersToDays() {
  const allDays = day.querySelectorAll('.day');
  allDays.forEach(li => {
    li.addEventListener('click', () => {

      let clickedDay = li.getAttribute('data-day');
      let clickedMonth = li.getAttribute('data-month');
      let clickedYear = li.getAttribute('data-year');
      selectedday = (clickedYear+"-"+clickedMonth+"-"+clickedDay)
      togday()
    });
  });
}
function addEventDayClicks(){
  const allEventDays = day.querySelectorAll('.eventday');
  allEventDays.forEach(li => {
    li.addEventListener('click', () => {

      let clickedDay = li.getAttribute('data-day');
      let clickedMonth = li.getAttribute('data-month');
      let clickedYear = li.getAttribute('data-year');
      let finallist = (clickedDay+"-"+clickedMonth+"-"+clickedYear)
      selectedday = (clickedYear+"-"+clickedMonth+"-"+clickedDay)
      togday()
    });
  });
}

manipulate();
prenexIcons.forEach(icon => {
  icon.addEventListener("click", () => {
    month = icon.id === "calendar-prev" ? month - 1 : month + 1;

    if (month < 0 || month > 11) {
      date = new Date(year, month, new Date().getDate());
      year = date.getFullYear();
      month = date.getMonth();
    } else {
      date = new Date();
    }

    clickedDay = null;
    selectedDayElement = null;

    manipulate();
  });
});

let dtogelements=document.getElementsByClassName("togday")
for (var i = 0; i < dtogelements.length; i++) {
  dtogelements[i].addEventListener("click",togday)
}

function togday(){
  document.getElementById('daypage').classList.toggle("selected")
}

document.getElementById("savedaychanges").addEventListener("click",saveday)
function saveday(){

  let appname=document.getElementById('appname').value
  let appemail=document.getElementById('appemail').value
  let apptime=document.getElementById('apptime').value
  let appmessage=document.getElementById('appmessage').value

  let daydic={"date":selectedday,"appname":appname,"appemail":appemail,"apptime":apptime,"appmessage":appmessage}

  path=extension+"/saveday"
  whattosend=JSON.stringify(daydic)

  setreq()
  fetch(newreq).then(function(response) {
    return response.json()
  }).then(function(x) {
    eventinfo=x
    manipulate()
    togday()
  });
}
