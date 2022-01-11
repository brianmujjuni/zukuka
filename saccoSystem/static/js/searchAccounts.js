
const searchField = document.querySelector("#searchField")
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
        fetch("/accounts/search_accounts",{
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
                                <td class=" ">${item.accountNo}</td>
                                <td class=" ">${item.accountName}</td>
                                <td class=" ">${item.accountType}</td>
                                <td class=" ">${item.firstName}</td>
                                <td class=" ">${item.lastName}</td>
                                <td class="a-right a-right ">${item.accountStatus}</td>
                                <td class=" ">${item.date1} </td>
                                <td class=" last"><a href="${ update-account ,item.accountNo }">View</a>
                                <td class=" last"><a href="${'delete-account' ,item.accountNo }">Delete</a>
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