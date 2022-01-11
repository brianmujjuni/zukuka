
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
        fetch("/members/search-dormantMembers",{
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
                                <td class=" ">${item.accountCurrency}</td>
                                <td class=" ">${item.firstName}</td>
                                <td class="a-right a-right ">${item.lastName}</td>
                                <td class=" ">${item.balance}/=<i class="success fa fa-long-arrow-up"></i></td>
                                <td class=" ">${item.regDate}</td>
                                <td class=" last"><a href="${'update-status' , item.accountNo }">View</a>
                                <td class=" last"><a href="${'delete-member' , item.accountNo }">Delete</a>
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