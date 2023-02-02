function getContent() {
        var div_val = document.getElementById("Main").innerHTML;
        document.getElementById("Test").value = div_val;
        if (div_val == '') {
            //alert("option alert or show error message")
            return false;
            //empty form will not be submitted. You can also alert this message like this.
        }
    }


function f() {

  let i=document.getElementById('Main')
  
  i.innerText='\n\n\n\n\n\n\n\n\n\n'
  i.focus()
}

setTimeout(() => {
  f()
  console.log('Script');
}, 1);