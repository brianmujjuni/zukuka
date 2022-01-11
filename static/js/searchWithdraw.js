const searchText = document.querySelector('#withdrawSearch');
const tableOutput = document.querySelector('.table-output');
const appTable =document.querySelector('.app-table');
tableOutput.style.display = 'none';
const noResults = document.querySelector(".no-results");
const tbody = document.querySelector('.table-body');

searchText.addEventListener("keyup",(e)=>{
  const searchValue = e.target.value;

  if (searchValue.trim().length > 0){
    tbody.innerHTML = ''

    fetch("/withdraws/search-withdraw",{
      body: JSON.stringify({ searchText: searchValue}),
      method: "POST"
    })
    .then((res) => res.json())
    .then((data)=>{
      console.log('data',data)
      appTable.style.display='none'
      tableOutput.style.display ='block'

      if(data.length === 0){

        noResults.style.display = "none";
        tableOutput.style.display = "none";

      }else{
        noResults.style.display = "none";
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
            <td class="a-right a-right ">${item.oldBalance }</td>
            <td class=" "> ${item.withdrawAmount }/=<i class="success fa fa-long-arrow-down"></i></td>
            <td class=" ">${item.newBalance } </td>
            <td class=" ">${item.dateReg } </td>
            <td class=" last"><a href="${'update-withdraw' , item.withdraw_id }">View</a>
            <td class=" last"><a href="${'delete-withdraw' , item.withdraw_id}">Delete</a>
            </td>
          </tr>

           `
        })
          
      }
    })
  }else{
    tableOutput.style.display = "none";
    appTable.style.display = "block";
  } 
});