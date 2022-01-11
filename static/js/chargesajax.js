
document.querySelector('.depositPrint').addEventListener('click',(e)=>{
 
 printlayer('.depositData')
})

function printlayer(layer){
    let generator = window.open(",'name,")
    let layetext = document.querySelector(layer)
    generator.document.write(layetext.innerHTML.replace("Print Me"))
    generator.document.close()
    generator.print()
    generator.close()
}

window.querySelector('.depositData').print()