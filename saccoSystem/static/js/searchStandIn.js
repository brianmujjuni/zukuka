
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
        fetch("/accounts/search_standin",{
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
                                <td class=" ">${item.firstName}</td>
                                <td class=" ">${item.lastName}</td>
                                <td class=" ">${item.gender}</td>
                                <td class=" ">${item.contact} </td>
                                <td class=" ">${item.regBy} </td>
                                <td class=" ">${item.regDate} </td>
                                <td class=" last"><a href="${  'update-standIn' ,item.id }">View</a>
                                <td class=" last"><a href="${ 'delete-standIn' ,item.id }">Delete</a>
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