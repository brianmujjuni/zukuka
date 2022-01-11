
function generateTransactionId(mn,mx){
    const uniform = "ZTID";
    const pt = '-'
    const yr = new Date()
    let year = yr.getFullYear()
    

    let uniformId

        rand = Math.floor(Math.random() * mx - mn + 1) + mn
        uniformId = uniform + pt + rand + pt + year
        document.querySelector('.withdraw_id').value = uniformId
    
}
generateTransactionId(10000000,90000000)

