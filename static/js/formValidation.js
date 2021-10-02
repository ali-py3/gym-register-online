let form = document.querySelector('.myForm')
let firstName = document.getElementById('fname')
let lastName = document.getElementById('lname')
let address = document.getElementById('address')
let birthYear = document.getElementById('birth')
let phone = document.getElementById('birth')
let nationalCode = document.getElementById('national-code')
let canc = document.getElementById('btn-cancel')
    
    form.addEventListener('submit', e => {
        if(firstName.value === ""){
        
            alert('نام الزامی است')
        }
        else if(lastName.value === ""){
        
            alert("نام خانوادگی الزامی است")
        }
        else if(address.value === ""){
           
            alert("آدرس الزامی میباشد")
        }
        else if(phone.value ===""){
         
            alert("شماره تلفن الزامی است")
        }
        else if(nationalCode.value === "" && nationalCode.value.length < 10){
            alert("invalid national code")
        }
        else if(birthYear.value === ""){
            
            alert("تاریخ تولد الزامی است")
        }
    } )

    birthYear.addEventListener('change' , (e) => {
  
})

 canc.addEventListener('click' , (e) => {
            e.stopPropagation()
          
})
    
