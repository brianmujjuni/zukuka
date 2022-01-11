document.querySelector('.gender').addEventListener('change',function(e){
    console.log('Hello brian ')
    Acc_Id(10000000,90000000)
})

//alert(Acc_Id(10000000,90000000))
//method calling account generator
//Acc_Id(10000000,90000000)

// function generate random account numbers

function Acc_Id(min,max){
    const uniform = "Z";
    const pt = '-'
    const yr = new Date()
    let year = yr.getFullYear()
    const sexType = ['M','F'];

    let uniformId,gender
   
    gender = document.querySelector('.gender').value

    if (gender =='Male'){
        rand = Math.floor(Math.random() * max - min + 1) + min
        uniformId = uniform+sexType[0]+ pt + rand + pt + year
        document.querySelector('.accountNo').value = uniformId

    }else{
        rand = Math.floor(Math.random() * max - min + 1) + min
        uniformId = uniform+sexType[1]+ pt + rand + pt + year
        document.querySelector('.accountNo').value = uniformId
    }
    
    
   return uniformId
}




//function to generate all transaction Ids
