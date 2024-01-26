
const renderChartdata = (categories,amount)=>{
    const ctx = document.getElementById('expenseschart').getContext('2d');
const myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: categories,
        datasets: [
            
            {
            label: 'last months expensive',
            data: amount,
            backgroundColor: [
                'rgba(255, 99, 132, 2)',
                'rgba(54, 162, 235, 2)',
                'rgba(255, 206, 86, 2)',
                'rgba(75, 192, 192, 2)',
                'rgba(153, 102, 255, 2)',
                'rgba(255, 159, 64, 2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: { 
        title:{
            display: true,
            'text': 'expensive for the last 4 months '
        }
       
    }
});
}

//creating a functions that will  fetch the api pr making an api call using ajax

const ChartRenders =()=>{

    console.log('fetting')

    fetch('Summary_expensive_ajax')
    .then((result) => result.json())
    .then((result) => {
    // getting the values and key of data printed in the network
    const expensivedata = result.expenses_data;
     const [categories, amount] = [Object.keys(expensivedata), Object.values(expensivedata)]
     renderChartdata(categories,amount)


    

    // console.log('result', result);
    // renderChartdata([], []);

    

    });

};
document.onload = ChartRenders();






















//creating a function and hiding the chaart insid the function
// const renderchar =(data, labels)=>{
//     const ctx = document.getElementById('ourmain').getContext('2d');
//  const myChart = new Chart(ctx, {
//      type: 'bar',
//      data: {
//          labels: ['monday','turedays', 'friday','saturday','friday','sunday','precius'],
//          datasets: [{
//              label: 'Last 6 Months expensive',
//              data: [12, 19, 3, 5, 2, 3],
//              backgroundColor: [
//                  'rgba(255, 99, 132, 1)',
//                  'rgba(54, 162, 235, 1)',
//                  'rgba(255, 206, 86, 1)',
//                  'rgba(75, 192, 192, 1)',
//                  'rgba(153, 102, 255, 1)',
//                  'rgba(255, 159, 64, 1)'
//              ],
//              borderColor: [
//                  'rgba(255, 99, 132, 1)',
//                  'rgba(54, 162, 235, 1)',
//                  'rgba(255, 206, 86, 1)',
//                  'rgba(75, 192, 192, 1)',
//                  'rgba(153, 102, 255, 1)',
//                  'rgba(255, 159, 64, 1)'
//              ],
//              borderWidth: 1
//          }]
//      },
//      options: {
//         title:{
//             display: true,
//             text: 'expensive Catergory',
//         },
         
//      },
//  });

// }

// const  getchartdata = () =>{
//     console.log('fetting')
//     fetch('/Summary_expensive_ajax')
//     .then((res) => res.json())
//     .then((results) => {
//         console.log('result', results);
//         renderchar([], []);

//     });


// };

// document.onload  = getchartdata();











 