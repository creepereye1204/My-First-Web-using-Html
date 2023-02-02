
function Check(){
    if(window.event.keyCode === 13){ //javascript에서는 13이 enter키를 의미함

        let Id =document.getElementById('Id').value
        let Pw =document.getElementById('Pw').value
        let Form=document.getElementById('User_Info')
        if(Id==='')
        {
            alert('Please fill id')
        }
        else if(Pw==='')
        {
            alert('Please fill password')
        }
        else
        {
            console.log(Form)
            Form.submit()
              
        }
    }
}