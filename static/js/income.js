const searchvalue = document.getElementById('searchText');
const tableapp  =   document.getElementById('table-app');
const pagination = document.getElementById('pagination-app');
const  seachingtable = document.getElementById('tablesearchbox');
const tablebody = document.getElementById('tablebody')
seachingtable.style.display = 'none';



searchvalue.addEventListener('keyup',(e) =>{
    const searchtext = e.target.value;
    if(searchtext.length > 0){
        tablebody.innerHTML ="";

        fetch('/incomeapp/income-searching',{
            body: JSON.stringify({searchText:searchtext}),
            method: 'POST'

        }).then(response =>{  
            return response.json()
        }).then(data=>{

            console.log('my eial', data);
        
            tableapp.style.display='none';
            pagination.style.display= 'none';
            seachingtable.style.display= 'block'

        if(data.length===0){

           seachingtable.innerHTML = 'result not found, try again';

        }else{
           data.forEach(item => {
            tablebody.innerHTML += `
            <tr>
        <td>${item.incomeAmount}</td>
      <td>${item.incomesource}</td>
      <td>${item.incometype}</td>
      <td>${item.inconmedate}</td>
      
     
          </tr>`;
               
           });
        }

        });

    }else{  tableapp.style.display='block';
           pagination.style.display= 'block';
           seachingtable.style.display="none";
    }
  
  

    
});


