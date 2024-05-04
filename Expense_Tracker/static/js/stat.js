const renderChart = (data, labels) => {
    const ctx = document.getElementById('myChart');
    new Chart(ctx, {
        type: 'doughnut',
        options: {
            title: {
            display: true,
            text: 'Expense Per Category',
            },
        },
        data: {
            labels:labels,
            datasets: [{
                label: 'Last 6 months expense per category',
                data: data,
                backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(255, 205, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(201, 203, 207, 0.2)'
                ],
                borderColor: [
                'rgb(255, 99, 132)',
                'rgb(255, 159, 64)',
                'rgb(255, 205, 86)',
                'rgb(75, 192, 192)',
                'rgb(54, 162, 235)',
                'rgb(153, 102, 255)',
                'rgb(201, 203, 207)'
                ],
                borderWidth: 1,
            }]
        },
    });
};

const getChartData = () => {
    console.log('Fetching data...');
    fetch('/expense_category_summary')
    .then(res => res.json())
    .then(results => {
        console.log("Results",results);
        const category_data = results.category_data;
        const [labels, data] = [Object.keys(category_data), Object.values(category_data)];
        console.log("Labels",labels);
        console.log("Data",data);
        console.log("Category Data",category_data);
        renderChart(data, labels);
    });
        
};



document.onload = getChartData();