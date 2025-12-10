const quotes=[
  ["Mountaintops inspire leaders but valleys mature them.","- Winston Churchill"],
  ["some quote by someone cool","- Gary"],
  ["Lead from the back and let others believe they are in front.","- Nelson Mandela"],
  ["One voice can change a room.","- Barack Obama"],
  ["Don’t tell people how to do things, tell them what to do and let them surprise you with their results.","- George Patton"],
  ["Winners focus on opportunity. Losers focus on obstacles. Leaders focus on solutions.","- Maxime Lagacé"],
  ["Innovation distinguishes between a leader and a follower.","- Steve Jobs"],
  ["The real leader has no need to lead – he is content to point the way.","- Henry Miller"],
  ["Great leaders take much responsibility and little credit.","- Tyler Winklevoss"],
  ["Leadership is the capacity to translate vision into reality.","- Warren Bennis"],
  ["As we look ahead into the next century, leaders will be those who empower others.","- Bill Gates"],
  ["A man who wants to lead the orchestra must turn his back on the crowd.","- Max Lucado"],
  ["If you aren’t willing to be mocked, you’ll never be able to lead.","- Naval Ravikant"],
  ["You don’t need a title to be a leader.","- Mark Sanborn"],
  ["A leader is a dealer in hope.","- Napoleon Bonaparte"],
  ["Great spirits have always found violent opposition from mediocrities.","- Albert Einstein"],
  ["I’ve learned that people will forget what you said, people will forget what you did, but people will never forget how you made them feel.","Maya Angelou"],
  ["I have not failed. I’ve just found 10000 ways that won’t work.","- Thomas Edison"],
  ["To lead people, walk behind them.","- Lao Tzu"],
  ["If your actions inspire others to dream more, learn more, do more and become more, you are a leader.","John Quincy Adams"],
  ["The greatest leader is not necessarily the one who does the greatest things. He is the one that gets the people to do the greatest things.","- Ronald Reagan"],
  ["A true leader has the confidence to stand alone, the courage to make tough decisions, and the compassion to listen to the needs of others.","- Douglas MacArthur"],
  ["Leadership and learning are indispensable to each other.","- John F.Kennedy"],
  ["No man will make a great leader who wants to do it all himself, or to get all the credit for doing it.","- Andrew Carnegie"],
  ["Leaders aren’t born, they are made. And they are made just like anything else, through hard work","- Vince Lombardi"],
  ["Great leaders are almost always great simplifiers, who can cut through argument, debate, and doubt to offer a solution everybody can understand","- Colin Powell"],
  ["Earn your leadership every day","- Michael Jordan"],
  ["I am not afraid of an army of lions led by a sheep; I am afraid of an army of sheep led by a lion.","- Alexander the Great"],
]
var chosen=Math.floor(Math.random() * (27 - 0)) + 0;
const quoteamount=27
const quote=document.getElementById("quote")
const person=document.getElementById("person")
const barbar=document.getElementById("loadingbar")
quote.innerHTML=quotes[chosen][0]
person.innerHTML=quotes[chosen][1]
function nextquote(){
  $("#quotes").animate({
    "opacity":"0"
  },500,function(){
    chosen+=1
    if (chosen>quoteamount) {
      chosen=0
    }
    quote.innerHTML=quotes[chosen][0]
    person.innerHTML=quotes[chosen][1]
    $("#quotes").animate({
      "opacity":"1"
    },500,function(){startbar()})
  })
}
function startbar(){
  loadingbar.style.width="0%"
  $("#loadingbar").animate({
    "width":"100%"
  },8000,function(){nextquote()})
}
startbar()

function makesound(){
  $("#sound").animate({
    "height":"5.9vh",
    "top":"-=.8vh",
    "left":"-=.8vh",
    "opacity":"0"
  },800,function(){
    $("#sound").css({
      "height":"4.55vh",
      "top":"17.5%",
      "left":"+=.8vh",
      "transform": 'rotate('+Math.floor(Math.random() * (359 - 1 + 1)) + 1+'deg)',
      "opacity":"1"
      })
      makesound()
    })
}
makesound()
