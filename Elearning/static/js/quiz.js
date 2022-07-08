const quizForm = document.getElementById("quiz-form");
const csrf = document.getElementsByName("csrfmiddlewaretoken");
const url = window.location.href;
const scoreBox = document.getElementById("score-box");
const resultFinal = document.getElementById("result-box");


const timerBox = document.getElementById("timer-box");

  const CountDown = (time) => {
      
      if (time.toString().length<2) {
          timerBox.innerHTML = `<b>0${time}:00</b>`
      } else {
          timerBox.innerHTML = `<b>${time}:00</b>`
  
      }
      let min= time-1
      let sec=60
      let dispSec
      let disMin
      const inter=setInterval(() => {
        sec --
        if(sec<0){
          sec=59
          min --
        }
        if (min.toString().length<2){
          disMin='0'+ min
        } else{
          disMin = min
        }
        if (sec.toString().length<2){
          dispSec='0'+ sec
        }
        else {
          dispSec = sec
        }
        if(min === 0  && sec === 0){
          console.log('time over')
          clearInterval(inter)
          alert('time over')
          sendData()
        }


        timerBox.innerHTML= `<b>${disMin}:${dispSec}</b>`



      },1000)
    
  }

CountDown(time)
const sendData = () => {
  
  const elements = [...document.getElementsByClassName("answer")];
  const data = {};
  data["csrfmiddlewaretoken"] = csrf[0].value;
  elements.forEach((el) => {
    if (el.checked) {
      data[el.name] = el.value;
    } else {
      if (!data[el.name]) {
        data[el.name] = null;
      }
    }
  });

  
  $.ajax({
    type: "POST",
    url: `${url}save/`,
    data: data,
    success: function (response) {
      const results=response.results
      //console.log(results)
      quizForm.classList.add('not-visible')
      
      scoreBox.innerHTML =  `${response.passed ? 'Congratulation! ' : 'You need to try again.' } Your result is ${response.marks} % `
      const mystyle2=['container','p-3', 'text-align', 'h3','bg-info']
      scoreBox.classList.add(...mystyle2)
      results.forEach(result=>{
          const divv=document.createElement('div')
          for (const [question, resp] of Object.entries(result)){
              divv.innerHTML+=question
              const mystyle=['container','p-3', 'text-align', 'h3',]
              divv.classList.add(...mystyle)

              if (resp=='not answered'){
                divv.innerHTML+='- not answered'
                divv.classList.add('bg-danger')
                            
              }
              else{
                  const answer = resp['answered']
                  const correct_answer = resp['correct_answer']
                  //console.log(answer,correct_answer)
                  if (answer== correct_answer){
                    divv.classList.add('bg-success')
                    divv.innerHTML+=`answered:  ${answer} `

                  }
                  else{
                    divv.classList.add('bg-danger')
                    divv.innerHTML += ` | correct answer: ${correct_answer} `
                    divv.innerHTML += ` | Your answer: ${answer} `
                  }
              }
          }
          //const mysyle2 =document.getElementsByTagName('Body')[0]
          //mysyle2.append(divv)
          
         
          resultFinal.append(divv)
          
      })
     
    },
    error: function (error) {
      console.log(error);
    },
  });
};
quizForm.addEventListener("submit", (e) => {
  e.preventDefault();
  sendData();
});



