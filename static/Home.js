var Respones;
let url='https://MyOwnPlanServer.iostream1204.repl.co/Content/'
var Test=''


// async function Contetnt() {
//     await fetch('https://MyOwnPlanServer.iostream1204.repl.co/Content').then(response => response.json()).then(res=>{ Respones=res; })	
//     console.log(Respones[0])
    
    
// }



function Check_Index(Raw_Text) {
  var Index=''
    for(var i=1;i<Raw_Text.length;i++){
      if(Raw_Text[i]!=']'){
        Index=Index+Raw_Text[i]
      }
      else{
        location.href=url+Index
      }
    }
  
}

// setInterval(
//   async function f(params) {
//     await fetch('https://MyOwnPlanServer.iostream1204.repl.co/Lists').then(response => response.json()).then(res=>{ Respones=res; })	
//     console.log(Respones[0])
//     let Lists=document.getElementById('Lists')
//     Lists.append('안녕')
//   }, 2000);
async function f(params) {
    await fetch('https://MyOwnPlanServer.iostream1204.repl.co/Lists').then(response => response.json()).then(res=>{ Respones=res; })	
    
    const Lists=document.getElementById('Lists')
    
  
    for(var i=Respones.length-1;i>-1;i--){
      var Home = document.createElement("div");
      var Index=document.createElement("a");
      var Title = document.createElement("a");
     
      // var Main = document.createElement("h3");
      Index.textContent="["+(i+1).toString()+']  '
      Title.textContent = Respones[i][1];
      
      // Main.innerHTML=Respones[i][2];
      // Main.setAttribute("style","display:None;")
      // Title.setAttribute("onclick", onclick="Toggle()");
      // Title.click();
      
      Home.appendChild(Index)
      Home.appendChild(Title)
      
      Home.setAttribute("onclick","Check_Index(this.textContent)");
      
      

      


      
      Lists.appendChild(Home)
      // Lists.appendChild(Main);
    }
    
}
f()