
const searchField = document.querySelector(".depositSearch")
const tableOutput =document.querySelector(".table-output")
const appTable = document.querySelector(".app-table")
tableOutput.style.display = "none"
const noResults = document.querySelector(".no-results")
const tbody = document.querySelector(".table-body")
tableOutput.style.display = "none"

searchField.addEventListener("keyup",(e)=>{
    const searchValue = e.target.value

    if(searchValue.trim().length > 0){
        tbody.innerHTML = ""
        fetch("/deposits/search-deposit",{
            body: JSON.stringify({ searchText: searchValue}),
            method: "POST",
        })
        .then((res)=> res.json())
        .then((data)=>{
            console.log("data",data)
            appTable.style.display = "none"
            tableOutput.style.display = "block"
            if(data.length === 0){
                noResults.style.display = "block"
                tableOutput.style.display = "none"

            }else{
                noResults.style.display ="none"
                data.forEach((item)=>{
                    tbody.innerHTML += `

                    <tr class="even pointer">
                                <td class="a-center ">
                                  <input type="checkbox" class="flat" name="table_records">
                                </td>
                                
                                <td class=" ">${item.accountNo} </td>
                                <td class=" ">${item.accountName}</i></td>
                                <td class=" ">${item.accountType}</td>
                                <td class=" ">${item.accountCurrency}</td>
                                <td class="a-right a-right ">${item.oldBalance}/=</td>
                                <td class=" ">${item.depositAmount }/=<i class="success fa fa-long-arrow-up"></i> </td>
                                <td class=" "> ${item.newBalance}/=</td>
                                <td class=" ">${item.dateReg} </td>
                               
                                <td class=" last"><a href="${'update-deposit' ,item.deposit_id }">View</a>
                                <td class=" last"><a href="${'delete-deposit' ,item.deposit_id}">Delete</a>
                                </td>
                              </tr>
                    `
                })
            }
        })
    }else{
        tableOutput.style.display = "none"
        appTable.style.display = "block"
    }
})