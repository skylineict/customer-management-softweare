const incomechardrender =(incomesource, amountincome) =>{

    const ctx = document.getElementById('incomechart');
const myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: incomesource,
        datasets: [{
            label: '# of Votes',
            data: amountincome,
            backgroundColor: [
                'rgba(255, 99, 132, 2)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 2)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
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
        title: {
            display: true,
            'text': 'expensive for the last 4 months '
        }
    }
});

}

const rendercharincom =()=>{
    console.log('trying my fatch')
    fetch('/incomesummary_ajax')
    .then((rest) => rest.json())
    .then((result) =>{

        const incomesdate = result.income_data;
        const [incomesource,amountincome] = [Object.keys(incomesdate), Object.values(incomesdate)]
        console.log('result',result);                                                                                                      


        incomechardrender(incomesource,amountincome)


    });

    
};
document.onload = rendercharincom();

