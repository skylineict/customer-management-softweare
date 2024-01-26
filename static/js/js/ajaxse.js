//geting all the input  form with they class and id
const usernamefield = document.getElementById('usernameinput');
const emailfield = document.getElementById('emailinput');
const feedBackArea = document.querySelector('.invalid-feedback');
const EmailfeedBackArea = document.querySelector('.EmailfeedBackArea');
const passwordField = document.getElementById('passwordinput')
const passwordField1 = document.getElementById('passwordinput1')
const usernamesuccessoutput  = document.querySelector('.usernamesuccessoutput');
const showpassword = document.querySelector('.showpassword');
const emailcheckinginput = document.querySelector('.emailcheckinginput');
const sumbitbtn = document.querySelector('.sumbitbtn');
const message  = document.querySelector('.messages')


//to show password input on form
showpassword.addEventListener('click', (e) =>{
    if(showpassword.textContent === "SHOW"){
        showpassword.textContent = 'HIDE';
        passwordField.setAttribute('type', 'text');
        passwordField1.setAttribute('type', 'text');
    }else{
        showpassword.textContent = 'SHOW';
        passwordField.setAttribute('type', 'password');
        passwordField1.setAttribute('type', 'password');
    }
});
//show password ends here 


usernamefield.addEventListener('keyup',(e) =>{
    // console.log('77777777',77777777);
    //getting the username input value
    const usernamevalue = e.target.value;
    //displaying the user validating form whenver the input is deleted
    usernamesuccessoutput.style.display = 'block';

    // this line of code is to add username cheking loader
    usernamesuccessoutput.textContent = `Validating.. ${usernamevalue}`;
  
    //removing error display on the form when user is validated
    usernamefield.classList.remove('is-invalid');

    // to stop displaying the error stlye of the user
    feedBackArea.style.display= 'none';
   
    // console.log('username is',usernamevalue);
     
    //passworking the url for the username validation from view
    if(usernamevalue.length > 0){
        fetch('/membersauth/username-validation',{
            body:JSON.stringify({username:usernamevalue }),
            method: 'POST',
        })
        .then((res) => res.json())
        .then((data) => {
             //hide the checking message when everythin is back
            usernamesuccessoutput.style.display = "none";
            // console.log('data', data);
           
           
      
            //this line of code check if there is error on the form
        if(data.username_error){
           
            //adding errors style on the form
            usernamefield.classList.add('is-invalid');
            //display the error stlye 
            feedBackArea.style.display= 'block';
            //displaying the errros on the html form
            feedBackArea.innerHTML = `<p>${data.username_error}</p>`;
             //adding button disable
             sumbitbtn.disabled = true

        }else{
            sumbitbtn.removeAttribute('disabled')
        }
});
    

    }
    

});

emailfield.addEventListener('keyup', (e) =>{
    //get my email input value 
    const emailvalue = e.target.value;
    emailcheckinginput.textContent = `validating Email`;
    emailcheckinginput.style.display = "block"
    //fetch the url on my system
    emailfield.classList.remove('is-invalid')
    EmailfeedBackArea.style.display = "none"
    
    if(emailvalue.length > 0){
        fetch('/membersauth/email-validation',{
            body: JSON.stringify({email: emailvalue}),
            method: 'POST'
        
    
        }).then(response => {
            return response.json()
        }).then(data=>{
            console.log('my eial', data);
            emailcheckinginput.style.display = "none";
     
        //display the consolog error to my form
    
        if (data.email_error){
            emailfield.classList.add('is-invalid');
            EmailfeedBackArea.style.display = "block";
            EmailfeedBackArea.innerHTML =`<p>${data.email_error}</p>`
            sumbitbtn.disabled = true
        }else{
            sumbitbtn.removeAttribute('disabled')
        }
    });
    

    }
  
});

// password validation



// function onChange(){
//     if(passwordField.value == passwordField1.value){
//         sumbitbtn.disabled = false;
//     }else{
//         sumbitbtn.disabled = true
//     }
// }


function onChange(){
    const passworvalue = document.querySelector('input[name=password1]');
    const passworvalue1  = document.querySelector('input[name=password2]');
    if (passworvalue.value == passworvalue1.value){
        passworvalue.setCustomValidity('');
        sumbitbtn.removeAttribute('disabled')
    }
    else{
        sumbitbtn.disabled = true
        passworvalue.setCustomValidity('password didnt match');
        

    }

}

